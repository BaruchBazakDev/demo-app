pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t demo-app-baruch .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker-compose up -d'
                sh 'curl demo-app:5000'
            }
        }

        stage('Publish') {
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