file=open('filelist.txt','r')
file3=open('filelistprint.txt','w')
for line in file:
    file1=open(line[46:len(line)-2].strip(),'r')
    for line1 in file1:
        e=line1
    a=e+' '*(6-len(e))+line[46:len(line)-6]+'\n'
    file1.close()
    file3.write(a)
file.close()
file3.close()
