#!/bin/bash
apt-get update -y
apt-get install -y nginx python3 python3-pip
systemctl enable nginx
systemctl start nginx
