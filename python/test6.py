def zhihu(a):
    def wrapper():
        print ('泻药')
        a()
        print('以上')

    return wrapper

@zhihu
def answer1():
    print('我也不知道啊')

answer1()
