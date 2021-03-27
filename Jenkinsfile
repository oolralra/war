node {
    agent : any

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

    stage('SSH transfer') {
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: false, failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "dev",//Jenkins 시스템 정보에 사전 입력한 서버 ID
                        verbose: true,
                        transfers: [
                            sshTransfer(
                                sourceFiles: "", //전송할 파일
                                removePrefix: "", //파일에서 삭제할 경로가 있다면 작성
                                remoteDirectory: "", //배포할 위치
                                execCommand: "make port" //원격지에서 실행할 커맨드
                            )
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