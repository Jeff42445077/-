import random
a = random.randint(1,100)
print('-------小菊花妈妈课堂开课啦-------')
temp = input('亲爱的小朋友 快想一想 小菊花妈妈想的是哪个数字呀\n')
if isinstance(temp,int) :
    guess = int(temp)
    while guess != a :
        temp = input('亲爱的小朋友 重新想一想 小菊花妈妈想的是哪个数字呀\n')
        guess = int(temp)
        if guess == a :
            print('我操了 你怎么知道问题的答案呢')
            print('虽然你猜中了 但是 这一切 值得么')
        else:
            if guess > a :
                print('诶，哥，大了，大了。')
            else:
                print('小了，小了。')

            print('傻逼 哈哈哈这都猜不到 ')
    print('-------小菊花妈妈课堂下课啦-------')
else:
    print ('你丫说啥呢傻逼东西，让你说数字哦，给你机会你不中用啊。')
    print('-------小菊花妈妈课堂下课啦-------')
