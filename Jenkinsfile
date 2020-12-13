pipeline {
  agent any
  stages {
    stage('Remove image'){
      steps{
        bat 'remove.bat'
      }
    }
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
