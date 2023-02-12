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
            when {
                expression {
                    return env.BRANCH_NAME == 'dev' || 'main';
                }
            }
            steps {
                echo 'In ' + env.BRANCH_NAME + ' branch, testing..'
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
        stage('Deploy'){

            environment {
                SSHKEY = credentials('sshkey')
                STAGING_INSTANCE_IP = credentials('STAGING_INSTANCE_IP')
                PROD_INSTANCE_IP = credentials('PROD_INSTANCE_IP')
                DOCKER_CRED = credentials('Dawei-Dockerhub')
                }
            steps{
                echo 'Deploying'
                if (env.BRANCH_NAME == 'develop'){
                sh '''
                    eval "$(ssh-agent -s)"
                    echo "$SSHKEY" | ssh-add -
                    ssh -o StrictHostKeyChecking=no ec2-user@$STAGING_INSTANCE_IP "docker pull $DOCKER_CRED_USR/webpage:latest && docker stop my-container && docker rm my-container && docker run --name my-container -d $DOCKER_CRED_USR/webpage:latest"
                    '''
                }
                else if (env.BRANCH_NAME == 'main'){
                sh '''
                    eval "$(ssh-agent -s)"
                    echo "$SSHKEY" | ssh-add -
                    ssh -o StrictHostKeyChecking=no ec2-user@$STAGING_INSTANCE_IP "docker pull $DOCKER_CRED_USR/webpage:latest && docker stop my-container && docker rm my-container && docker run --name my-container -d $DOCKER_CRED_USR/webpage:latest"
                    '''
                }
    }

}
