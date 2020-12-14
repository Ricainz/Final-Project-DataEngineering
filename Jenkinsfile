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
    stage('Remove image'){
      steps{
        bat 'remove.bat'
      }
    }
  }
}
