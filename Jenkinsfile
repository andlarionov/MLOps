pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'echo "Setting up the environment..."'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                sh 'python create_dataset.py'
            }
        }
        stage('Train') {
            steps {
                sh 'echo "Training the model..."'
                sh 'python train_model.py'
            }
        }
        stage('Predict') {
            steps {
                sh 'echo "Making predictions..."'
                sh 'python make_prediction.py'
            }
        }
    }
    post {
        always {
            sh 'echo "Pipeline completed."'
        }
    }
}
