sudo rm -rf /etc/nginx/sites-enabled/iwinghire
sudo rm -rf /etc/nginx/sites-available/iwinghire

sudo cp -rf /home/ubuntu/iwinghire/nginx/nginx.conf /etc/nginx/sites-available/iwinghire

sudo ln -s /etc/nginx/sites-available/iwinghire /etc/nginx/sites-enabled

sudo systemctl restart nginx

sudo service nginx status