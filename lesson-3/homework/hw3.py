#1
fruits = ['Banana','Apple','Melon','Peach','Pineapple']
print(fruits[2])

#2
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
full = list1 + list2
print(full)

#3
nums = [23,89,100,99,30,50,77,44,0]
first = nums[0]
middle = nums[len(nums)//2]
last = nums[-1]
new = [first,middle,last]
print(new)

#4
movies = ['One Piece','Avangers','Spider-man','Attack on Titan','Batman']
movies = tuple(movies)
print(movies)

#5
cities = ['New York','Rome','Tashkent','Paris','London']
for i in cities:
    if i.lower() == 'Paris'.lower():
        print(i,'is found')
        break
else:
    print("Paris not found")

#6
numbers = [56,989,323,848,2,55,-99,4]
copy = numbers.copy()
print(copy)

#7
numbers = [56,989,323,848,2,55,-99,4]
print("Before",numbers)
numbers[0],numbers[-1] = numbers[-1],numbers[0]
print("After",numbers)

#8
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[3:7])

#9
colors = ['Red','Green','blue','yellow','blue','blue','purple']
cnt_blue = sum(1 for i in colors if i.lower() == 'blue')
print(cnt_blue)

#10
animals = ('wolf','lion','tiger','shark')
lion_index = next(i for i, a in enumerate(animals) if a.lower() == 'lion')
print(lion_index)

#11
numbers1 = (1,2,3,4,5,6,7,8,9,10)
numbers2 = (56,989,323,848,2,55,-99,4)
mix = numbers1+numbers2
print(mix)

#12
l_numbers = [56,989,323,848,2,55,-99,4]
t_numbers = (1,2,3,4,5,6,7,8,9,10)
print("Length of a list",len(l_numbers),
      "\nLength of a tuple",len(t_numbers))

#13
five = (23,65,33,30,89)
lst = list(five)
print(lst)

#14
numbers2 = (56,989,323,848,2,55,-99,4)
print("Max",max(numbers2),"\nMin",min(numbers2))

#15
animals = ('wolf','lion','tiger','shark')
print("Before",animals)
reverse = tuple(reversed(animals))
print("After",reverse)
