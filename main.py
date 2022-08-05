HRML = open("HRMasterlist.txt", "r")

affectedCount = 0
totalPay = 0.00

for rows in HRML:
    elementList = rows.split("|")
    if elementList[7] == "FullTime" and int(elementList[3][6:10]) > 1995:
        totalPay += float(elementList[8]) * 0.85
        affectedCount += 1
print(f"The total pay to the {affectedCount} affected employee is ${totalPay}")