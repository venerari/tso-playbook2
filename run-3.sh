 
#!/bin/bash

#create hosts
awk -F',' 'FNR > 1 { print  $1 }' input.csv > temp
#remove empty lines
awk NF temp > hosts

chmod u+x read-csv-create2.py
 
./read-csv-create2.py input.csv
cp server.yml roles/get-info-csv/vars/
ansible-playbook -i hosts get-info-csv.yml
