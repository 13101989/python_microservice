pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'git@github.com:13101989/python_microservice.git'

                // Install dependencies
                sh "python -m pip install --upgrade pip && pip install -r requirements.txt"

                //Analyzing the code with pylint
                sh "pylint app/"
                sh "mypy app/"
                sh "pytest ."
            }
        }
    }
}
