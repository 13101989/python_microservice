pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-v /your/workspace:/workspace'
        }
    }

    stages {
        stage('Setup and Test') {
            steps {
                checkout scm // Checkout the code from the source control

                script {
                    // Install dependencies
                    sh """
                        python3 -m pip install --upgrade pip
                        python3 -m pip install -r requirements.txt
                    """

                    // Code Analysis and Tests
                    sh "python3 -m pylint \$(git ls-files '*.py')"
                    sh "python3 -m mypy \$(git ls-files '*.py')"
                    sh "python3 -m pytest ."
                }
            }
        }
    }
}
