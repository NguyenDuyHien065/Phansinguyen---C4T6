list = [5, 7, 300, 90, 24, 50, 75]
n = 0
for c in list:
    if c>n:
        n=c
print("Now my biggest sheep has size ", n, ". Let's sheer it")
for c in list:
    if c == n:
        list.remove(c)
print ("After sheering, this is my flock ")
print (list)