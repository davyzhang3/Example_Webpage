pipeline {
    agent any

    environment {
        VIRTUALENV = 'venv'
        DOCKER_CRED = credentials('Dawei-Dockerhub')
    }

    stages {
        stage('preparing') {
            steps {
                echo 'Preparing..'
                sh "whoami"
                script {
                    // Create and activate a virtual environment
                    sh '''
                        python3 -m venv ${VIRTUALENV}
                        . ${VIRTUALENV}/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Testing....'
                script {
                    // Run your test command
                    sh "python3 -m coverage run test.py"
                    sh "python3 -m coverage report"
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building'
                // Log in to Docker
                sh "docker login --username ${DOCKER_CRED_USR} --password ${DOCKER_CRED_PSW}"
                // Build and push Docker image
                sh "docker build -t ${DOCKER_CRED_USR}/webpage:latest -f Dockerfile ."
                sh "docker push ${DOCKER_CRED_USR}/webpage:latest"
            }
        }
    }
}
