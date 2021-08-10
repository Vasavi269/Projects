pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub_cred_vasavi')
	}

	stages {

		stage('Build') {

			steps {
				     sh 'sudo docker build -t helloworld:latest .'
			}
		}
		
		stage('Run'){
		
			steps {
				     sh 'sudo docker run -p 5000:5000 helloworld:latest'
			}
		}

		stage('Login') {

			steps {
				     sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				     sh 'sudo docker push helloworld:latest'
			}
		}
	}

	post {
		always {
			      sh 'sudo docker logout'
		}
	}

}
