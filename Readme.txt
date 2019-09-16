# Read me

To build a docker image:

Step 1: Create a docker file with file name "Dockerfile" and save it in the project root directory

Step 2: Run the following command to build the docker image with tag the name as "polestar-app".
        docker build . -t polestar-app:latest

Run the Docker image:

Step 1: Make sure that required port 8000 is free and not listening or used by any other application

Step 2: Run the fowowing command to run the container
        docker run -it -d -p 8000:8000 polestar-app

Post Deployment Steps:

Open Browser and run the following URL's

1. localhost:8000
2. localhost:8000/index
3. localhost:8000/api/ships

Hosted Application Access:

Access the hosted application by launching the following URL, Note: it was hosted on my AWS freetire account with limited resources.
http://13.127.9.228:8000/

http://13.127.9.228:8000/api/ships/

http://13.127.9.228:8000/api/positions/9632179
