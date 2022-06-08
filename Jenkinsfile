pipeline {
    agent any

    options {
        timestamps()
        timeout(time:10, unit:'MINUTES')
    }

    stages {

        stage('Checkout') {
            steps {
                deleteDir()
                echo 'Pulling... ' + env.GIT_BRANCH
                checkout scm
                echo "commit hash : ${env.GIT_COMMIT}, tag_name: ${env.TAG_NAME}, author: ${env.GIT_AUTHOR_NAME}"
                }
        }

        stage('Build') {
            when {
		        expression {
                    env.GIT_BRANCH ==~ /(main|feature.*)/
			        }
	            }
            steps {
                sh 'docker build -t demo-app-baruch .'
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            when {
		        expression {
                    env.GIT_BRANCH ==~ /(main|feature.*)/
			        }
	            }
            steps {
                sh 'sleep 5'
                sh 'docker build -t test-app ./tests'
                sh 'docker run -it --network jenkins test_app'
                sh 'curl demo-app:5000/'
            }
        }

        stage('Publish') {
            when {
		        expression {
                    env.GIT_BRANCH ==~ /(main)/
			        }
	            }
            steps {
                echo 'Publish image to ECR'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
            sh 'docker-compose down'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}