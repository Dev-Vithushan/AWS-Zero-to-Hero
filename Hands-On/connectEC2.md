# Connecting to an EC2 Instance Using Terminal (SSH) 💻..☁️

These steps assume you have an EC2 instance running on AWS and you have the following:

`Your Key Pair (.pem file):` You downloaded this when you created your EC2 instance. Keep it safe!

`Terminal or Command Prompt:` You'll use this to connect.
EC2 Instance's Public IP Address or DNS: Find this in the EC2 console.

## Steps

1. Locate Your Key Pair (.pem file):

    - Find the .pem file you downloaded when you created your EC2 instance.
Set Permissions (Important for Security):

2. macOS/Linux: Open your terminal and run

    ``` sh
    chmod 400 /path/to/your/keypair.pem 
    ```
    `Replace:` 
    /path/to/your/keypair.pem with the actual path

3. Connect Using SSH:

    - Linux/MacOS

    ``` sh
    ssh -i /path/to/your/keypair.pem ec2-user@your-instance-public-ip-or-dns
    ```

    `Replace:`
- /path/to/your/keypair.pem (or C:\path\to\your\keypair.pem) with the actual path to your key pair file.
- ec2-user with the correct username for your AMI (Amazon Machine Image). Common usernames include ubuntu, centos, admin, etc. Check your AMI documentation if unsure.

- your-instance-public-ip-or-dns with your instance's public IP address or DNS name.
    