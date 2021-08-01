class Myclass:
    def fun(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a

obj=Myclass()
result=obj.fun(10,20,30)
print("Value:",result)


# class Myclass:
#     def fun(self,*args):
#         sum=0
#         for i in args:
#             sum+=i
#         print("Sum Value:",sum)
# 
# obj=Myclass()
# obj.fun(10)
# obj.fun(10,20)
# obj.fun(10,20,30)
# obj.fun(10,20,30,40)

