
String addFix(String version, String fixNumber){
    return version+"."+fixNumber
}
String incrementBranch(String version){
    splitVersion = version.split("\\.")
    return splitVersion[0]+"."+splitVersion[1]+"."+splitVersion[2].next()
}
String branch_and_commit(String branch, String massage){
    return branch+" "+massage
}
String e2e = "e2e"

pipeline {
    agent any

    options {
        timestamps()
        timeout(time:10, unit:'MINUTES')
    }

    stages {
        stage('Prep') {
            steps {
                git branch: env.GIT_BRANCH, url: 'https://github.com/BaruchBazakDev/demo-app.git'
                script {
                    if (env.GIT_BRANCH == 'main') {
                        env.VERSION = sh (
                                    script: "git tag | tail -n 1 | cut -d '.' -f 1-2",
                                    returnStdout: true
                                    ).trim()
                        echo "${env.VERSION} version"
                        sh "git tag"
                        if (VERSION == "") {
                            env.VERSION = "1.0"
                            }
                        echo "${VERSION} version1"
                        TAG = sh (
                                    script: "git tag | tail -n 1 | grep ${VERSION} | cut -d '.' -f3",
                                    returnStdout: true
                                    ).trim()

                        env.NEW_TAG = (TAG == "") ? addFix(env.VERSION,"0") : addFix(env.VERSION,TAG.next())
                        echo "My new tag: ${env.NEW_TAG}"
                    }
                    commit = sh (
                        script: "git log -1 --oneline",
                        returnStdout: true,
                        ).trim()
                }
            }
        }

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
                sh 'docker build -t demo-app-baruch ./application'
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
                sh 'curl reverse-proxy/devops'
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
                sh '''aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin\
                    644435390668.dkr.ecr.eu-central-1.amazonaws.com
                    docker tag demo-app-baruch:latest 644435390668.dkr.ecr.eu-central-1.amazonaws.com/demo-app-baruch
                    docker push 644435390668.dkr.ecr.eu-central-1.amazonaws.com/demo-app-baruch'''
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