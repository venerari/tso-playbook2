#!/bin/bash

#create the repo
if ! [ -f /etc/yum.repos.d/centos.repo ]; then
  sh -c 'echo -e "[centos]\nname=CentOS $releasever - $basearch\nbaseurl=http://mirror.centos.org/centos/7/os/\$basearch/\nenabled=1\ngpgcheck=1\ngpgkey=http://mirror.centos.org/centos/7/os/\$basearch/RPM-GPG-KEY-CentOS-7" > /etc/yum.repos.d/centos.repo'
fi
#download epel-release 7-11, this link might get broken from time to time, find another one that wil work
wget -nc https://archive.fedoraproject.org/pub/epel/7Server/x86_64/Packages/e/epel-release-7-11.noarch.rpm
#install it
rpm -ivh epel-release-7-11.noarch.rpm

#install sshpass git ansible

yum install sshpass git ansible -y

#prepare to connect to each server so that ansible can penetrate the remote server
#prepare the template script sshcopy
#make sure you are either using root or user with sudo no password
awk -F',' 'FNR > 1 { print "sshpass ssh-copy-id -o StrictHostKeyChecking=no " $1 }' server.csv > sshcopy
#if you are using password with sudo, use below instead and add the password,
#awk -F',' 'FNR > 1 { print "sshpass -p 'you-password' ssh-copy-id -o StrictHostKeyChecking=no " $1 }' server.csv > sshcopy
#change it to executable
chmod u+x sshcopy
#run it
#./sshcopy

awk -F',' 'FNR > 1 { print $1 }' server.csv > inventory

ansible-playbook -i inventory get-info-csv.yml
