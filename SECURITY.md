# Security Policy



## RSA Key-Based Authentication

The project utilizes **RSA key-based authentication** for secure communication and command execution via SSH. Here are some key details:

- **Private Key Location**: Users must specify the location of their private RSA key file (e.g., `C:\path\to\your\key.pem`) in the code to establish secure SSH connections to the server.
  
- **Key Permissions**: The private RSA key file must have appropriate permissions (i.e., not publicly readable). It is crucial that this file remains private to ensure the security of the server communication.

- **Security of Keys**: 
  - We recommend users use a passphrase for their private keys for additional security.
  - If the RSA key is compromised, users should immediately revoke the compromised key and generate a new one.
  - **Do not distribute your private key to unauthorized individuals**. Sharing the private key with anyone who is not authorized can compromise the security of the system and may lead to unauthorized access.

- **SSH Authentication**: The RSA private key is used to authenticate the user (in this case, `ubuntu`) to the remote server. SSH keys provide a more secure alternative to password-based authentication, ensuring that only authorized users can access the server.

## Reporting a Vulnerability

If you discover a security vulnerability within the project, we encourage you to report it as soon as possible. Here’s how you can report a vulnerability:

1. **Where to Report**: 
   - Please send your security concerns to our dedicated security email at `tcareer@hotmail.com`. For immediate concerns, feel free to reach out through our project’s GitHub repository by opening a private issue.

2. **Update Frequency**:
   - You will receive an acknowledgment within 24 hours. We will provide an update on the investigation status within 3 business days after acknowledgment.
   - For more urgent issues, expect faster feedback within 1 business day.

3. **What to Expect**:
   - **Accepted Vulnerabilities**: If the vulnerability is verified and accepted, a patch will be created and deployed as soon as possible. The patch will be included in the next release cycle, or an emergency release will be made.
   - **Declined Vulnerabilities**: If we determine the issue is not a security concern, we will provide detailed reasoning. You may request a follow-up if you feel the issue needs further investigation.

4. **Responsible Disclosure**:
   - We ask that security issues are disclosed responsibly and privately, allowing us time to address the vulnerability before it is made public. Once the issue is patched, we will publicly announce the fix and acknowledge your contribution to improving the project’s security.
