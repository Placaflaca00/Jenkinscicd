pipeline {
    agent any
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-service-accountw')
        TF_VAR_project_id = 'tecnologai-emergente'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Placaflaca00/Jenkinscicd.git', branch: 'main'
            }
        }
        stage('Terraform Init') {
            steps {
                bat 'terraform init -backend-config="bucket=my-terraform-state-bucketw" -backend-config="prefix=terraform/state" -input=false -reconfigure -force-copy'
            }
        }
        stage('Terraform Apply') {
            steps {
                bat 'terraform apply --auto-approve'
            }
        }
        stage('Synchronize Frontend') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-ssh-key', keyFileVariable: 'SSH_KEY_FILE', usernameVariable: 'SSH_USER')]) {
                    bat """
                    rsync -Pavz -e "ssh -i %SSH_KEY_FILE% -o StrictHostKeyChecking=no" frontend/ %SSH_USER%@34.67.33.86:/var/frontend/
                    """
                }
            }
        }
        stage('Synchronize API') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-ssh-key', keyFileVariable: 'SSH_KEY_FILE', usernameVariable: 'SSH_USER')]) {
                    bat """
                    rsync -Pavz -e "ssh -i %SSH_KEY_FILE% -o StrictHostKeyChecking=no" api/ %SSH_USER%@34.67.33.86:/var/api/
                    """
                }
            }
        }
    }
}
