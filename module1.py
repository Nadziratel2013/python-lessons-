f = open('perepis.txt')
l=[]
s=str()
l=f.read().splitlines()
for i in range(len(l)):
    s=s.join(l[i])
    print(s)
f.close()