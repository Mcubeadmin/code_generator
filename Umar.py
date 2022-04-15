loadNum = int(input("Enter the No of Load Cases: "))
Lists = []
count = []
countList = []

#load type and title input and splitting
print("Enter the Load type and load title seperated by (,)")
for i in range(loadNum):
    data = input("Enter the data: ")
    splitdata = data.split(",")
    print(data)
    print(splitdata)
    if bool(countList) == False:
        print("first")
        count.clear()
        count.append(splitdata[0])
        count.append(1)
    elif lastinput == splitdata[0]:
        print("second")
        for j in range(len(countList)):
            if countList[j][0] == lastinput:
                countList[j][1] = int(countList[j][1]) + 1
                break
    else:
        print("third")
        count.clear()
        count.append(splitdata[0])
        count.append(1)
    print(count)
    lastinput = splitdata[0]
    print(lastinput)
    countList.append(count)
    Lists.append(splitdata)

print(countList)


#load line code generation
print("\n")
for i in range(loadNum):
    print("LOAD " + str(i+1) + " LOADTYPE " + Lists[i][0] + " TITLE " + Lists[i][1])

"""#equation input
eq = input("\nEnter the equation to be generated: ")
eq = eq.split(" ")
print(eq)
"""