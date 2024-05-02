pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'echo "Setting up the environment..."'
                sh 'pip install -r Lab_2/requirements.txt'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                sh 'python Lab_2/create_dataset.py'
            }
        }
        stage('Train') {
            steps {
                sh 'echo "Training the model..."'
                sh 'python Lab_2/train_model.py'
            }
        }
        stage('Predict') {
            steps {
                sh 'echo "Making predictions..."'
                sh 'python Lab_2/make_prediction.py'
            }
        }
    }
    post {
        always {
            sh 'echo "Pipeline completed."'
        }
    }
}
