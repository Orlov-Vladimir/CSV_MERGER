import csv

file = open("C:\\csv\\csv_1.csv", "r")
list_1 = list(csv.reader(file, delimiter=","))
file.close()

file = open("C:\\csv\\csv_2.csv", "r")
list_2 = list(csv.reader(file, delimiter=","))
file.close()

file = open("C:\\csv\\csv_3.csv", "r")
list_3 = list(csv.reader(file, delimiter=","))
file.close()

list_res = []
i = 0

while i < 10:
    for first_string in list_1[0]:
        list_res.append(first_string)
        del list_1[0]

    for first_string in list_2[0]:
        list_res.append(first_string)
        del list_2[0]

    for first_string in list_3[0]:
        list_res.append(first_string)
        del list_3[0]
    i += 1

with open('C:\\csv\\merged.csv', 'w', newline='') as res_file:
    in_csv_writer = csv.writer(res_file, delimiter=' ')
    in_csv_writer.writerows(list_res)

print(list_res)
