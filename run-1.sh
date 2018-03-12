#create the repo & install extra repo
if [ ! -f /etc/yum.repos.d/centos.repo ]; then
    sudo sh -c 'echo -e "[centos]\nname=CentOS $releasever - $basearch\nbaseurl=http://mirror.centos.org/centos/7/os/\$basearch/\nenabled=1\ngpgcheck=1\ngpgkey=http://mirror.centos.org/centos/7/os/\$basearch/RPM-GPG-KEY-CentOS-7" > /etc/yum.repos.d/centos.repo'
    rpm -qa epel-release > x
     if [[ ! -s x ]]; then
        sudo wget https://archive.fedoraproject.org/pub/epel/7Server/x86_64/Packages/e/epel-release-7-11.noarch.rpm
        sudo rpm -ivh epel-release-7-11.noarch.rpm
        sudo yum install git ansible sshpass -y
     fi
fi
