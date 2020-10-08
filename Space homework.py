#1
'''
def TictacToe(str) :
    for i in range (0, len(str), 3):
        print ("|", str[i:i+3], "|")


TTCGame = input("Please Enter TicTacToe Pattern as 9 character string: ")

TictacToe(TTCGame)
'''
#2
'''

numbers = [1,11,23,44,54,76,9,76,32,4,565,87,545]
isOdd = []
isEven = []

for i in numbers:
    if i % 2:
        isEven.append(i)
    else: isOdd.append(i)

print(isEven, isOdd)

'''

#3
'''

numbers = [1,11,23,44,54,76,9,76,32,4,565,87,545]
morethan100 = []
lessthan100 = []

for i in numbers:
    if i >= 100:
        morethan100.append(i)
    else: lessthan100.append(i)

print(morethan100, lassthan100)

'''

#4
'''

enterWord = input("Enter Random Word: " )
enterNum = int(input("Enter Random Number: "))

print(enterWord, enterNum)
'''


#5
''' 

enterNum1 = int(input("Enter Number 1: " ))
enterNum2 = int(input("Enter Number 2: "))

print(enterNum1*enterNum2)
'''

#6
'''

mixedList = [1,2,"George","32",32,"64",128]
x = 0
integers = []
strings = []

for i in mixedList:
    if type(mixedList[x]) == int :
        integers.append(i)
        x+=1
    else: strings.append(i)

print(integers, strings)
'''

#7
'''
enterList = input("Enter list of items you want to buy: ")
myList = enterList.split(",")
middleValue = (len(myList))/2

if len(myList) % 2 :
    print(myList[int(middleValue)])
else:print(myList[int(middleValue)-1], ",", myList[int(middleValue)])

print(myList)
'''

#8
'''
myList = []

def calculate35 (var):
    for var in range(1, int(var)+1):
        if var % 3 == 0 or var % 5 == 0 :
            myList.append(var)



calculate35(15)
print(myList)

'''

#9
'''
enterText = 0

while enterText != "Exit":
    enterText = input("Type 'Exit' if you want to end this nightmare:")
    print(enterText)

print("Game Over")
'''

#10
'''
myList = ["dog", "cat", "kangaroo", "elephant"]
x = 0

while myList[x] != "elephant":
    print(myList[x])
    x+=1
'''

#11
'''
myList = ["ნიკა 28 წლის" , "ნინი შავგრემანი" ,"მარიამი" , "ქერა მარიკა", "იოგურტი"]
print(myList[1:-1])

'''


