pipeline {
    agent any
    environment {
        SONARQUBE_SERVER = 'NPY'  // Asegúrate de que este nombre coincida con la configuración en Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Clonando el repositorio...'
                // Clonamos el repositorio desde GitHub
                git branch: 'main', url: 'https://github.com/Naty03Riveros/bootcamp_cyber.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Compilando el proyecto...'
                // Aquí se compila el proyecto, si es necesario, o se ejecuta alguna acción como tests.
                bat 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    echo 'Iniciando el análisis de SonarQube...'
                    
                    // Con esta función, activamos el entorno de SonarQube configurado en Jenkins.
                    withSonarQubeEnv(SONARQUBE_SERVER) {
                        // Ejecutamos el análisis de SonarQube sin nohup
                        bat 'mvn sonar:sonar'  // No es necesario usar 'nohup'
                    }
                    
                    echo 'Análisis de SonarQube finalizado.'
                }
            }
        }
        stage('Wait for SonarQube Analysis') {
            steps {
                script {
                    // Este paso espera a que el análisis de SonarQube se complete
                    echo 'Esperando a que SonarQube complete el análisis...'
                    waitForQualityGate abortPipeline: true
                    echo 'Análisis completado.'
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo 'El análisis de SonarQube fue exitoso.'
        }
        failure {
            echo 'El análisis de SonarQube falló.'
        }
    }
}

