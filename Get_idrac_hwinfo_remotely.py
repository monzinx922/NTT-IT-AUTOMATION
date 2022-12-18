import subprocess

# The IP address or hostname of the remote server
server = '192.168.1.100'

# The username and password to use for SSH authentication
username = 'admin'
password = 'password'

# The racadm command to get the system information
racadm_cmd = 'racadm getsysinfo'

# The SSH command to run on the remote server
ssh_cmd = f'ssh {username}@{server} {racadm_cmd}'

# Run the SSH command and save the output
output = subprocess.run(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=password, encoding='ascii')

# Print the output
print(output.stdout)
