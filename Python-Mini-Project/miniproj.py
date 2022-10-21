number1 =float(input ('Enter first number:'))
number2 = float(input ('Enter second number:'))

total = number1 * number2
print(total)

newtotal = total + 1100
print(newtotal)


english = 50
maths = 70
science = 70

total = english + maths + science
average = total / 3
print("Your average score is :")
print(average)

number1 =float(input ('Enter first number:'))
number2 = float(input ('Enter second number:'))

if number1 > number2:
    number1bigger = True
else:
    number1bigger = False

print('It is', number1bigger, 'that number1 is bigger.')

password = "test123"
user = input("Please enter your password: ")
if password == user:
  print("Password is correct")
else:
  print("ERROR: Try again")

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

