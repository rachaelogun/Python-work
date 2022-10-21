
SOMETHING = int(input('Exam check part 3:'))
count = 0
while count < 20:
 count = count + 3
 if SOMETHING < 20:
    SOMETHING = SOMETHING + 2
    print(SOMETHING, "is EVEN")
 else:
     print(count, "is ODD")