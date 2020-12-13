pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        sh 'docker-compose build'
      }
    }
    stage('Run docker images'){
          steps{
            sh 'docker-compose up'
          }
}
}
}
