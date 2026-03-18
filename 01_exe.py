# from unicodedata import digit
# x = input('number between 1-9')
# while not x.isdigit():
#     x = input('number')
#     continue
# x = int(x)
# if x >=1 and x <=9:
#     for i in range(1, x + 1):
#         for j in range(1, i + 1):
#             print(j, end=' ')
#         print()
#     for k in range(x - 1, 0, -1):
#         for l in range(1, k + 1):
#             print(l, end=' ')
#         print()

y = 5
list1=[]
list2 = []
for i in range(1, y + 1):
    list1.append(i)
    for j in range(1, i + 1):
        list2.append(j)
    list1 = str(list1)
    print(list1)
list3 = " ".join(map(str, list2))
print(list3.replace("1", "\n1"))





