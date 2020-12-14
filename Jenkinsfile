def groovyfile
pipeline {
  agent any
  stages {
    stage ('Build'){
	  	steps{
			script{
				 def filename = 'jenkins.' + env.BRANCH_NAME + '.groovy'
				 groovyfile = load filename
			}
		}
	  }
    stage('Run app'){
      steps{
        script{
          groovyfile.run_app()
        }
      }
    }
    stage('StressTest'){
      steps{
        script{
          groovyfile.stress_test()
        }
      }
    }
      stage('Release branch'){
        steps{
		script{
          groovyfile.release()
		}
        }
      }
     stage('Remove image'){
      steps{
        script{
          groovyfile.remove()
        }
      }
	}
    }
}
