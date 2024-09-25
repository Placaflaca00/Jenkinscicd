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
                bat 'pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-ssh-key', keyFileVariable: 'SSH_KEY_FILE', usernameVariable: 'SSH_USER')]) {
                    bat """
                    scp -i %SSH_KEY_FILE% -o StrictHostKeyChecking=no -r app %SSH_USER%@%VM_IP%:/var/app/
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
