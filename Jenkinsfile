
pipeline { 
    agent any
    environment {
        // Nombre del servidor de SonarQube configurado en Jenkins
        SONARQUBE_SERVER = 'NYP'
    }
    stages {
        stage('Checkout') {
            steps {
                // Clona el código desde GitHub
                git branch: 'main', url: 'https://github.com/Naty03Riveros/bootcamp_cyber.git'
            }
        }
        stage('Build') {
            steps {
               
                sh 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Ejecuta el análisis de SonarQube
                    withSonarQubeEnv(SONARQUBE_SERVER) {  
                        // Comando Maven para análisis de SonarQube con parámetros adicionales
                        sh '''
                        mvn sonar:sonar \
                          -Dsonar.projectKey=bootcamp_cyber \
                          -Dsonar.host.url=$SONAR_HOST_URL \
                          -Dsonar.login=$SONAR_AUTH_TOKEN
                        '''
                    }
                }
            }
        }
      
    }
    post {
        // Acciones después de la ejecución del pipeline
        always {
            echo 'Pipeline finished!'
        }
    }
}
