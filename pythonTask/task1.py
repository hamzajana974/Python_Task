#Task 01

# list1 = ['m','na','i','ke']
# list2 = ['y','me','s','lly']
# cont = []
# count=-1
# for i in list1:
#     count = count+1
#     if count == len(list1):
#         count = 0
#         break
#     res = list1[count]+list2[count]
#     cont.append(res)
# print(str(cont))

# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)

#Task 02
#Print list with another list like pointer
# list1 = ['Hello', 'Take']
# list2 = ['Dear', 'Sir']
# cont = []
# cont1 = []
# count=-1
# for i in list1:
#     count = count+1
#     if count == len(list1):
#         count = 0
#         break
#     res = list1[0]+list2[count]
#     cont.append(res)
#     res1 = list1[1]+list2[count]
#     cont1.append(res1)
# print(str(cont+cont1))

# Task 03
# print vertically and reverse list

# list1 = [10,20,30,40]
# list2 = [100,200,300,400]
# list2.reverse()
#
# for l1,l2 in zip(list1,list2):
#     print(l1,l2)

# Task 04
#Squre of list item

# number = [1,2,3,4,5,6,7]
# cont = []
# for i in number:
#     sqr = i**2
#     cont.append(sqr)
# print(cont)

#Task 05
# Empty string remove fro list

# list1 = ["Mike","","Emma","Kelly","","Brad"]
# cont = []
# for i in list1:
#     if i != "":
#         cont.append(i)
# print(cont)

# Task 06

# list1 =[5,20,15,20,25,50,20]
# cont = []
#
# for i in list1:
#     if i == 20:
#         cont.append(i)
# print(cont)

# Task 07

list1 = [5,10,15,20,25,50,20]
list1[3] = 200
print(list1)

# Task 08
# list1 = ['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
#
# sub_list = [ 'h','i','j']
#
# list1[2][1][2].extend(sub_list)
# print(list1)

# Task 09
# list1 = [10,20,[300,400,[5000,6000],500],30,40]
# list1[2][2].append(7000)
# print(list1)