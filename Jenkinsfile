pipeline {
    agent { docker { image 'jenkins-blueocean' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m pytest --alluredir=report -m "not not_reusable"'
            }
        }
    }
}
