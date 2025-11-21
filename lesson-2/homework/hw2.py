#1
name = input("Your name - ")
b_year = int(input("Year of birth - "))

age = 2025 - b_year

print("Name -",name,"\nAge -",age)

#2
txt = 'LMaasleitbtui'
laseti = []
malibu = []
for i in txt:
    if i.lower() in 'laseti'.lower():
        if i.lower() not in laseti:
            laseti.append(i.lower())
    if i.lower() in 'malibu'.lower():
        if i.lower() not in malibu:
            malibu.append(i.lower())
print(laseti)
print(malibu)

#3
txt1 = 'MsaatmiazD'
matiz = []
damas = []
for i in txt1:
    if i.lower() in 'matiz'.lower():
        if i.lower() not in matiz:
            matiz.append(i.lower())
    if i.lower() in 'damas'.lower():
        if i.lower() not in damas:
            damas.append(i.lower())
print(matiz)
print(damas)

#4
txt2 = "I'am John. I am from London"
area = txt2[-6:]
print(area)

#5
reverse = input("Type something >>> ")
reverse = reverse[::-1]
print(reverse)

#6
smth = input(">>> ")
vowel_cnt = []
for i in smth:
    if i.lower() in 'aeiou':
        vowel_cnt.append(i.lower())
print("Number of vowels -",len(vowel_cnt))

#7
nums = []
for i in range(5):
    nums.append(int(input(">>> ")))

print("Max number -",max(nums))

#8
word = input(">>> ")
if word[::-1].lower() == word.lower():
    print(word,"is Palindrome word")
else:
    print(word,"is not Palindrom")

#9
domain = input("Email >>> ")
domain = domain.split("@")[1]
print(domain)

#10
import string
import secrets

letters = string.ascii_letters
digits = string.digits
specials = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

all_chars = letters + digits + specials
length = 10
password = ''.join(secrets.choice(all_chars) for _ in range(length))

print("Random password :",password)
