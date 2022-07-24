# Data Filter
from collections import defaultdict

outputDto = {}

# key dept id and value dept name
depts = {}
maxdepts = 0

# key as product id value as dept id
productsMap = {}

# key as orderId and value as productId set
orderPriorMap = defaultdict(list)

# key as orderId and value as productId set
orderTrainMap = defaultdict(list)


def initializeOutputObject():
    for i in range(7):
        day = {}
        for j in range(24):
            dept = {}
            for k in range(21):
                dept[k] = 0
            day[j] = dept
        outputDto[i] = day


def setDept(rows: list, start, end):
    for i in range(start, end):
        row = rows[i]
        deptId = int(row[0])
        depts[deptId] = row[1]
        # maxdepts = max(deptId, maxdepts)


def setProducts(rows: list, start, end):
    for i in range(start, end):
        row = rows[i]
        productsMap[int(row[0])] = int(row[1])


def setPriorProducts(rows: list, start, end):
    for i in range(start, end):
        row = rows[i]
        temp = orderPriorMap[int(row[0])]
        temp.append(int(row[1]))
        orderPriorMap[int(row[0])] = temp


def setTrainProducts(rows: list, start, end):
    for i in range(start, end):
        row = rows[i]
        temp = orderTrainMap[int(row[0])]
        temp.append(int(row[1]))
        orderTrainMap[int(row[0])] = temp


def setOrder(rows, start, end):
    for i in range(start, end):
        row = rows[i]
        orderId = int(row[0])
        isPrior = row[1] == 'prior'
        tempans = outputDto[int(row[2])][int(row[3])]
        productSet = None
        if isPrior:
            productSet = orderPriorMap[orderId]
            pass
        else:
            productSet = orderTrainMap[orderId]
            pass
        productSet = set(productSet)
        for pId in productSet:
            deptId = productsMap[int(pId)]
            tempans[deptId-1] += 1
        outputDto[int(row[2])][int(row[3])] = tempans


