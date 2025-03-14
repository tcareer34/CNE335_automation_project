# TIm Nguyen
# CNE 335 3-13-2025
# Automation Project

import os
from putty.keys import PPKKey
import paramiko

#class Server:
    # Code for Server Ping Assignment
    # def __init__(self, server_ip):
    #     # TODO -
    #     self.server_ip = server_ip
    #
    # def ping(self):
    #     # TODO - Use os module to ping the server
    #     result = os.system(f'ping -n 5 {self.server_ip}')
    #     return result

    # Code for Automated SSH Assignment

class Server:
    """ Server class for representation and manipulating servers. """

    def __init__(self, server_ip, rsa_key, upgrade, username):
        self.server_ip = server_ip
        self.rsa_key = rsa_key
        self.upgrade = upgrade
        self.username = username


    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 5 %s" % self.server_ip)
        #command = f'ping -c 5 {self.server_ip}' if os.name != 'nt' else f'ping -n 5 {self.server_ip}'
        #return os.system(command) == 0
        return result

    #def run_command(self, command):
    def upgrade(self):
        """Run upgrade command via SSH."""

        ssh = paramiko.SSHClient()

        my_key = paramiko.RSAKey.from_private_key_file(self.rsa_key)  # Fix key handling
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.server_ip, username=self.username, pkey=my_key)

        stdin, stdout, stderr = ssh.exec_command(self.command)
        for line in stdout.read().splitlines():
            print(line)

        #    output = stdout.read().decode().strip()
        #    error = stderr.read().decode().strip()

        ssh.close()  # Ensure proper cleanup / disconnect

        #    if error:
        #        return f"Error:\n{error}"
        #    return output

        #except paramiko.SSHException as e:
        #    return f"SSH error: {e}"