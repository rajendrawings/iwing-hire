sudo rm -rf /etc/nginx/sites-enabled/iwing-hire
sudo rm -rf /etc/nginx/sites-available/iwing-hire

sudo cp -rf /home/ubuntu/iwing-hire/nginx/nginx.conf /etc/nginx/sites-available/iwing-hire

sudo ln -s /etc/nginx/sites-available/iwing-hire /etc/nginx/sites-enabled

sudo systemctl restart nginx

sudo service nginx status