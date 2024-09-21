pipeline {
    agent { label 'Ubuntu-Agent' }
    stages {
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
                        rsync -Pavz -e "ssh -o StrictHostKeyChecking=no" frontend/ usuario@ip_de_tu_vm:/var/frontend/
                        rsync -Pavz -e "ssh -o StrictHostKeyChecking=no" api/ usuario@ip_de_tu_vm:/var/api/
                    '''
                }
            }
        }
    }
}
