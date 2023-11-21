pipeline {
    agent any // This will run on any available node

    stages {
        stage('Setup and Test') {
            steps {
                checkout scm // Checkout the code from the source control

                script {
                    // Set up Python 3.10 (assuming Python 3.10 is already installed on the node)
                    // You might need to adjust the command depending on how Python is installed on your nodes
                    sh "sudo apt-get update && sudo apt-get install -y python3.10"

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
