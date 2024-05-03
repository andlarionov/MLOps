pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'echo "Activation of virtual environment"'
                sh 'source /home/larionov/ml_project/venv_ml_project/bin/activate'
            }
        }
        stage('Setup_2') {
            steps {
                sh 'echo "Setting up the environment..."'
                sh 'pip install -r Lab_2/requirements.txt'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                sh '/home/larionov/ml_project/venv_ml_project/bin/python scripts/Lab_2/create_dataset.py'
            }
        }
        stage('Train') {
            steps {
                sh 'echo "Training the model..."'
                sh '/home/larionov/ml_project/venv_ml_project/bin/python Lab_2/train_model.py'
            }
        }
        stage('Predict') {
            steps {
                sh 'echo "Making predictions..."'
                sh '/home/larionov/ml_project/venv_ml_project/bin/python Lab_2/make_prediction.py'
            }
        }
    }
    post {
        always {
            sh 'echo "Pipeline completed."'
        }
    }
}
