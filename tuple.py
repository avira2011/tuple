'''stuDetails_tuple=('Surabhi', 89)

#packing
address = 

for x in address:
    print (x, end = " ")

#unpacking


house, apartment, city, state, pin = address

#nested tuple
n_tuple = ("mouse", [8,4,6], (1, 2, 3))

#nested index

print(n_tuple[0][3])
print(n_tuple[1,1])'''









group_records = []

for i in range(2):
    print('Enter group',(i+1))
    group_name = input("Enter your group name: " )
    group_size = input("Enter the size of your group: ")
    comp_date = input("Enter the date of your competition: ")
    venue = input("Enter the venue: ")
    medal_type = input("Enter the medal type: ")

    group_tuple = (group_name, group_size, comp_date, venue, medal_type)

    group_records.append(group_tuple)

for j in group_records:
     print(j)

