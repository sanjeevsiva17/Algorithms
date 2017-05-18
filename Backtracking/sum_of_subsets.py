inp = [5, 7, 10, 12, 15, 18, 20]
tSum = 35
numele = len(inp)
set = [0 for x in range(numele)]
sele = [0 for x in range(numele)]
inp.sort()
set = inp


def findSubSets(sumtn, index, sumor):
    selele[index] = 1
    if tSum == set[index] + sumtn:
        ch = ''
    for i in range(nos):
        if selele[i] == 1:
            ch = ch + str(set[i]) + ' '
            print(ch)
        if (index + 1 < numele) and (sumtn + set[index] + set[index + 1] <= tSum):
            findSubSets(sumtn + set[index], index + 1, sumor - set[index])
        selele[index] = 0
        if (index + 1 < numele) and (sumtn + set[index + 1] <= tSum) and (sumtn + sumor - set[index] >= tSum):
            findSubSets(sumtn, index + 1, sumor - set[index])


def findSets(set, tSum):
    sumele = 0
    for i in range(num):
        sumele = sumele + set[i]


findSubSets(0, 0, sumele)
findSets(inp, tSum)
