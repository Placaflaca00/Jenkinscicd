# Jenkins CI/CD Pipeline for API and Frontend Deployment

Este proyecto utiliza un pipeline de **Jenkins** para automatizar el despliegue de dos componentes principales: el backend (**API**) y el frontend, en una máquina virtual (VM) alojada en **Google Cloud**. A continuación, se explica cómo está configurado el pipeline y cómo se sincronizan las carpetas entre el repositorio y la VM.


## Funcionalidad del Pipeline

El pipeline en Jenkins se compone de varias etapas clave:

1. **Checkout**:
   - En esta etapa, Jenkins clona el repositorio desde GitHub. Esto asegura que siempre se esté trabajando con la versión más reciente del código fuente.
   - Comando usado:
     ```groovy
     git url: 'https://github.com/Placaflaca00/Jenkinscicd.git', branch: 'main'
     ```

2. **Build**:
   - Instala las dependencias necesarias del proyecto utilizando Python. Este paso asegura que todas las librerías necesarias estén disponibles para ejecutar la aplicación.
   - Comandos usados:
     ```groovy
     bat 'python -m pip install --upgrade pip'
     bat 'pip install -r requirements.txt'
     ```

3. **Test**:
   - Ejecuta pruebas unitarias con **pytest** para garantizar que las modificaciones recientes no hayan roto el código.
   - Comandos usados:
     ```groovy
     bat '''
     set PYTHONPATH=%CD%
     pytest --junitxml=test-results.xml
     '''
     ```

4. **Deploy (API y Frontend)**:
   - En esta etapa, el pipeline sincroniza los archivos desde el repositorio hacia la máquina virtual en Google Cloud.
   - Se utiliza **SCP** (Secure Copy Protocol) para transferir los archivos de las carpetas `api` y `frontend` a las rutas correspondientes en la VM.
   - Jenkins utiliza credenciales SSH para acceder de manera segura a la VM y realizar la transferencia de archivos.

## Sincronización de Carpetas (API y Frontend)

La sincronización de los directorios `api` y `frontend` se realiza utilizando el siguiente código en el Jenkinsfile:

```groovy
withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-ssh-key', keyFileVariable: 'SSH_KEY_FILE', usernameVariable: 'SSH_USER')]) {
    // Deploy API
    bat """
    scp -i %SSH_KEY_FILE% -o StrictHostKeyChecking=no -r api %SSH_USER%@%VM_IP%:/var/api/
    """
    // Deploy Frontend
    bat """
    scp -i %SSH_KEY_FILE% -o StrictHostKeyChecking=no -r frontend %SSH_USER%@%VM_IP%:/var/frontend/
    """
}
