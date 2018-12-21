f = open('perepis.txt')
s=str()
g=int()
for line in f.readlines():
    a=int(line[len(line)-3::])
    if(a<78):
        y=line[len(line)-11::]
        temp=line.find(' ')
        index = temp
        line = line[:index]
        line = line[0:]
        print(line," ",y)
        g+=1
f.close()
print(g)