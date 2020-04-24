# CyberHead
## Modular Open Source Trading


<p align="center">
    <img src="https://cyberhead.uk/assets/strategies.png" />
</p>


## Run it locally
1. [Install Docker](https://docs.docker.com/install/)
2. Clone the project: `git clone https://github.com/TheCyberHead/CyberHead`
3. Go into the cloned project's docker folder: `cd CyberHead/docker`
4. Run the Docker container: `sudo docker-compose up -d`
5. Launch CyberHead: `sudo docker-compose exec cyberhead python core.py`


You can go into the container with: `sudo docker-compose exec cyberhead bash`

Any change into the cloned repository is sync with the container files in `/home/cyberhead/CyberHead`
