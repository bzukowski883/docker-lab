# Please refer to this file if you are having trouble with README.md

# The Lab

for https -> needs a valid cert authrority configured in docker + nginx
#in cml do docker exec -it alpine sh if you don't want to use the gui

Try without the | as its not in the apk pipeline
apk upgrade
apk update
apk add curl

Curling the backend? well currently this docker project has a python backend 
which inside nginx you can see the port for proxy_pass http://backend:8000/;
so try to curl that

# pygame support
What does it mean to run pygame? well there is a few ways to do it, the first is to build the file
for one create a container called pygame and run the dockerfile in ./pygame like so
docker build -t pygame ./pygame
docker run -it --name pygame pygame

# ping pygame
if you try to run ping pygame in the alpine container and nothing comes up chances are they are made on seperate IPs simply run the next set of commands to check

This command shows your networks on the computer currently running
docker network ls

See what network the containers are running on
docker inspect pygame --format '{{json .NetworkSettings.Networks}}'
docker inspect alpine --format '{{json .NetworkSettings.Networks}}'

then you can connect the containers to the same network IE whatever alpine is currently connected to (docker_demo_demo_net) probably somthing like this
docker network connect docker_demo_demo_net pygame

then run exec into the alpine shell ^command at top^ and ping pygame, at this point you should be able to see it



# Offical EOF #









# Creating a https cert for encryption across lan/wan 
First create the certs folder inside webserver IE /certs normally
mkdir -p webserver/certs

openssl needs to be installed
run a openssl certficate generation command
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout webserver/certs/server.key \
  -out webserver/certs/server.crt \
  -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost"

To clarify this line   -addext "subjectAltName=DNS:localhost"  isnt strictly nessesary but your modern browsers will have some trust issues without it

inside the ./webserver/nginx.conf we would have to add sll_certificates like so
server {
    listen 80 ssl;
    server_name localhost;

    ssl_certificate /etc/nginx/certs/server.crt;
    ssl_certificate_key /etc/nginx/certs/server.key;
    
    ...
}

however if you want to still have http access probably use a different port

