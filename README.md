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
Deleted the local SQLite DB.
Made new admin user and made new post on the app. Everything works together with RDS as the new DB.
Now I want to make the app scalable and resilient.
First I've made AMI from my running App instance,
used this AMI for the LaunchTemplate,
Created an ASG and used my existing ALB, to balance between 3 AZ's, from my blackjack flask app that's hosted already.
Now I use r53 to have the app hosted on MartinsCloud.be instead of the public IP of the EC2.
Reused existing ALB from the Blackjack EB environment.
Attached ACM certificate to ALB for HTTPS.
ALB listener configured on port 443 (HTTPS).
redirected port 80 HTTP traffic to port 443 HTTPS.

I also wanted to load my existing blackjack project with the same loadbalancer to direct traffic but it was hosted with elastic beanstalk in the default vpc. I needed to make a new elastic beanstalk deployment in my newly created vpc 
where my MartinsCloud homepage EC2 adn RDS is hosted. With this beanstalk deployment I've created an ALB, used the existing certificates from my previous working app to work together for my homepage and existing blackajck app in this ALB.

ALso in Route 53 I needed to change the A records martinscloud.be and www.martinscloud.be to point at the new ALB.

In the ALB i made a rule that traffic that contains /blackjack* will be redirected to my blackjack app TargetGroup.
a second default rule I've made is to direct all other traffic to my MartinsCloud homepage EC2 TargetGroup.

Everything is working so now I safely delete the elastic beanstalk deployment that I've made in the default vpc.

