pipeline{
    agent any
        // kubernetes {
        //   yamlFile "jenkins-pod.yaml"
        // }
    stages{
        stage('build'){
            parallel
            steps{
                echo 'hello'
            }

        }
        stage('Test'){
            steps{
                echo 'test'
            }
        }
        stage('clean'){
            steps{
                echo 'clean'
            }
        }
    }
}