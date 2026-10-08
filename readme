# SNHU Containerization Seminar Lab
## Intro 

This is a docker lab designed to introduce you to the concepts of docker. You will investigate some of the docker commands, docker-compose, and key concepts to the functioning of docker like networking.

If you're reading this durring the presentation, I appreciate the go getter attitude, but what I am talking about will be important to UNDERSTANDING this lab. Obviously you can complete it without me up there, but you will learn more if you listen first, then act.

## What the heck is a container

A container is just another process like any other based on an image. The only difference is that the system uses permissions called namespaces. These systems are simmilar to what users see as privilages. They are used to to block both view and interaction of the container with anything outside the tiny domain assigned to it on your computer (if your using windows than the vm).

The system then tells the container it is the root user and has all permissions, and as such, it functions pretty much like a virtual machine. Except, in reality, it is just another process on your machine. You can access what it is doing from the host, but it can't do anything outside of its assigned area.

## Whats an image?
The image is just the bluepring the process is made from. If you think of your google chrome program as the image, and your google chrome process as the container, you have the right idea. We just have to define the containers very explicitly, as normally you get programs that are download and use. Here we build them a little.

## Networking? but this is a process?

Yes, this is a process. Each of the processes believe they are the entire machine by themselves, we give each process the opportunity to have an ip and port. Docker uses the range 172.17.0.0/16 for its ips. These ips are designated to be local only by IANA(Internet Assigned Numbers Authority), so they can't be accidentally mistaken for WAN ips. Then each process also gets the opportunity to have ports like your machine does. 

Then docker hosts a virtual router and DNS, where each ip is tied to the containers name. This allows us to do something like ping "my_container" instead of ping 172.17.13.163

When developing these networks we also get control over which containers are a part of which network and what kind of networks they are. There are 6 differnt network drivers (types of networks).

For this lab though, we only touch on user defined bridge.

# Command List

The commands here are broken up into docker and docker compose. Docker compose is the tool you use to run your file that gives information on multiple docker containers at once. While docker is the tool used to just run a single container.

anything that looks like `this` is text where you input what you want in the command. Its pretty self explanitory when you read the commands and their descriptions.

These are all the commands you will need to properly explore this lab the way it is intended. This does not mean that these are the only commands, and that I have discussed all flags regarding these commands. An example is docker run and network connect. Here I have not shown you how to launch a container already connected because for demonstrative purposes, it is better to show both before and after connection.

## Docker

### docker ps | grep `text`
docker ps is a command that retrieves all actively running containers, it is extremely useful when working with docker and its one of those ones to remember.

The | grep text portion is optional, but it allows you to filter based on whether the line contains the phrase youre looking for. 99% of the time when you do this you are looking for the image, as the container's names are garbage most of the time.

### docker run --name `name` `image`

this runs a pre existing container based on an image. The name flag is optional, but if you want to do anything else with the container afterwards then you will want it, as if you dont set the name you will need to do a docker ps to get the string of characters. If you use name, you can just type the name you used again.

### docker run -it `image`

can be combined with the command above (just put -it before --name) and it will open the interactive terminal for the launched container. This is important as for a container like pygame we need to be able to interact with the container. If we do not include -it it will crash uneligently.

### docker exec -it `container` `command`

this command allows your to create an interactive terminal (-it) inside of a container. Without the it, it just prints the output of the command. if you are attempting to create an interactive termnial, your command should be "sh" or "bash".

### docker network ls

this is the command that just retrieves all your networks, like the one above, but you should never really have enough where you need to grep it.

### docker network connect `network` `container`

this command attaches an already existing container to a network. 

## Docker Compose

### docker-compose up --build

this command launches the containers and builds them if the docker file attached to them sees a difference. you should really always use build, as when you don't need it, it wont hurt. However, if you forget about it, it can be a pain in the neck.

### docker-compose down

this simply closes the containers that are tied to the compose file. this does not delete any data stored in any kind of mount.

### docker-compose down -v

this command does the same as docker compose down, except it does delete data inside of volume mounts. this is useful when you need to full reset your environment becuase something corrupted your db for example.

# Our Images

in this lab we have a total of 5 containers, and each of them has a different purpose. Here I will describe their purpose.

## webserver

This is a very basic front end. It is a Nginx server that give out a static page when someone connects to it via http. the page it gives has a fetch that attempts to grab data from the backend. 

Due to the fact that your browser is actually not inside the container though, we can't fetch from http://backend like we could if we did a curl from inside the container. Thus, we set it to fetch from /api/users, and we have a tiny reverse proxy line (location in nginx.conf) that forwards you to the backend.

## backend

This is a tiny python backend that when it recieves :8000/users it gets data from the database and returns it. Super simple.

## database

The database is a basic Postgres database that houses 3 pieces of information to be passed to the front end at the behest of the backend. Postgres is just a different type of SQL like mySQL.

## pygame

This is a small python interactive script. Game is definetly generous, but it had to have a memorable name. This container is here to show that a container can do almost anything, despite its limitiations. When running this container you must run it with docker run -it as it has choice() in it.

## alpine

This is our utility container. This is where we will be execing into so we can ping the other containers to display docker functionalities.

Some portions of the lab will require you to investigate the source code to find port numbers or other relevent information. The first item I gave you the port, as it is not explicitly stated in the code.

# The Lab

This lab will use all of the information above, and will require a lot of back and forth. This lab is rather loose as I will not tell you what to use and where, as you have all the resources you need above you. If you are completing this durring the lab portion of the meeting, then feel free to ask questions.

1. launch the containers inside docker compose.
2. connect to the webserver using your browser at url https://localhost:8080
3. click the button and notice the update.
4. enter an interactive terminal in alpine and use the following commands to add curl to the container:
    apk upgrade |
    apk update |
    apk get curl
5. curl the backend's get api from inside the alpine container (remember we are inside the container so we have the DNS) and notice the output
6. now put the same url inside your host machine's browser.

This is important as it shows that because only the front end is exposed to teh host's port, the only way to our data is via our front end. we cannot attempt to bypass it. This dramatically increases security in a system.

Furthermore, we have shown that we can get 3 containers to all interact with eachother, and even form a chain of information passing.

7. we are going to run the command to launch pygame now.
8. you can play through once, but once you are done leave the game open on the choice menu
9. now open a NEW terminal and go back to inside the alpine terminal and ping the pygame container.
10. now use the command to add the pygame to the existing docker network (found in the compose file)
11. go back to your alpine container and attempt to ping it again.
12. finish the game

Here we have shown that containers can host interactive terminals. This is important as it shows that almost anything you want a program to do a container can do. Now having a gui is difficult, as it is a container and can't mess with your host's "domain". However, we can use forwarding technologies to just forward the gui output to your screen. With termnials you can see that any text based thing you want can be launched in a container.

# Post-lab

Good job finishing the lab. While I showed you everything I thought was important in sucha  small time there is still so much more for you to be able to learn. I emplore you to go back through and make modifications and figure out how to make the docker work your own.

Containerization is an extremely important tool, and is applicable to any and every project you do in school. there are some things containers aren't good at like guis, but not everything needs to be in a container. you can just containerize your db, and leave everything else normal. Thats what is so awesome about containers, is that you can mix and match them to be used where they give an advantage and not used where they don't.