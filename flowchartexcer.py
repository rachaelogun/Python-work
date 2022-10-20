num = int(input('Please enter a number: '))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


physics = int(input('Please enter a number: '))
chemistry = int(input('Please enter a number: '))
maths = int(input('Please enter a number: '))

total= physics + chemistry + maths
percent = total /450*100

if percent >= 60:
    print("pass")
else:
    print(fail)




