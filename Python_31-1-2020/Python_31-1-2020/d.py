li = range(6, 32, 3)
print(li)

#for i in li:
#    print(i)

try:
    o = iter(li)
    print(o)
    #print(dir(o))
    print(o.next())
    print(o.next())
    print(o.next())
    print(o.next())
    print(o.next())
    print(o.next())
    print(o.next())
    print(o.next())
    print(o.next())
    print(o.next())
except StopIteration as e:
    pass
except Exception as e:
    pass