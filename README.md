# CyberHead
## Modular Open Source Trading

![CyberHead](https://im4.ezgif.com/tmp/ezgif-4-74683d231dc5.gif)
![DataSets CyberHead](https://im4.ezgif.com/tmp/ezgif-4-98aeaf8cdbe3.gif)


## Run it locally
1. [Install Docker](https://docs.docker.com/install/)
2. Clone the project: `git clone https://github.com/TheCyberHead/CyberHead`
3. Go into the cloned project's docker folder: `cd CyberHead/docker`
4. Run the Docker container: `sudo docker-compose up -d`
5. Launch CyberHead: `sudo docker-compose exec cyberhead python core.py`

You can go into the container with: `sudo docker-compose exec cyberhead bash`
Any change into the cloned repository is sync with the container files in `/app/`

### Install without Docker

- Go to `/CyberHead/cyberhead` and run `pip install -r requirements.txt`
- Install MySQL and define the environment variables required to stabilish the connection, you can just add them in your .bashrc local file :
```
export CH_DB_NAME="database_name"
export CH_DB_HOST="database_host"
export CH_DB_USER="database_user"
export CH_DB_PASSWORD="database_password"
```
- Install Node.js & yarn
- Install Nginx
- Go to `/CyberHead/cyberhead/web` and run `yarn install && yarn build`, this step will create a `build` folder, in the default Nginx configuration define the root path to the `build` folder. The nginx configuration file will look like the following one :
```
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name cyberhed.uk;

	location / {
		try_files $uri /index.html;
	}
}
```
- It's important to define the `location` section, without this you will be getting random 404 errors.
- If you wish to add an SSL certificate there's an easy way to to so with [Let's Encrypt](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)
- Install [RabbitMQ](https://www.rabbitmq.com/install-debian.html)
- Once you've finished the prior setup, go to the root folder and execute `python main.py` and then run the Celery configuration `celery -A tasker worker --loglevel=info`


### Structure

CyberHead was built with a modular mindset, to provide you a platform that gives you the ability to use what you need and trash away what you don't, the CyberHead' core is very simple, a centralized queue manager where most of the CPU intensive tasks takes place and a Flask service which serves the API for the frontend.

If you'd like to start building services and integrate them into CyberHead you can just go and create a folder inside `modules` and start coding by following the other's module structure.

### Financial Data

Our main source of data is Yahoo but this is not a limitation at all, CyberHead strategy functionality was built to be source-agnostic, once you start collecting data and pushing it into the local DB it will just works with any source you prefer.

### Databases

The vas majority of the platform runs on MySQL, but, everything is wrapped using an ORM, so, if you'd like to switch to Postgres, it's an easy task.

### Frontend

The UI is currently using React.js, this gives us the ability to develop data intensive visualizations and very reactive interfaces.

### Queues
We're using RabbitMQ as our queue broker, this was implemented using Celery.

### Contact
If you want to get in touch, drop us a line at info@cyberhead.uk


### MIT License

2020 CyberHead

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
