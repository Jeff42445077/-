flag = True
number = 1

while flag:
    answer = input('为什么超级英雄都穿紧身衣？')
    if number <= 6 :
        if answer == ('救人要紧') :
            flag = False
            print('Congrats my man!')
        else :
            print('Maybe try another one!')
    else :
        print('次数用完了')
        break
    print(f'[这是第{number}次回答]')
    number += 1
