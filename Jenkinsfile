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
                sh 'coverage run test.py'
                sh 'coverage report'
                
            }
        }
        stage('Build'){

            environment {
                DOCKER_CRED = credentials('DaweisGtihub')
                }
            
            when{
				expression{
					env.BRANCH_NAME == "develop"
				}
			}
            steps{
                echo 'Building'
                sh "docker build -t $DOCKER_CRED_USR/webpage:latest -f Dockerfile ."
                sh "docker push $DOCKER_CRED_USR/webpage:latest"
            }
        }
    }

}
