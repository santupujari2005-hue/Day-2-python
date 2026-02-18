#String functions
#str.endswith(" ")
str="I am studying python from YouTube"
print(str.endswith("ube"))
print(str.endswith("cbe"))
print(str.endswith("e"))
print(str.startswith("I"))

#str.capitalize() , capitalizes 1st charector
str1="i am studying python from YouTube."
print(str1.capitalize())
str1=str1.capitalize() #Both are wark's same
print(str1)

#str.replace(old,new)
str2="your name is Santosh"
print(str2.replace("your","my"))
print(str2.replace("Santosh","Yash"))

#str.find(word) returns 1st index of 1st occurrer
str3="your name is Santosh"
print(str3.find("o"))
print(str3.find("S"))
print(str3.find("is"))
print(str3.find("name"))

#str.count("am") counts the occurrence of substring
str4="i am from India and Yash from US"
print(str4.count("from"))
print(str4.count("a"))

