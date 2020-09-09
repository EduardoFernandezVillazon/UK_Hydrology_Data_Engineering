import os
import csv
import stat


def create_ssh_script():
    with open('instance_public_dns.csv', mode='r') as instance_dns_file:
        instance_reader_rows = csv.reader(instance_dns_file, delimiter=',', quotechar='"')
        for row in instance_reader_rows:
            with open('secure_shell_command.sh', 'w') as file:
                file.write('ssh -i ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/HydroEC2pair.pem ubuntu@{public_dns}'.format(public_dns=row[0]))
            os.chmod('~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/secure_shell_command.sh',
                     stat.S_IRWXU)
            break


def create_ssh_tunnel_script():
    with open('instance_public_dns.csv', mode='r') as instance_dns_file:
        instance_reader_rows = csv.reader(instance_dns_file, delimiter=',', quotechar='"')
        for row in instance_reader_rows:
            with open('secure_shell_command.sh', 'w') as file:
                # MODIFY FROM HERE TO END

                file.write('ssh -i ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/\
                        HydroEC2pair.pem ubuntu@{public_dns}'.format(public_dns=row[0]))
            os.chmod('~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/secure_shell_command.sh',
                     stat.S_IRWXU)
            break


create_ssh_script()

# command: ~/PycharmProjects/UK_Hydrology_Data_Engineering/venv/code_repository/secure_shell_command.sh
