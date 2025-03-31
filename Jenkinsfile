pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        VENV_PATH = "venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/pratikkadam551/python-selenium-automation.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_PATH
                    . $VENV_PATH/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    . $VENV_PATH/bin/activate
                    $VENV_PATH/bin/python -m pytest -s
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', fingerprint: true
        }
        failure {
            echo 'Tests failed! Check logs.'
        }
    }
}
