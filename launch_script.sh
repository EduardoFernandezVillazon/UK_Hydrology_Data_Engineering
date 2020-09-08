#!/bin/bash

echo "TESTING YUM UPDATE"
apt  update -y
echo "TESTING PYTHON INSTALLATION"
apt install python3 python3-pip -y
pip3 install Pygments
# pip install --upgrade pip
echo "TESTING PANDAS INSTALLATION"
pip3 install pandas
echo "TESTING APACHE INSTALLATION"
pip3 install  apache-airflow==1.10.12  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.12/constraints-3.7.txt"