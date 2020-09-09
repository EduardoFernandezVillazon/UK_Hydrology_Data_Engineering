import configparser
import boto3
import json
import time
import os
import csv


def create_keypair():
    with open('HydroEC2pair.pem', 'w') as outfile:
        key_pair = ec2.create_key_pair(KeyName='HydroEC2pair')
        outkey = key_pair['KeyMaterial']
        outfile.write(outkey)

    os.system('chmod 400 ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/HydroEC2pair.pem')


def delete_keypair():
    try:
        os.system('rm ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/HydroEC2pair.pem')
    except:
        pass
    try:
        ec2.delete_key_pair(KeyName='HydroEC2pair')
    except:
        pass


def save_instance_ids():
    instance_ids = []
    for instance in response['Instances']:
        instance_ids.append(instance['InstanceId'])

    with open('instance_ids.csv', mode='a') as instance_id_file:
        instance_writer = csv.writer(instance_id_file, delimiter=',', quotechar='"')
        instance_writer.writerow(instance_ids)
    return instance_ids


ec2 = boto3.client('ec2',
                   region_name="us-west-2",
                   )
# config = configparser.ConfigParser()
# config.read_file(open('project_config.ini'))

delete_keypair()
create_keypair()

response = ec2.run_instances(
    ImageId='ami-0ba60995c1589da9d', #ami-0a07be880014c7b8e
    InstanceType='t2.micro',
    KeyName='HydroEC2pair',
    MaxCount=1,
    MinCount=1,
    UserData=open("launch_script.sh", "r").read()
)

InstanceIds = save_instance_ids()

waiter = ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=InstanceIds)

response = ec2.describe_instances(InstanceIds=InstanceIds)

InstancePublicDNS_Name = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        InstancePublicDNS_Name.append(instance['PublicDnsName'])

with open('instance_public_dns.csv', mode='a') as instance_dns_file:
    instance_writer = csv.writer(instance_dns_file, delimiter=',', quotechar='"')
    instance_writer.writerow(InstancePublicDNS_Name)
