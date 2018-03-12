 
#!/bin/bash
 
 chmod u+x read-csv-create2.py
 
 ./read-csv-create2.py input.csv
 
 ansible-playbook -i hosts get-info-csv.yml
