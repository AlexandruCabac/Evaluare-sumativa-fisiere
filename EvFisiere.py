t,out1='',''
with open("C:\\Users\\Phantom\\Desktop\\INPUT.txt",'r')as f:
    data=list(f.readlines())
print('Nr.'+'\t'+'Numele'+'\t'+'Prenumele'+'\t'+'Nota1'+'\t'+'Nota2'+'\t'+'Nota3')
for i in data:
    t+=i
    if '\n' in i:
        i=i[:-1]
    print(i)
    linie=i.split()
    n="%.2f"%((float(linie[3])+float(linie[4])+float(linie[5]))/3)
    out2=linie[0]+'\t'+linie[1]+'\t'+linie[2]+'\t'+str(n)
    out1=out1+'\n'+out2
print('Nr.'+'\t'+'Numele'+'\t'+'Prenumele'+'\t'+'Media'+out1)
with open("C:\\Users\\Phantom\\Desktop\\REZERVA.txt",'w')as f:
    f.write(t)
with open("C:\\Users\\Phantom\\Desktop\\OUTPUT.txt",'w')as f:
    f.write(out1)