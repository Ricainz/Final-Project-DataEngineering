pipeline {
  agent any
  stages {
    stage('Building'){
      steps{
        bat 'build.bat'
      }
    }
    stage('Running'){
      steps{
        bat 'run.bat'
      }
    }
    stage('Test'){
      steps{
        bat 'test.bat'
      }
    }
  }
}
