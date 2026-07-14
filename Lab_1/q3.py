n = int(input("Enter order of matrix: "))

A = []
print("Enter matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

m = int(input("Enter power: "))

result = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    result.append(row)

for k in range(m):
    temp = []
    for i in range(n):
        row = []
        for j in range(n):
            s = 0
            for x in range(n):
                s += result[i][x] * A[x][j]
            row.append(s)
        temp.append(row)
    result = temp

print("Result:")
for row in result:
    print(row)