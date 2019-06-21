import random

name = input("名前を入力してください＞＞")
num = int(random.random()*10)

if(num==0):
    print("{}さんの運勢は大吉です".format(name))
elif(num>=1 and num<=5):
    print("{}さんの運勢は中吉です".format(name))
elif(num>=6 and num<=8):
    print("{}さんの運勢は小吉です".format(name))
elif(num==9):
    print("{}さんの運勢は凶です".format(name))
elif(num==10):
    print("{}さんの運勢は大凶です".format(name))