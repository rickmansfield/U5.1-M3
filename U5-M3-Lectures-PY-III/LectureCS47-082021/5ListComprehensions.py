l = [1, 2, 3, 4, 5]
for i in range(len(l)):
  l[i] = l[i] * 2

l2 = [l[i] * 2 for i in range(len(l)) if l[i] == 4]
# for i in range(len(l)):
# l2.append(l[i] * 2)


l3 = []
for i in range(len(l)):
  l3.append(l[i] * 2)
print(l)
print(l2)
print(l3)
print(l)


