## Script used for building docker images and running container
Docker_image_name=data-pipeline-scripts
image_tag=latest
Docker_container_name=data-pipeline-container


docker stop $Docker_container_name
docker rm $Docker_container_name

docker build -t $Docker_image_name:$image_tag .
docker run -id  --env-file ../.env --name $Docker_container_name $Docker_image_name:$image_tag

docker exec -it $Docker_container_name bash