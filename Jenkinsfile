pipeline {
    agent any 

    environment {
        VENV_PATH = "venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/pratikkadam551/python-selenium-automation.git'
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
