pipeline {
  agent any
  stages {
    stage('Building'){
      steps{
        sh 'docker-compose build'
      }
    }
    stage('Running'){
      steps{
        sh 'docker-compose up'
      }
    }
  }
}
