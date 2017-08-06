import csv
import re

'''
This script reads Visma Nova's Asiakastiedot csv file,
finds the companies names and contact person data. After locating
the said information goes through the list and skips where there are
no email address or fields with names pointing to billing and outputs the
data to a text file in the same folder where the script was run.
The script assumes the customer info csv file is in the same folder.
Before using this script, please convert all semicolons to commas.
Visma can't do proper csv files and many other things are bad...
'''

#line[2] Yritysnimi rivi 1
#line[3] Yritysnimi lisärivi

#line[2] Henkilön koko nimi
#line[12] sähköposti

with open('asiakaslista_uusi.csv') as file:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        m = re.search(r'(lasku)', line[3], re.I)
        n = re.search(r'(reskontra)', line[3], re.I)
        p = re.search(r'(reskontra)', line[12], re.I)
        o = re.search(r'(lasku)', line[12], re.I)
        q = re.search(r'(lasku)', line[2], re.I)
        r = re.search(r'(reskontra)', line[2], re.I)
        at = re.search(r'(@)', line[12], re.I)
        if line[0] == '0':
            if int(line[1]) >= 10000  and m is None and n is None:
                yritys = line[2] + ' ' + line[3]
            else:
                pass

        elif line[0] == '1':
            

            if at and p is None and o is None and q is None and m is None and n is None and r is None and line[12] is not False:
                email = line[12]
                name = line[2]
                try:
                    name = line[2].split()
                    first = name[0]
                    last = name[1]
                except:
                    pass
                
                with open('parsittu.txt', 'a') as output:
                    data = email + ', ' + first + ', ' + last + ',, ' + yritys
                    output.write(data + '\n')
            else:
                pass
