def groovyfile
pipeline {
  agent any
  stages {
    stage ('Groovy'){
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
    stage('Remove image'){
      steps{
        script{
          groovyfile.remove()
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
    }
}
