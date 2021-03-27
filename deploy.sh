echo "Starting to deploy docker image.."

DOCKER_IMAGE=tjdntjr123/private_lesson:dev

docker pull $DOCKER_IMAGE
docker ps -q --filter ancestor=$DOCKER_IMAGE | xargs -r docker stop
docker run --rm --env-file ./.env.prod -p 8000:80 -d --name dev $DOCKER_IMAGE
