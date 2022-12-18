import subprocess

# The racadm command to get the system information
racadm_cmd = 'racadm getsysinfo'

# Run the racadm command and save the output
output = subprocess.run(racadm_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the output
print(output.stdout.decode())
