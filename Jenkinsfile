pipeline {
    agent any

    tools {
        allure 'Allure' // Ensure this matches the configured name in Global Tool Configuration
    }

    environment {
        VENV_PATH = "venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/pratikkadam551/python-selenium-automation.git'
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                sh '''
                    . $VENV_PATH/bin/activate
                    pytest
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**/*.*', allowEmptyArchive: true
        }
    }
}
