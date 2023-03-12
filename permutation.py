def permutation(a, x=0):

    if x >= len(a):
        print(a)
        return

    for i in range(x, len(a)):

        a[x], a[i] = a[i], a[x]
        permutation(a, x+1)
        a[x], a[i] = a[i], a[x]

#permutation(["aa", "aaa", "aB", "B"])

a = []
b = []
q = ""

while (q != "ok" ):
    q = input("Enter something : ")
    a.append(q)
    if (q == "ok" ):
        a.pop()
        break

    for j in a:
        if j not in b:
            b.append(j)



permutation(b)
print(type(b))
print(len(b))




