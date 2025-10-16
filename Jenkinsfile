pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python3"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Advay-S/ci-cd-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment step: (optional cloud deploy here)'
            }
        }
    }

    post {
        success {
            echo '✅ Build, test, and deployment successful!'
        }
        failure {
            echo '❌ Build or tests failed. Check logs in Jenkins console output.'
        }
    }
}
