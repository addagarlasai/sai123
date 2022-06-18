#1.write a python function to get first letter of each word of complete string
#given by the user?
s = input("enter your string:")
b =s.split()
d=''
for i in b:
       c=i[0].upper()+i[1:].lower()
       d=d+" "+c
print(d)       
       
