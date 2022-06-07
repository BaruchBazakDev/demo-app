
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
                git branch: env.GIT_BRANCH, url: 'git@gitlab_web:Baruch_developer/analytics.git'
                script {
                    branchName = env.GIT_BRANCH.split('/')
                    if (branchName[0] == 'feature' || branchName[0] == 'release') {
                        env.VERSION = branchName[1]
                        echo "${env.VERSION}"
                        sh "git tag"
                        TAG = sh (
                                    script: "git tag | tail -n 1 | grep ${env.VERSION} | cut -d '.' -f3",
                                    returnStdout: true
                                    ).trim()

                        env.NEW_TAG = (TAG == "") ? addFix(branchName[1],"0") : addFix(branchName[1],TAG.next())
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

        stage('Publish') {

        }

    post {
    always {
        deleteDir()
        echo "Job done"
        }
    }
}