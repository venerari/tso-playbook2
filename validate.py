#!/usr/bin/python

# this will be based in individual fact files, e.g., sdcgigdcapmdw01_output.csv
import csv
import os.path
import time
import sys
#import argparse

def _init_vars_input():
    host_input = ""
    ipaddress_input = ""
    cpucore_input = ""
    ram_input = ""
    disk_input = ""
    fact_file = ""
    msg = ""

def _init_vars_fact():
    host_fact = ""
    ipaddress_fact = ""
    cpucore_fact = ""
    ram_fact = ""
    disk_fact = ""
    msg = ""

if __name__ == '__main__':
    try:
        #_declare_vars()
        global host_input
        global fact_file
        global ipaddress_input
        global cpucore_input
        global ram_input
        global disk_input
        global host_fact
        global ipaddress_fact
        global cpucore_fact
        global ram_fact
        global disk_fact
        global msg

        with open('input.csv') as csvfile_input:
            reader_input = csv.DictReader(csvfile_input)
            output_dict = dict()
            output_list = []
            for row_input in reader_input:
                #print(row_input['Hostname'], row_input['RemoteTestPort'])
                #_init_vars_input()
                host_input = ""
                ipaddress_input = ""
                cpucore_input = ""
                ram_input = ""
                disk_input = ""
                fact_file = ""
                msg = ""

                host_input = row_input['Hostname']
                if host_input:
                    fact_file = host_input + '_output.csv'
                    msg = ""
                    if os.path.isfile(fact_file):
                        ipaddress_input = row_input['IPAddress']
                        cpucore_input = row_input['CPUCore']
                        ram_input = row_input['RAM']
                        disk_input = row_input['Disk']

                        with open(fact_file) as csvfile_fact:
                            fact_row_ctr = 1
                            reader_factfile = csv.DictReader(csvfile_fact)
                            row_fact = None
                            for row_fact in reader_factfile:
                                #_init_vars_fact()
                                host_fact = ""
                                checkhost_fact = ""
                                port_fact = ""
                                ipaddress_fact = ""
                                cpucore_fact = ""
                                ram_fact = ""
                                disk_fact = ""
                                msg = ""

                                host_fact = row_fact['Hostname']
                                checkhost_fact = row_fact['Check-Host']
                                port_fact = row_fact['Port']
                                ipaddress_fact = row_fact['IPAddress']
                                cpucore_fact = row_fact['CPUCore']
                                ram_fact = row_fact['RAM']
                                disk_fact = row_fact['Disk']
                                if fact_row_ctr == 1:
                                    if (host_input != host_fact):
                                        msg = "Host from input does not match value from fact file. Host input = " + host_input + ". Host fact = " + host_fact
                                    if (ipaddress_input != ipaddress_fact):
                                        msg += "| IP address from input does not match value from fact file."
                                    if (cpucore_input != cpucore_fact):
                                        msg += "| No. of CPU cores from input does not match  value from fact file."
                                    if (ram_input != ram_fact):
                                        msg += "|RAM from input does not match value from fact file."
                                    if (disk_input != disk_fact):
                                        msg += "| Disk size from input does not match value from fact file."
                                    if not msg:
                                        msg = "Passed"
                                else:
                                    #_init_vars_input()
                                    host_input = ""
                                    ipaddress_input = ""
                                    cpucore_input = ""
                                    ram_input = ""
                                    disk_input = ""
                                    fact_file = ""
                                    msg = ""

                                output_dict = {'Hostname input': host_input, 'Hostname output': host_fact, 'Check-host': checkhost_fact, 'Port': port_fact, 'IP input': ipaddress_input, 'IP fact': ipaddress_fact, 'CPU core input': cpucore_input, 'CPU core fact': cpucore_fact, 'RAM input': ram_input, 'RAM fact': ram_fact, 'Disk input': disk_input, 'Disk fact': disk_fact, 'Message': msg}
                                output_list.append(output_dict)
                                fact_row_ctr += 1
                    else:
                        msg += "Fact file " + fact_file + " not found."
                        output_dict = {'Hostname input': host_input, 'Hostname output': "", 'Check-host': "", 'Port': "", 'IP input': "", 'IP fact': "", 'CPU core input': "", 'CPU core fact': "", 'RAM input': "", 'RAM fact': "", 'Disk input': "", 'Disk fact': "", 'Message': msg}
                        output_list.append(output_dict)
        ###print (time.strftime("%d/%m/%Y"))
        #output_file = "validation_" + time.strftime("%d%m%Y-%H%M") + ".csv"
        output_file = "output.csv"
        with open(output_file, 'w') as csvfile_output:      
            fieldnames = ['Hostname input', 'Hostname output', 'Check-host', 'Port', 'IP input', 'IP fact', 'CPU core input', 'CPU core fact', 'RAM input', 'RAM fact', 'Disk input', 'Disk fact', 'Message']
            writer_output = csv.DictWriter(csvfile_output, fieldnames=fieldnames)
            writer_output.writeheader()
            writer_output.writerows(output_list)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
