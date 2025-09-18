created a yaml file for cloudformation. i've created a stack with physical resources like vpc, 3 private subnets, 6 public subnets, routetables, igw.
created ec2 in public subnet a
installed : sudo yum update -y sudo yum install -y git python3-pip adn connected to the github repo
Cloned project from GitHub
Created a virtual environment
Installed project requirements
Flask app is running in development mode on my EC2
Installed a production server (Gunicorn)
Installed Nginx
Now, instead of http://<EC2-PUBLIC-IP>:5001/, my Flask app is accessible at: http://<EC2-PUBLIC-IP>/
Next I made Flask run in the background with Gunicorn + systemd, so it doesn’t stop when I close the terminal.
created rds free tier instance
made subnetgroup for rds
made sg to allow mysql from port 3306 from my ec2 sg
IAM database authentication instead of static username/password
Changed main.py to use RDS instead of SQLite

