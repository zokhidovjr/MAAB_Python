#1
my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}
asc_dict = dict(sorted(my_dict.items(),key=lambda x: x[1]))
desc_dict = dict(sorted(my_dict.items(),key=lambda x: x[1],reverse=True))
print(my_dict,'\n',asc_dict,'\n',desc_dict)

#2
dct = {0: 10, 1: 20}
dct[2] = 30
print(dct)

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
mix = dic1 | dic2 | dic3
print(mix)

#4
n=int(input(">>> "))
sqr = {}
for i in range(1,n+1):
    sqr[i] = i*i
print(sqr)

#5
sqr = {}
for i in range(1,16):
    sqr[i] = i*i
print(sqr)

#SET 1
my_set = set([1,22,65,65,98,47,44,2])
print(my_set)

#2
my_set = {1,22,65,65,98,47,44,2}
for i in my_set:
    print(i)

#3
my_set = {1,22,65,65,98,47,44,2}
#my_set.add(30)
my_set.update([30,23,89,55])
print(my_set)

#4
my_set = {1,22,65,65,98,47,44,2}
my_set.remove(22)
print(my_set)

#5
my_set = {1,22,65,65,98,47,44,2}
my_set.discard(24)
print(my_set)
