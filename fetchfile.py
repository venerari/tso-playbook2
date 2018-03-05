#! /usr/bin/python
import os
import paramiko
import scp
import sys
import string
import re
#os.system("/usr/bin/scp"+" user1@10.193.176.6:"+"/etc/hosts "+"/var/tmp/temp1/.")
server_name="server1"
def get_file_from_server(host_ip1,server_name_1):
#global server_name
  ssh1=paramiko.SSHClient()
  ssh1.load_system_host_keys()
  ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh1.connect(host_ip1,username='sftp_user')
  print ("test")
  #sys.exit(0)
  with scp.SCPClient(ssh1.get_transport()) as scp1:
   #scp.put('test.txt', 'test2.txt')
   server_name_1.strip()
   server_name_1 = server_name_1.translate(string.maketrans('', ''), '?!')
   new_file_name='/tmp/'+server_name_1+'_info.csv'
   new_file_name = new_file_name.translate(string.maketrans('', ''), '?!')
   new_file_name = re.sub('[?$]', '', new_file_name)
   scp1.get('/tmp/info.csv',new_file_name)
  scp1.close()
def get_servername():
  global server_name
  with open('./hosts.list') as f:
    for line in f:
       print line 
       line=line.rstrip('\n')
       host_ip=line.split(" ")[0]
       server_name1=line.split(" ")[1]
       server_name1.rstrip()
       print host_ip
       print server_name1
       #sys.exit(0)
       get_file_from_server(host_ip,server_name1)
  f.close()
  #return host_ip
#####################################################

get_servername()
sys.exit(0)
#ssh1=paramiko.SSHClient()
#ssh1.load_system_host_keys()
#ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("testing")
