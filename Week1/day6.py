'''Author = Leva DU'''
#左上三角格式输出九九乘法表
for i in range(1,10):
    for j in range(i,10):
       print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")