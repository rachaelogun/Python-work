SOMETHING = int(input('Exam check part 3:'))

count = 0
while count < 2:
 count = count + 3
 if SOMETHING > 2:
     SOMETHING = SOMETHING + 2
     print(count, "is even")
 else:
     print(count, "is odd")


count = 0
while count < 9:
 count = count + 3
 if SOMETHING:
     print(count, "is even")
 else:
     print(count, "is odd")