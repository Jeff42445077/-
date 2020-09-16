def rabbit_hen(rabbit,hen):
     headnumber = rabbit+ hen
     legnumber = 4*rabbit + 2*hen
     return [headnumber,legnumber]

rabbit1 = float(input('请输入兔子的数量是：'))
hen1 = float(input('请输入鸡的数量是：'))
answer = rabbit_hen(rabbit1,hen1)
print('总共有'+str(answer[0])+'个头，\n总共有'+str(answer[1])+'条腿。')
