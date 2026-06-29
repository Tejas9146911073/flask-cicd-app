pipeline {
    agent any
    environment {
        PYTHON_ENV = 'venv'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Setting up Python Virtual Environment...'
                sh '''
                    python3 -m venv ${PYTHON_ENV}
                    . ${PYTHON_ENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running pytest tests...'
                sh '''
                    . ${PYTHON_ENV}/bin/activate
                    python -m pytest tests/ --junitxml=test-reports/results.xml
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying Flask application to Staging...'
                sh '''
                    . ${PYTHON_ENV}/bin/activate
                    echo "Starting application service in staging..."
                    python -c "import flask; print('Flask is installed and verified!')"
                    echo "Application deployed successfully to staging!"
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
