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
                bat 'terraform init -backend-config="bucket=my-terraform-state-bucket" -backend-config="prefix=terraform/state"'
            }
        }
        stage('Terraform Apply') {
            steps {
                bat 'terraform apply --auto-approve'
            }
        }
        stage('Synchronize Frontend') {
            steps {
                sshagent(['jenkins-ssh-key']) {
                    bat '''
                    rsync -Pavz -e "ssh -o StrictHostKeyChecking=no" frontend/ jenkins@<VM_IP>:/var/frontend/
                    '''
                }
            }
        }
        stage('Synchronize API') {
            steps {
                sshagent(['jenkins-ssh-key']) {
                    bat '''
                    rsync -Pavz -e "ssh -o StrictHostKeyChecking=no" api/ jenkins@<VM_IP>:/var/api/
                    '''
                }
            }
        }
    }
}
