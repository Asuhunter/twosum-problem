
def Twosum(a1: list, num):
    for i in range(len(a1) - 1):
        for j in range(i + 1,len(a1)):
            if num == a1[i] + a1[j]:
                return i, j

a = [4,3,6,9]

p1 = Twosum(a, 9)
print(p1)
