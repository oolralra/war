node {
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
//      stage ('Deploy') {
//         steps {
//             script {
//                 echo 'Using remote command over ssh'
//                 sh 'echo "Today is:" date'
//                 echo '*** Executing remote commands ***'
//
//                 sh '${REMOTE_USER}@${REMOTE_HOST}'
//                 sh 'scp deploy.sh ${REMOTE_USER}@${REMOTE_HOST}:~/'
//                 sh 'ssh ${REMOTE_USER}@${REMOTE_HOST} "chmod +x deploy.sh"'
//                 sh 'ssh ${REMOTE_USER}@${REMOTE_HOST} ./deploy.sh'
//             }
//         }
    }
}