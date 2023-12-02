pipeline {
    agent any

    stages {
        stage('Clone Github repository') {
            steps {
                git branch: 'main', url: 'https://github.com/13101989/python_microservice.git'
                
                script {
                    sh """
                        whoami
                    """
                }
            }
        }
    }
}

