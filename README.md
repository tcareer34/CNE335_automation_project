# AWS EC2 Instance Auto-Ping

## Author
**Tim Nguyen**

## Project: CNE 335 Automation Project

### AWS EC2 Instance Location
[EC2 Instance Details](https://us-west-2.console.aws.amazon.com/ec2/home?region=us-west-2#InstanceDetails:instanceId=i-0c9334bf2f9e62a1e)

---

## 📌 Overview
This project automates the following tasks:
- **Server Ping**: Checks if a server is reachable by sending ICMP echo requests.
- **Automated SSH Command Execution**: Uses SSH to remotely execute system update and upgrade commands.

---

## 🚀 Features
- **Ping a Server**: Utilizes the `os` module to send a ping request to a specified server IP.
- **SSH Automation**: Uses `paramiko` to securely connect to a remote server and execute commands.
- **Error Handling**: Manages SSH connection errors and command execution errors gracefully.

---

## 📋 Prerequisites
- Python 3.x
- Required Python modules:
  - `os`
  - `paramiko`
- Please download the tim_cne335.pem file shared in this repository and place it in your c:\ drive for SSH authentication 
- A server with SSH access

---

## ⚙️ Installation
1. Clone the repository or copy the script to your local environment.
2. Install required dependencies:
```bash
pip install paramiko
```

---

## 🛠️ Usage

### 1. Initialize and Run the Server Automation Script
```python
from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Tim Nguyen")

if __name__ == '__main__':
    print_program_info()

    server_ip = "34.219.149.76"
    rsa_key = r"C:\\tim_cne335.pem"
    username = "ubuntu"

    upgrade_command = "sudo apt-get update && sudo apt-get upgrade -y"
    my_server = Server(server_ip, rsa_key, username)

    if my_server.ping():
        print(f"Server {server_ip} is reachable.")
        print('Updating...')
        ssh_result = my_server.run_command(upgrade_command)
        print("Upgrade output: \n", ssh_result)
    else:
        print(f"Server {server_ip} is unreachable, please check the server's public IPv4 address.")
```

---

## 📝 Notes
- Ensure the private key file has the correct permissions (`chmod 600` on Unix systems).
- The ping command varies by operating system:
  - **Windows**: `ping -n 5`
  - **Unix/Linux**: `ping -c 5`

---

