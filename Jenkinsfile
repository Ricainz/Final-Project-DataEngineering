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
    stage('Unit tests'){
      steps{
        script{
          groovyfile.unittest()
        }
      }
    }
    stage('Validation'){
      steps{
        script{
          groovyfile.test_done()
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
