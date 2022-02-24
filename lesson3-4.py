def my_func(x, y):
   res = 1
   if y > 0:
        for i in range(int(y)):
            res *= x
        return res
   elif n < 0:
       for i in range(abs(int(n))):
           res *= x
        return 1 / res
    else:
        return res

x, y[float(input()) for i in range(2)]
print(my_func(x, y))