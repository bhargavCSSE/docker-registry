### Local Docker Registry Deployment guide

By defualt, security features and auth are disabled while setting up local docker registry. <br>
By default, the registry runs on localhost:5000

Prerequisites: <br>

    1.  docker and docker-compose - To run the registry
    
    2.  htpasswd - To generate authentication for users to access the local registry
    Note: You don't need htpasswd if you want to setup an insecure registry without auth.

Steps to setup without auth: <br>

    1.  Clone the repo by executing,
        git clone https://github.com/bhargavCSSE/docker-registry.git
    
    2.  Run command:
        docker compose up

How to setup with auth: <br>
    
    1.  After cloning the repository, open docker-compose.yaml and uncomment line 11-13

    2.  Navigate to "a2auth" directory in the cloned repo.
    
    3.  Run following command and replace "yourusername" with your desired username:
        htpasswd -Bc registry.password yourusername
    
    4.  Enter the desired password. Re-enter the password. This step completes adding a user to the registry.
    
    5.  Run the command: 
        docker compose up

######## <br>

**If the registry is setup without certs and auth, then execute following steps to make your docker allow pulling/pushing from the local remote registry.**

Note: This configuration is done on client side of docker installation, which is trying to access the registry.

    1.  In the cloned repo, navigate to docker-config directory and open the file "daemon.json" in any text editor.

    2.  Copy the json content within {}

    3.  Go to your docker's daemon.json file and add the copied content.
        Docker's daemon.json file location:
        Windows: 
            %userprofile%\.docker\daemon.json
        Linux/Debian: 
            /etc/docker/daemon.json

    4.  In the copied content, replace "registry-address" with your local registry address. It should look something like below,
        "insecure-registries":["1.1.1.1:5000"] or
        "insecure-registries":["yourdomain.com"]
    
    5.  Test connection with the registry using curl by executing,
        curl -X GET http://registry-address/v2/_catalog

    6.  (optional) Test out your registry with provided test image

######## <br>

How to use/test the registry using provided test image
(Recommend running this test on a remote node that is connected to the node running the registry)

To push the image,

    1.  In the cloned repo, navigate to test-img directory.

    2.  To build the image, run following command,
        docker build -t heartbeat-img:latest -t heatbeat-img:v1 .

    3.  Tag the image with registry address using,
        docker tag heartbeat:latest registry-address/heartbeat:latest
    
    4. (optional) if auth is enabled then run following command to login,
        docker login registry-address

    5.  Then run the command,
        docker push registry-address/heartbeat:latest

To pull the image

    1.  Run command,
        docker pull registry-address/heartbeat:latest

To execute the image

    1. docker run -it registry-address/heartbeat:latest

    2. Press ctrl + c or cmd + c to exit out of it
