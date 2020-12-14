def run_app(){
  bat 'run.bat'
}
  
def stress_test(){
  echo 'stress test running'
}

def remove(){
  bat 'remove.bat'
}

def release(){
  echo 'Push to release branch'
}

return this
