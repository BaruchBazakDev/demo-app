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
                    env.GIT_BRANCH ==~ /(main|feature.*|release.*)/
			        }
	            }
            steps {
                sh "docker build -t demo-app-baruch ."
                }
            }
        }

        stage('Test') {
            when {
                expression {
                    env.GIT_BRANCH ==~ /(main|release.*|feature.*)/
                }
                beforeOptions true
		    }
            steps {
                echo "test"
            }
        }

        stage('Publish') {
            steps {
                echo "publish to ecr"
            }
        }

    post {
    always {
        deleteDir()
        echo "Job done"
        }
    }
}