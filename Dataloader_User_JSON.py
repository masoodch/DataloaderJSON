import csv

domain = input("Please enter the customer primary email domain: ")
root = input("Enter the Root Path: ")
newRoot = str(root.replace("\\", "\\\\"))


with open('famcs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print('{')
            print(f'\t"localRoot": "{newRoot}\\\\{row[0]}, {row[1]}",')
            print(f'\t"remoteRoot": "{row[0]}, {row[1]}",')
            print(f'\t"driveRoot": "Work ({row[1]} {row[0]})",')
            print('\t"targetUser":{"identity": "',row[2],'@',domain,'"}', sep='')
            print('},')
            line_count += 1
    print(f'Processed {line_count} lines.')




