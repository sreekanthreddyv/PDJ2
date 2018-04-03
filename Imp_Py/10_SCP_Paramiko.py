from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

ssh_client = SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(AutoAddPolicy())
ssh_client.connect(hostname='192.168.2.231',
                   username="systebui", password="votarytech")

scp = SCPClient(ssh_client.get_transport())

scp.put('test.txt', 'test2.txt')
scp.get('test2.txt')

scp.put('test.txt', recursive=True, remote_path = '/home/systebui/Music')
scp.close()

