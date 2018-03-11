#!/bin/bash
#make sure you are using user with sudo no password
#please create a file with your password like this "echo Your_password > secret"

if [ ! -f secret ]; then
   echo "Please create your secret first! (echo Your_password > secret)"
   exit 1
fi

pass=$(cat secret)

#create the repo & install extra repo
if [ ! -f /etc/yum.repos.d/centos.repo ]; then
    sudo sh -c 'echo -e "[centos]\nname=CentOS $releasever - $basearch\nbaseurl=http://mirror.centos.org/centos/7/os/\$basearch/\nenabled=1\ngpgcheck=1\ngpgkey=http://mirror.centos.org/centos/7/os/\$basearch/RPM-GPG-KEY-CentOS-7" > /etc/yum.repos.d/centos.repo'
    rpm -qa epel-release > x
     if [[ ! -s x ]]; then
        sudo wget https://archive.fedoraproject.org/pub/epel/7Server/x86_64/Packages/e/epel-release-7-11.noarch.rpm
        sudo rpm -ivh epel-release-7-11.noarch.rpm
     fi
     #install sshpass git ansible
     sudo yum install sshpass -y
fi

#prepare to connect to each server so that ansible can penetrate the remote server
#prepare the template script sshcopy
#if you are using password with sudo, use below instead and add the password,
awk -F',' 'FNR > 1 { print "sshpass -p 'password' ssh-copy-id -o StrictHostKeyChecking=no " $1 }' input.csv > sshcopy
# -v password='$pass'
#change it to executable
chmod u+x sshcopy
#run it
#./sshcopy
