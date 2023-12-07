pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/chandrasehkhar/devops_home_test.git']]])
            }
        }
       // stage('Build') {
        //    steps {
        //        git branch: 'main', url: 'https://github.com/chandrasehkhar/devops_home_test.git'
         //       sh 'python3 app.py'
          //  }
       // }
        //stage('Test') {
        //    steps {
        //        sh 'python3 -m pytest'
        //    }
       // }
       // stage('Vulnerability Scan - Docker Trivy') {
       //     steps {
     
         //      sh "sudo bash trivy-image-scan.sh"
          //  }
        //}
        stage('Build docker iamge') {
            steps {

               sh 'docker build -t vadlakondasathya/first:latest .'
               }
        }
        stage('push docker iamge') {
            steps {
                withCredential([string(credentialId: 'docker-pwd', variable: 'dockerHubPwd')]){
                    sh "docker login -u vadlakondasathya -p ${dockerHubPwd}"
                }

                sh 'docker push vadlakondasathya/first:latest .'
               }
        }
       }
    }

