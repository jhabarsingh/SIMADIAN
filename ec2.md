## Deploy Django App On EC2 Instance 

[Blog](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/)

1. Create the EC2 instance

2. SSH into the insance

3. run these commands 
	```
	sudo apt-get update
	sudo apt-get upgrage -y
	# ask to update grub choose install the package maintainance version
	sudo apt-get install python3-venv
	python3 -m venv env	
	source env/bin/activate
	git clone <project-name>
	pip install -r requirements.txt
	
	pip install gunicorn
	sudo apt-get install -y nginx
	
		
	```
4. change inbound traffic rule for the instance 

5. Bind the wsgi application to the gunicorn
	```
	gunicorn --bind 0.0.0.0:8000 projectname.wsgi
	``` 

6. Install supervisor
