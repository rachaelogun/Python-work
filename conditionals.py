from ast import Pass

#longer conditional statement
exam = int(input('Exam check part 1:'))
exam1 = 65
exam2 = 64

if exam1 < exam2:
    print ("pass")
else:
    print("fail")


#short ifelse conditional statement

exam1 = int(input('Exam check part 2:'))

if exam1 > 65:
    print("pass")
else:
    print("fail")
    

#short if/elif/else conditional statement
Distinction = 70
Merit = 69
Pass = 50

result = int(input('Exam check part 3:'))

if result <= 70:
  print("Distinction")
elif result <= 69:
  print("Merit")
else:
  print("Pass")
