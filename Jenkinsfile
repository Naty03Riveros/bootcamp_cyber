pipeline {
    agent any
    environment {
        // Definir el nombre del servidor de SonarQube configurado en Jenkins
        SONARQUBE_SERVER = 'NPY'  // Asegúrate de que este nombre coincida con la configuración de Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                // Clona el código desde GitHub en la rama 'main'
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
                    // Ejecuta el análisis de SonarQube con la configuración de servidor 'NPY'
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
