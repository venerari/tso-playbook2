#!/bin/bash
#make sure you are using user with sudo no password
#please create a file with your password like this "echo Your_password > secret"

#generate ssh
if [ ! -f ~/.ssh/id_rsa ]; then
	ssh-keygen -q -f ~/.ssh/id_rsa -N ""
fi

if [ ! -f secret ]; then
   echo "Please create your secret first! (e.g. echo Your_password > secret)"
   exit 1
fi

pass=$(cat secret)

#install sshpass
sudo yum install sshpass -y

#prepare to connect to each server so that ansible can penetrate the remote server
#prepare the template script sshcopy
#if you are using password with sudo, use below instead and add the password,
#awk -F',' 'FNR > 1 { print "sshpass -p 'password' ssh-copy-id -o StrictHostKeyChecking=no " $1 }' input.csv > sshcopy
#grab first column and ignore first row
awk -F',' 'FNR > 1 { print  $1 }' input.csv > sshcopy
#remove empty lines
awk NF sshcopy > hosts
#generate the sshpass
awk -v password="$pass" '{print "sshpass -p " password " ssh-copy-id -o StrictHostKeyChecking=no " $1}' hosts > sshcopy
# -v password='$pass'

#change it to executable
chmod u+x sshcopy
#run it
./sshcopy
