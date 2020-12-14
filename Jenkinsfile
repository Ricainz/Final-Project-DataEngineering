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
    stage('Merging'){
      steps{
        script{
          groovyfile.user_acceptance()
        }
      }
    }
	  stage('Pushed'){
        steps{
		script{
          groovyfile.live()
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
