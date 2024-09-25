import sys
import csv


def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)



def viewer():
    data = []
    with open('data.csv') as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)
    print(data)
    return data


#view()

def remove(i):
    def save(j):
        with open('data.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
    new_list = []
    telephone = i

    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telephone:
                    new_list.remove(row)
        save(new_list)

# remove('2973')
# view()

def update(i):
    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(i)

    new_list = []
    telephone = i[0]

    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    email = i[4]

                    data = [name, gender, telephone, email]
                    index = new_list.index(row)
                    new_list[index] = data
    update_newlist(new_list)

# sample = ['13421','laura','Female','32432','hdjw']
# update(sample)

def search(i):
    data = []
    telephone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    print(data)
    return data

