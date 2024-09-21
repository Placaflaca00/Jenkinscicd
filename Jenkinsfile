pipeline {
    agent { label 'Ubuntu-Agent' }

    environment {
        PATH = "$PATH:/usr/bin"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout SSH') {
            steps {
                sshagent(['github-ssh-key']) {
                    sh 'git clone git@github.com:Placaflaca00/Jenkinscicd.git .'
                }
            }
        }

        stage('Checkout with Credentials') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'GITHUB_USERNAME', passwordVariable: 'GITHUB_TOKEN')]) {
                    sh 'git clone https://$GITHUB_USERNAME:$GITHUB_TOKEN@github.com/Placaflaca00/Jenkinscicd.git .'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Construyendo...'
                sh 'whoami'
                sh 'pwd'
            }
        }

        stage('Testing') {
            steps {
                sh '''
                    python -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    pytest --maxfail=1 --disable-warnings
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sshagent(['gcp-ssh-key']) {
                    sh '''
                        rsync -Pavz -e "ssh -o StrictHostKeyChecking=no" frontend/ moha251mmed@34.68.41.66:/var/frontend/
                        rsync -Pavz -e "ssh -o StrictHostKeyChecking=no" api/ moha251mmed@34.68.41.66:/var/api/
                    '''
                }
            }
        }

        stage('Check PATH') {
            steps {
                sh 'echo $PATH'
            }
        }
    }
}
