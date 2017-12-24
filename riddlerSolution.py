import itertools
import sys
import re

def noEquals(operatorList):
    noEquals = True
    for operator in operatorList:
        if(operator == "5"):
            return False
    return True

digits = int(sys.argv[1])
operatorLists = []
validDigits = '0123456'
for num in itertools.product(validDigits, repeat=digits-1):
    s = ''.join(num)
    operatorLists.append(s)
attempts = 0
numValid = 0
for a in range(1000000, 2000000):
    if(a%10000==0):
        print(a)
    textNum = str(a)
    while(len(textNum)<digits):
        textNum = "0" + textNum

    isValid = False
    for operatorList in operatorLists:
        if(noEquals(operatorList) == True):
            continue

        atEquals = False
        iterLocation = 0
        expressionList = []
        expression = textNum[iterLocation]
        while(iterLocation < digits):
            if(iterLocation == digits-1):
                expressionList.append(expression)
                break    
            if(operatorList[iterLocation] == "5"):
                expressionList.append(expression)
                expression = textNum[iterLocation+1]
            if(operatorList[iterLocation] == "0"):
                expression = expression + "+" + textNum[iterLocation+1]
            if(operatorList[iterLocation] == "1"):
                expression = expression + "-" + textNum[iterLocation+1]
            if(operatorList[iterLocation] == "2"):
                expression = expression + "*" + textNum[iterLocation+1]
            if(operatorList[iterLocation] == "3"):
                expression = expression + "/" + textNum[iterLocation+1]
            if(operatorList[iterLocation] == "4"):
                expression = expression + "**" + textNum[iterLocation+1]
            if(operatorList[iterLocation] == "6"):
                expression = expression + "%" + textNum[iterLocation+1]
            
            iterLocation += 1

        isValid = True
        for c in range(0, len(expressionList)-1):
            try:
                if(expressionList[c].count("*") >= 4):
                    digitsOnly = re.sub("[^0-9]", "", expressionList[c])
                    numAbove = 0
                    exponentSum = 0
                    for a in range(0, len(digitsOnly)):
                        if(int(digitsOnly[a]) >= 2):
                            numAbove += 1
                        exponentSum += int(digitsOnly[a])
                    if(numAbove >= 3 and exponentSum >= 10):
                        isValid = False
                        continue
                if(expressionList[c+1].count("*") >= 4):
                    digitsOnly = re.sub("[^0-9]", "", expressionList[c+1])
                    numAbove = 0
                    exponentSum = 0
                    for a in range(0, len(digitsOnly)):
                        if(int(digitsOnly[a]) >= 2):
                            numAbove += 1
                        exponentSum += int(digitsOnly[a])
                    if(numAbove >= 3 and exponentSum >= 10):
                        isValid = False
                        continue
                if(eval(expressionList[c]) != eval(expressionList[c+1])):
                    isValid = False
            except (OverflowError, ZeroDivisionError):
                isValid = False
                break
        if(isValid == True):
            break
    attempts += 1
    if(isValid == True):
        numValid += 1
    else:
        print(textNum)
    
print("Attempts: " + str(attempts))
print("Number valid: " + str(numValid))
print("Percent valid: " + str(numValid/attempts))
