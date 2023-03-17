#!/bin/sh   
sudo apt update
sudo apt upgrade
cd /var
sudo mkdir app
chmod 777 -R /var/app
git clone https://github.com/TakadahHQ/Website.git
