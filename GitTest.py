input("名前を入力してください＞＞")
num = int(random.random()*10)
if(num==0):
    print("大吉")
elif(num>=1 and num<=5):
    print("中吉")
elif(num>=6 and num<=8):
    print("小吉")
elif(num==9):
    print("凶")
elif(num==10):
    print("大凶")