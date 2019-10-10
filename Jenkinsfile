pipeline {
  environment {
    registry = "blohmeier/capstone-test1"
    registryCredential = ‘dockerhub’
  }
  agent { docker { image 'python:3.7.4' } }
  stages {
    stage('Cloning Git from github repository') {
      steps {
        git 'https://github.com/blohmeier/devopsProjects-dockerWithNginx.git'
  }
}stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }   
    }
  }
}