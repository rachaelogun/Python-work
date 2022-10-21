
password = "test123"
user = input("Please enter your password: ")
if password == user:
  print("Welcome Test:")
else:
    print("hint: name and number")
    print("ERROR: Try again")
    user = input("Please enter your password: ")

orderno1 =float(input ('Enter Order number:'))
orderno2 = float(input ('Enter Order number:'))

total = orderno1 * orderno2
print(total)
newtotal = total + 1100
print(newtotal)

Happy = 100
Sad = 20
Normal = 50

emotion = Happy + Sad + Normal
average = emotion / 3
print("Your emotion score is :")
print(average)

orderno3 =float(input ('Enter Order number:'))
orderno4 = float(input ('Enter Order number:'))

if orderno3 > orderno4:
    number3bigger = True
else:
    number3bigger = False

print('It is', number3bigger, 'that orderno3 is bigger.')


  #File 1

for i in range(101):
    print(i)

#File 2
for i in range(5,10):
    print(i)

#File 3
for i in range(10,21,2):
    print(i)

SOMETHING = int(input('Exam check part 3:'))

count = 0
while count < 1000000000000000000:
 count = count + 3
 if SOMETHING < 1000000000000000000:
     SOMETHING = SOMETHING + 2
     print(SOMETHING, "is even")
 else:
     print(count, "is odd")

