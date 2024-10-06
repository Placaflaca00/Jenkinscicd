pipeline {
    agent any
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-service-accountw')
        TF_VAR_project_id = 'tecnologai-emergente'
        VM_IP = '34.67.33.86'  // Reemplaza con la IP de tu VM
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Placaflaca00/Jenkinscicd.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat '''
                set PYTHONPATH=%CD%
                pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        stage('Deploy API and Frontend') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-ssh-key', keyFileVariable: 'SSH_KEY_FILE', usernameVariable: 'SSH_USER')]) {
                    // Deploy API
                    bat """
                    scp -i %SSH_KEY_FILE% -o StrictHostKeyChecking=no -r api %SSH_USER%@%VM_IP%:/var/app/api/
                    """
                    // Deploy Frontend
                    bat """
                    scp -i %SSH_KEY_FILE% -o StrictHostKeyChecking=no -r frontend %SSH_USER%@%VM_IP%:/var/app/frontend/
                    """
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
