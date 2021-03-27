node {
    agent none

    stages {
        stage('Clone repository') {
            checkout scm
        }

        stage('Build image') {
            /* This builds the actual image; synonymous to
            * docker build on the command line */
            app = docker.build("tjdntjr123/private_lesson")
        }

        stage('Test image') {
            app.inside {
                sh 'echo "Tests passed"'
            }
        }

        stage('Push image') {
            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
                app.push("dev")
            }
        }

        stage('SSH docker run') {
            steps([$class: 'BapSshPromotionPublisherPlugin']) {
                sshPublisher(
                    continueOnError: false, failOnError: true,
                    publishers: [
                        sshPublisherDesc(
                            configName: "dev",
                            verbose: true,
                            transfers: [
                                sshTransfer(execCommand: "make port")
                            ]
                        )
                    ]
                )
            }
        }
    }
}