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
    stage('Live !'){
      steps{
        bat 'live.bat'
      }
    }
    stage('Remove image'){
      steps{
        bat 'remove.bat'
      }
    }
  }
}
