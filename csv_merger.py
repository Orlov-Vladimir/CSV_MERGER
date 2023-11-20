import csv

with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
    res_file.write('subscriberID' + '\n')
    res_file.close()

file = open("C:\\csv\\csv_1.csv", "r")
list_1 = list(csv.reader(file, delimiter=","))
file.close()
print("list_1 is done")

file = open("C:\\csv\\csv_2.csv", "r")
list_2 = list(csv.reader(file, delimiter=","))
file.close()
print("list_2 is done")

file = open("C:\\csv\\csv_3.csv", "r")
list_3 = list(csv.reader(file, delimiter=","))
file.close()
print("list_3 is done")

file = open("C:\\csv\\csv_4.csv", "r")
list_4 = list(csv.reader(file, delimiter=","))
file.close()
print("list_4 is done")

file = open("C:\\csv\\csv_5.csv", "r")
list_5 = list(csv.reader(file, delimiter=","))
file.close()
print("list_5 is done")

file = open("C:\\csv\\csv_6.csv", "r")
list_6 = list(csv.reader(file, delimiter=","))
file.close()
print("list_6 is done")

file = open("C:\\csv\\csv_7.csv", "r")
list_7 = list(csv.reader(file, delimiter=","))
file.close()
print("list_7 is done")

file = open("C:\\csv\\csv_8.csv", "r")
list_8 = list(csv.reader(file, delimiter=","))
file.close()
print("list_8 is done")

file = open("C:\\csv\\csv_9.csv", "r")
list_9 = list(csv.reader(file, delimiter=","))
file.close()
print("list_9 is done")

file = open("C:\\csv\\csv_10.csv", "r")
list_10 = list(csv.reader(file, delimiter=","))
file.close()
print("list_10 is done")

file = open("C:\\csv\\csv_11.csv", "r")
list_11 = list(csv.reader(file, delimiter=","))
file.close()
print("list_11 is done")

file = open("C:\\csv\\csv_12.csv", "r")
list_12 = list(csv.reader(file, delimiter=","))
file.close()
print("list_12 is done")

file = open("C:\\csv\\csv_13.csv", "r")
list_13 = list(csv.reader(file, delimiter=","))
file.close()
print("list_13 is done")

file = open("C:\\csv\\csv_14.csv", "r")
list_14 = list(csv.reader(file, delimiter=","))
file.close()
print("list_14 is done")

file = open("C:\\csv\\csv_15.csv", "r")
list_15 = list(csv.reader(file, delimiter=","))
file.close()
print("list_15 is done")

file = open("C:\\csv\\csv_16.csv", "r")
list_16 = list(csv.reader(file, delimiter=","))
file.close()
print("list_16 is done")

file = open("C:\\csv\\csv_17.csv", "r")
list_17 = list(csv.reader(file, delimiter=","))
file.close()
print("list_17 is done")

file = open("C:\\csv\\csv_18.csv", "r")
list_18 = list(csv.reader(file, delimiter=","))
file.close()
print("list_18 is done")

file = open("C:\\csv\\csv_19.csv", "r")
list_19 = list(csv.reader(file, delimiter=","))
file.close()
print("list_19 is done")

file = open("C:\\csv\\csv_20.csv", "r")
list_20 = list(csv.reader(file, delimiter=","))
file.close()
print("list_20 is done")

file = open("C:\\csv\\csv_21.csv", "r")
list_21 = list(csv.reader(file, delimiter=","))
file.close()
print("list_21 is done")

file = open("C:\\csv\\csv_22.csv", "r")
list_22 = list(csv.reader(file, delimiter=","))
file.close()
print("list_22 is done")

file = open("C:\\csv\\csv_23.csv", "r")
list_23 = list(csv.reader(file, delimiter=","))
file.close()
print("list_23 is done")

file = open("C:\\csv\\csv_24.csv", "r")
list_24 = list(csv.reader(file, delimiter=","))
file.close()
print("list_24 is done")

file = open("C:\\csv\\csv_25.csv", "r")
list_25 = list(csv.reader(file, delimiter=","))
file.close()
print("list_25 is done")

file = open("C:\\csv\\csv_26.csv", "r")
list_26 = list(csv.reader(file, delimiter=","))
file.close()
print("list_26 is done")

file = open("C:\\csv\\csv_27.csv", "r")
list_27 = list(csv.reader(file, delimiter=","))
file.close()
print("list_27 is done")

file = open("C:\\csv\\csv_28.csv", "r")
list_28 = list(csv.reader(file, delimiter=","))
file.close()
print("list_28 is done")

file = open("C:\\csv\\csv_29.csv", "r")
list_29 = list(csv.reader(file, delimiter=","))
file.close()
print("list_29 is done")

file = open("C:\\csv\\csv_30.csv", "r")
list_30 = list(csv.reader(file, delimiter=","))
file.close()
print("list_30 is done")

i = 0
m = min(len(list_1), len(list_2), len(list_3), len(list_4), len(list_5), len(list_6), len(list_7), len(list_8),
        len(list_9), len(list_10), len(list_11), len(list_12), len(list_13), len(list_14), len(list_15), len(list_16),
        len(list_17), len(list_18), len(list_19), len(list_20), len(list_21), len(list_22), len(list_23), len(list_24),
        len(list_25), len(list_26), len(list_27), len(list_28), len(list_29), len(list_30))

while i < m:
    for first_string in list_1[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_1[i])
            res_file.write(s + '\n')

    for first_string in list_2[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_2[i])
            res_file.write(s + '\n')

    for first_string in list_3[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_3[i])
            res_file.write(s + '\n')

    for first_string in list_4[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_4[i])
            res_file.write(s + '\n')

    for first_string in list_5[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_5[i])
            res_file.write(s + '\n')

    for first_string in list_6[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_6[i])
            res_file.write(s + '\n')

    for first_string in list_7[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_7[i])
            res_file.write(s + '\n')

    for first_string in list_8[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_8[i])
            res_file.write(s + '\n')

    for first_string in list_9[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_9[i])
            res_file.write(s + '\n')

    for first_string in list_10[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_10[i])
            res_file.write(s + '\n')

    for first_string in list_11[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_11[i])
            res_file.write(s + '\n')

    for first_string in list_12[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_12[i])
            res_file.write(s + '\n')

    for first_string in list_13[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_13[i])
            res_file.write(s + '\n')

    for first_string in list_14[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_14[i])
            res_file.write(s + '\n')

    for first_string in list_15[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_15[i])
            res_file.write(s + '\n')

    for first_string in list_16[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_16[i])
            res_file.write(s + '\n')

    for first_string in list_17[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_17[i])
            res_file.write(s + '\n')

    for first_string in list_18[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_18[i])
            res_file.write(s + '\n')

    for first_string in list_19[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_19[i])
            res_file.write(s + '\n')

    for first_string in list_20[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_20[i])
            res_file.write(s + '\n')

    for first_string in list_21[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_21[i])
            res_file.write(s + '\n')

    for first_string in list_22[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_22[i])
            res_file.write(s + '\n')

    for first_string in list_23[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_23[i])
            res_file.write(s + '\n')

    for first_string in list_24[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_24[i])
            res_file.write(s + '\n')

    for first_string in list_25[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_25[i])
            res_file.write(s + '\n')

    for first_string in list_26[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_26[i])
            res_file.write(s + '\n')

    for first_string in list_27[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_27[i])
            res_file.write(s + '\n')

    for first_string in list_28[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_28[i])
            res_file.write(s + '\n')

    for first_string in list_29[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_29[i])
            res_file.write(s + '\n')

    for first_string in list_30[i]:
        with open('C:\\csv\\merged.csv', 'a', newline='') as res_file:
            s = ''.join(list_30[i])
            res_file.write(s + '\n')

    i += 1

    if i % 100000 == 0:
        print("\n100k merged")

print("merge is done")

print("The job is done!")
