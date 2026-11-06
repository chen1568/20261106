menu = {60:"珍奶",30:"紅茶",25:"冬瓜茶",80:"雞排",40:"地瓜球",50:"烤玉米"}
drink = [60,30,25]
snack = [80,40,50]
ans = []
temp = []
for i in range(len(drink)):
    for j in range(len(snack)):
        if(drink[i]+snack[j]<=100):
            ans.append(menu[drink[i]]+"+"+menu[snack[j]])
print(ans)