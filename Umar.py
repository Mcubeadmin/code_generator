loadNum = int(input("Enter the No of Load Cases: "))
Lists = []
countList = []

#load type and title input and splitting
print("Enter the Load type and load title seperated by (,)")
for i in range(loadNum):
    data = input("Enter the data: ")
    splitdata = data.split(",")
    count = []
    if bool(countList) == False:
        count.append(splitdata[0])
        count.append(1)
        countList.append(count)
    elif lastinput == splitdata[0]:
        for j in range(len(countList)):
            if countList[j][0] == lastinput:
                countList[j][1] = int(countList[j][1]) + 1
                break
    else:
        count.append(splitdata[0])
        count.append(1)
        countList.append(count)
    lastinput = splitdata[0]
    Lists.append(splitdata)

print(countList)


#equation input
eq = input("\nEnter the equation to be generated: ")
eq = eq.split(" ")
eqint = []
for element in eq:
    eqint.append(float(element))

print(eqint)
print(type(eqint))
eqinput = int(input("Which load to repeat: "))
iter = int(countList[eqinput - 1][1])
print(iter)

#load line code generation
print("\n")
for i in range(loadNum):
    print("LOAD " + str(i+1) + " LOADTYPE " + Lists[i][0] + " TITLE " + Lists[i][1])
for i in range(iter):
    count = 101 + i
    print("Load Combination " + str(count))
    print(*eqint, sep = ' ')
    for j in range(len(eqint)):
        if eqint[j] == eqinput:
            eqint[j] = eqint[j] + 1
            eqinput = eqinput + 1
            break
          