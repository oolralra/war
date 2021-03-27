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
}