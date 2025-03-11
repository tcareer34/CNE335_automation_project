# Tim Nguyen
# CNE 335 3-10-2025
# Automation Ping Final Project
from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Tim Nguyen")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()

    # TODO - Create a Server object
    server_ip = "34.219.149.76"
    # Key path location
    rsa_key = r"C:\Tim_key.pem"
    username = "ubuntu"

# run application update and upgrade commands
    upgrade_command = "sudo apt-get update && sudo apt-get upgrade -y"
    my_server = Server(server_ip, rsa_key, username)

# TODO - Call Ping method and print results
if my_server.ping():
    print(f"Server {server_ip} is reachable.")
    print('Updating...')
    ssh_result = my_server.run_command(upgrade_command)
    print("Upgrade output: \n", ssh_result)

else:
    print(f"Server {server_ip} is unreachable, please check the server's public IPv4 address.")


