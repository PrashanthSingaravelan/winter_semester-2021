def get_even(list1):
    if sum(list1) % 2 != 0:
        list1.append(1)
    else:
        list1.append(0)
    return list1

def get_odd(list1):
    if sum(list1) % 2 == 0:
        list1.append(1)
    else:

        list1.append(0)
    return list1


def check_column(f_list):
    global nop, n
    print(n)
    print("list : ", f_list)
    list_re = []
    for i in range(nop + 1):
        list_re.append(sum([x[i] for x in f_list]))
    print("list_re : ", list_re)
    if(n == 2):
        for i in range(len(list_re)):
            list_re[i] = list_re[i] % 2
    else:
        for i in range(len(list_re)):
            list_re[i] = (list_re[i] + 1) % 2
    return list_re

def to_string(listfin, m):

    string2 = m.join([str(y) for y in listfin])
    return string2


n = 0
n = int(input("Enter the standard that sender and receiver are gonna follow : '1' for 'Odd_parity'  and '2' for 'Even_parity' : "))
print("At the Sender End...")
data = input("Enter the data to send in binary : ")
nop = int(input("Enter the no of packets for your data have to be encrypted : "))
extra = (nop - ((len(data)) % nop)) % nop
extra_bits = str('0' * extra)
data = extra_bits + data

list_data = [[int(x) for x in data[i:i + nop]]
             for i in range(0, len(data), nop)]
print(list_data)
if (n == 2):
    for i in list_data:
        get_even(i)
else:
    for i in list_data:
        get_odd(i)

print(list_data)
list_data.append(check_column(list_data))
print(list_data)
for l in range(len(list_data)):
    list_data[l] = to_string(list_data[l], '')
print("Sender data is : ", to_string(list_data, ' '))