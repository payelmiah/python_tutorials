f=open("F:\\Python\\working with json\\data\\funny.txt","r")
f_out=open("F:\\Python\\working with json\\data\\funnywrite.txt","w")
for line in f:
    tokens=line.split(' ')
    f_out.write("word cout "+str(len(tokens))+": "+line+"\n")


f.close()
f_out.close()