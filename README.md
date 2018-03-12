
# tso-playbook

Run this first,

```
sudo curl https://raw.githubusercontent.com/venerari/tso-playbook/master/run-1.sh | /bin/bash
```

Install ldap if you need it,
```
sudo curl https://github.com/BeyondTrust/pbis-open/releases/download/8.5.7/pbis-open-8.5.7.385.linux.x86_64.rpm.sh | /bin/bash
```

Create the sshcopy script to run to all the client, make sure input.csv already exist.
```
sudo curl https://raw.githubusercontent.com/venerari/tso-playbook/master/run-2.sh | /bin/bash
```

Generate the data from remote hosts,
```
curl https://raw.githubusercontent.com/venerari/tso-playbook/master/run-3.sh | /bin/bash
```

