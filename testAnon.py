# Just following this instruction to see if I can read all IP addresses, write them
# https://docs.python.org/3/library/csv.html
# and following this to see how to has them
# https://www.pythoncentral.io/hashing-strings-with-python/#:~:text=A hash function is a,is a one way function.&text=The value returned by a,, hash value, or checksum.
import csv
with open('AWS_Honeypot_marx-geo.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
