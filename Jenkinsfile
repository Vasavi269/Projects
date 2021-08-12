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

}
