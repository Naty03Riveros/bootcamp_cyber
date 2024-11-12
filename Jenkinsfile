pipeline {
    agent any
    environment {
        // Definir el nombre del servidor de SonarQube configurado en Jenkins
        SONARQUBE_SERVER = 'SonarQube'  // Este es el nombre configurado en Jenkins
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
                // Aquí agregas el comando para compilar el proyecto. Por ejemplo, si usas Maven:
                sh 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Ejecuta el análisis de SonarQube
                    withSonarQubeEnv(SONARQUBE_SERVER) {  
                        // Si estás usando Maven para el análisis de SonarQube
                        sh 'mvn sonar:sonar'
                    }
                }
            }
        }
        // Puedes agregar más etapas si lo deseas, como pruebas, despliegue, etc.
    }
    post {
        // Aquí puedes agregar acciones a realizar después de la ejecución del pipeline, como notificaciones
        always {
            echo 'Pipeline finished!'
        }
    }
}
