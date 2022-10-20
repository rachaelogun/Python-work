
SOMETHING = int(input('Exam check part 3:'))

count = 0
while count < 9:
 count = count + 3
 if SOMETHING < 9:
     SOMETHING = SOMETHING + 2
     print(SOMETHING, "is even")
 else:
     print(count, "is odd")
