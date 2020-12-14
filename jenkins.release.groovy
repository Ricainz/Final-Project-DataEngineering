def run_app(){
  bat 'run.bat'
}
  
def stress_test(){
}

def user_acceptance(){
  input 'Confirm push to main?' 
}
def remove(){
  bat 'remove.bat'
}

def release(){
}

def live(){
  echo 'pushed to main'
}

return this
