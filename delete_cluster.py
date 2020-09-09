import boto3
import os
import csv


def delete_keypair():
    try:
        os.system('rm ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/HydroEC2pair.pem')
    except:
        pass
    try:
        ec2.delete_key_pair(KeyName='HydroEC2pair')
    except:
        pass

ec2 = boto3.client('ec2',
                   region_name="us-west-2",
                   )

with open('instance_ids.csv', mode='r') as instance_id_file:
    instance_reader_rows = csv.reader(instance_id_file, delimiter=',', quotechar='"')
    for row in instance_reader_rows:
        response = ec2.terminate_instances(InstanceIds=row)

os.system('rm ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/instance_ids.csv')
os.system('rm ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/instance_public_dns.csv')

delete_keypair()