#STRINGS IN PYTHON
str1="Thise is a string" #best way to declare a sring
str2='Thise is a string' 
str3="""Thise is a string"""
str4='''Thise is a string'''
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

#\n is used to break the line
str5=" This is a string.\n we are creating it in pythpn"
print(str5)

#\t is used to give a tab space
str6="  This is a string.\twe are creating it in pythpn"
print(str6)

#Concatenation of strings
str7="Santosh"
str8="Pujari" 
print(str7+str8)#final_stri=str7+str8 or final_str=str7+" "+str8

#length of string
str9="Santosh"
len1=len(str9)
print(len1)
str10="Pujari"
len2=len(str10)
print(len2)
final_str=str9+" "+str10
len3=len(final_str)
print(len3)

#Indexing
str1="Santosh"
ch=str1[0]
print(ch)
print(str1[1])
print(str1[2])
print(str1[6]) #if str[7] gives error (string index out of range)

#Slicing 
str2="Python_Day"
print(str2[0:5]) #ending index is not included
print(str2[6:9])
print(str2[0:len(str2)])
print(str2[:6]) #[0:6]
print(str2[2:]) #print(str2[0:len(str2)])
print(str2[4:len(str2)])
#Slicing Negative Index
str3="Apple"
print(str3[-5:-2])





