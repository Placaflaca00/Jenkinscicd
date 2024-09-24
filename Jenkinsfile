pipeline {
    agent any
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-service-accountw')
        TF_VAR_project_id = 'tecnologai-emergente'
    }
    stage('Terraform Init') {
    steps {
        bat 'terraform init -backend-config="bucket=my-terraform-state-bucketw" -backend-config="prefix=terraform/state"'
            }
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Placaflaca00/Jenkinscicd.git', branch: 'main'
            }
        }
        stage('Terraform Init') {
            steps {
                bat 'terraform init'
            }
        }
        stage('Terraform Apply') {
            steps {
                bat 'terraform apply --auto-approve'
            }
        }
    }
}
