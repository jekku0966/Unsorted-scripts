import csv

with open('varasto_uusi.csv') as file:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        
        if line[0] == '0':
            
            if line[30] is not '126' or '122' or '125' or '605' or '121'\
               or '500' or '5' or '123' or '66' or '124' or '21' or '22' \
               or '34' or '37' or '0' or None or '':
                if line[37] is not '0' or '' or None:
                    try:
                        price = round(float(float(line[9].replace(',', '.'))/float(line[37]))*1.24, 3)
                        print(line[1], '{} €/{}'.format(str(price).replace('.', ','), line[5]))
                    except ValueError as e:
                        print(e)
                        pass

                else:
                        pass
            else:
                pass
            
        else:
            pass
            
