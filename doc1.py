# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d2:
#         if i in d1:
#             d1[i]+=d2[i]
#         else:
#             d1[i]=d2[i]
# print(d1)

# a="puji"
# b=12
# print(a+b)
a={'a':200,'b':100,'c':300,'d':600}
b={'e':100,'b':250,'c':100,'f':100}
for i in b:
        if i in a:
            a[i]+=b[i]
        else:
            a[i]=b[i]
print(a)