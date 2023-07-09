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
                sh 'export PYTHONPATH=$WORKSPACE:$PYTHONPATH'
                sh 'coverage run test.py'
                sh 'coverage report'
                
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
