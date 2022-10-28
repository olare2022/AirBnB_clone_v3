#!/usr/bin/env bash
<<<<<<< HEAD
#Sets up webservers for deployment: (Run script on both servers)
#If not done, does the following:
#       install Nginx; creats folders /data/, /data/web_static/,
#       /data/web_static/releases/, data/web_static/shared,
#       /data/web_static/releases/test
#       /data/web_static/releases/test/index.html (with some content)
#Create symbolic lnk /data/web_static/current to data/web_static/releases/test
#       delete and recreate symbolic link each time script's ran
#Recursively assign ownership of /data/ folder to user and group 'ubuntu'
#Update the Nginx config to server content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
#       restart Ngixn
# curl localhost/hbnb_static/index.html should return sample text"

ADD_WEBSTATIC=\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared
echo "Test index.html files to test Nginx config" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/release/test/ /data/web_static/current
sudo chown hR ubuntu:ubuntu /data/
sudo sed -i "35i $ADD_WEBSTATIC" /etc/nginx/sites_available/default
=======
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
sudo service nginx start
