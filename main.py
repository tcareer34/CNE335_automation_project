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
    server = Server('ubuntu@35.85.53.16', 'C:\Tim_key.pem')

    # TODO - Call Ping method and print the results
    command = 'sudo apt update && sudo apt upgrade -y'
    # Call Ping and print results
    if server.ping():
        print("Updating server...")
        # server.run_command(command)
        ssh_result = server.run_command(command)
