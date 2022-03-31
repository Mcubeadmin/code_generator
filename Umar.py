loadNum = int(input("Enter the No of Load Cases: "))
Lists = []

print("Enter the Load type and load title seperated by (,)")
for i in range(loadNum):
    data = input("Enter the data: ")
    splitdata = data.split(",")
    Lists.append(splitdata)


for i in range(loadNum):
    print("LOAD " + str(i+1) + " LOADTYPE " + Lists[i][0] + " TITLE " + Lists[i][1])

