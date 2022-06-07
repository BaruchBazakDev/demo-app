
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
                script {
                    if (branchName[0] == 'release') {
                        sh "mvn versions:set -DnewVersion=${env.NEW_TAG}"
                        echo "building application release version"
                    }
                    else{
                        echo "building application SNAPSHOT version from ${env.GIT_BRANCH}"
                    }
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
            echo "publish to ecr"
        }

    post {
    always {
        deleteDir()
        echo "Job done"
        }
    }
}