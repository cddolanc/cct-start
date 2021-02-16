import csv

data = open('example.csv', encoding="utf-8")

# print(data)   # gives error: <_io.TextIOWrapper name='example.csv' mode='r' encoding='UTF-8'>

csv_data = csv.reader(data)

data_lines = list(csv_data)

# print(data_lines[:3])

# for line in data_lines[:5]:
#     print(line)


# len(data_lines) #1001

# all_emails = []
# for line in data_lines[1:15]:
#     all_emails.append(line[3])

# print(all_emails)



# full_names = []

# for line in data_lines[1:15]:    # data_lines[1::]  list all lines except header
#     full_names.append(line[1]+' '+line[2])

# print(full_names)



# # newline controls how universal newlines works (it only applies to text mode). It can be None, '', '\n', '\r', and '\r\n'.
# file_to_output = open('to_save_file.csv','w',newline='')

# csv_writer = csv.writer(file_to_output,delimiter=',')

# csv_writer.writerow(['a','b','c']) #7

# csv_writer.writerows([['1','2','3'],['4','5','6']])

# file_to_output.close()




f = open('to_save_file.csv','a',newline='')

csv_writer = csv.writer(f)

csv_writer.writerow(['new','new','new']) #13

f.close()