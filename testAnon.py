# Just following this instruction to see if I can read all IP addresses, write them
# https://docs.python.org/3/library/csv.html
# and following this to see how to has them
# https://www.pythoncentral.io/hashing-strings-with-python/#:~:text=A hash function is a,is a one way function.&text=The value returned by a,, hash value, or checksum.
import csv

fileName = 'AWS_Honeypot_marx-geo.csv'
testFileName = 'test.csv'
ips = []

with open(fileName, newline='') as inFile:
    with open(testFileName, 'w', newline='') as outFile:
        inReader = csv.DictReader(inFile)
        fieldNames = inReader.fieldnames

        outWriter = csv.DictWriter(outFile, fieldnames=fieldNames)
        outWriter.writeheader()

        for row in inReader:
            row['Ip-address'] = '**********'
            outWriter.writerow(row)

# in_file = open(fileName, "rb")
# reader = csv.reader(in_file)
# out_file = open(fileName, "wb")
# writer = csv.writer(out_file)
# print(reader[0])
# for row in reader:
#     print(row[7])
#     writer.writerow(row)
# in_file.close()
# out_file.close()

# def readFile(filename):
#     with open(fileName, newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         count = 0
#         for row in spamreader:
#             print(count, ', '.join(row), '\n')
#             count = count + 1
#             if (count == 10):
#                 break


# def writeFile(filename):
#     with open(filename, 'a', newline='') as csvfile:
#         spamwriter = csv.writer(csvfile, delimiter=' ',
#                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#         spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# readFile(fileName)
# writeFile('test.csv')
