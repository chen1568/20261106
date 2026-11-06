wall = [45, 61, 27, 38, 50, 74, 63, 19, 56, 62, 82, 36]
list_answers = []
a = 0
b = 0
c = 0
for i in range(len(wall)):
    for j in range(len(wall)):
        if(j==i):
            continue
        a = wall[i]
        b = wall[j]
        if(a+b == 100):
            list_answers.append(a)
            list_answers.append(b)
            wall[i] = 0
            wall[j] = 0
print("「密碼： {}」".format(list_answers))