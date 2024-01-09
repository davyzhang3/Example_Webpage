pipeline {
    agent any

    environment {
        VIRTUALENV = 'venv'
    }
    
    stages {
        stage('preparing') {
            steps {
                echo 'preparing..'
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
            when {
                expression {
                    return env.BRANCH_NAME == 'develop' || 'main';
                }
            }
            steps {
                echo 'In ' + env.BRANCH_NAME + ' branch, testing..'
                script {
                    // Run your test command
                    sh '''
                        . ${VIRTUALENV}/bin/activate
                        python3 -m coverage run test.py
                        python3 -m coverage report
                    '''
                }
                
            }
        }
        stage('Build'){

            environment {
                DOCKER_CRED = credentials('Dawei-Dockerhub')
                }
            
            steps{
                echo 'Building'
                sh '''
                    . ${VIRTUALENV}/bin/activate
                    docker login --username ${DOCKER_CRED_USR} --password ${DOCKER_CRED_PSW}
                    docker build -t ${DOCKER_CRED_USR}/webpage:latest -f Dockerfile .
                    docker push ${DOCKER_CRED_USR}/webpage:latest
                '''
            }
        }
        stage('Deploy'){

            environment {
                STAGING_INSTANCE_IP = credentials('STAGING_INSTANCE_IP')
                PROD_INSTANCE_IP = credentials('PROD_INSTANCE_IP')
                DOCKER_CRED = credentials('Dawei-Dockerhub')
                }
            steps{
                script{
                    echo 'Deploying'
                    if (env.BRANCH_NAME == 'develop'){
                    sh '''
                        eval "$(ssh-agent -s)"
                        ssh-add ~/.ssh/id_rsa
                        ssh -o StrictHostKeyChecking=no ubuntu@$STAGING_INSTANCE_IP "docker ps -a --format '{{.Names}}' | grep -q my-container && docker stop my-container && docker rm my-container || true"
                        ssh -o StrictHostKeyChecking=no ubuntu@$STAGING_INSTANCE_IP "docker pull $DOCKER_CRED_USR/webpage:latest && docker run --name my-container -d -p 80:80 $DOCKER_CRED_USR/webpage:latest"
                        '''
                    }
                    else if (env.BRANCH_NAME == 'main'){
                    sh '''
                        eval "$(ssh-agent -s)"
                        ssh-add ~/.ssh/id_rsa
                        ssh -o StrictHostKeyChecking=no ubuntu@$PROD_INSTANCE_IP "docker ps -a --format '{{.Names}}' | grep -q my-container && docker stop my-container && docker rm my-container || true"
                        ssh -o StrictHostKeyChecking=no ubuntu@$PROD_INSTANCE_IP "docker pull $DOCKER_CRED_USR/webpage:latest && docker run --name my-container -d -p 80:80 $DOCKER_CRED_USR/webpage:latest"
                        '''
                    }
                }
            }
        }
    }

}
