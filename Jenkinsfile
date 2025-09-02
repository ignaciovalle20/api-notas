pipeline {
  agent any
  stages {
    stage('Run Api Notas') {
      steps {
	sh '''
        	docker run -d -p 8000:8000 -v ${pwd}/data:/usr/src/app/data --rm --name api-notas-docker api-notas
      	  '''
	}
    }
  }
}

