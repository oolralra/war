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

     stage ('Deploy') {
        steps {
            sh 'scp deploy.sh ${REMOTE_USER}@${REMOTE_HOST}:~/'
            sh 'ssh ${REMOTE_USER}@${REMOTE_HOST} "chmod +x deploy.sh"'
            sh 'ssh ${REMOTE_USER}@${REMOTE_HOST} ./deploy.sh'
        }
    }
}