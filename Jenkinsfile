pipeline {
  agent any
  stages {
    stage('Remove image'){
      steps{
        echo 'remove.bat'
      }
    }
    stage('Building'){
      steps{
        echo 'build.bat'
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
