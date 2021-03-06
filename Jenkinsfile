
String addFix(String version, String fixNumber){
    return version+"."+fixNumber
}
String incrementBranch(String version){
    splitVersion = version.split("\\.")
    return splitVersion[0]+"."+splitVersion[1]+"."+splitVersion[2].next()
}
String incrementVersion(String major, String minor, String fixNumber){
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
                git branch: env.GIT_BRANCH, credentialsId: 'demo-app', url: 'git@github.com:BaruchBazakDev/demo-app.git'
                script {
                    if (env.GIT_BRANCH == 'main') {
                        env.VERSION = sh(returnStdout: true, script: "git tag --sort version:refname | tail -1").trim()
                        echo "${VERSION}"
                        echo "${env.VERSION} - with env"
                        env.TAG_NEW = incrementBranch(env.VERSION)
                        echo "${TAG_NEW} -> new tag"
                    }
                    commit = sh (
                        script: "git log -1 --oneline",
                        returnStdout: true,
                        ).trim()
                }
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
                    docker tag demo-app-baruch:latest 644435390668.dkr.ecr.eu-central-1.amazonaws.com/demo-app-baruch:${TAG_NEW}
                    docker push 644435390668.dkr.ecr.eu-central-1.amazonaws.com/demo-app-baruch:${TAG_NEW}'''
            }
        }

        stage("Tag") {
            when {
		        expression {
                    env.GIT_BRANCH ==~ /(main)/
			        }
	            }
            steps {
                sh '''git tag ${TAG_NEW}
                    git push --tags'''
            }
        }
    }
    post {
        always {
            echo 'This will always run'
            sh 'docker-compose down'
            deleteDir()
        }
        success {
            echo '${TAG_NEW} version uploaded.'
            echo 'send mail - update to ${TAG_NEW} '
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
