pipeline {
    agent any

    stages {
        stage('preparing') {
            steps {
                echo 'preparing..'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing....'
                sh 'which python3'
                sh 'which pip'
                sh 'echo $WORKSPACE'
                sh 'echo $PYTHONPATH'
                
            }
        }
        stage('Build'){

            environment {
                DOCKER_CRED = credentials('Dawei-Dockerhub')
                }
            
            steps{
                echo 'Building'
                sh "docker login --username $DOCKER_CRED_USR --password $DOCKER_CRED_PSW"
                sh "docker build -t $DOCKER_CRED_USR/webpage:latest -f Dockerfile ."
                sh "docker push $DOCKER_CRED_USR/webpage:latest"
            }
        }
    }

}
