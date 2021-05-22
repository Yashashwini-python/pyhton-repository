##country="India"
##print(country)
##print(type(country))

##
##country="90"
##print(country)
##print(type(country))

##country='Australia'
##print(country[3])
##
##country[2]='d'
##print(country)

##
##statement = 'MI versus CSK'
##print(statement[2])
##
##print(statement[0:])
##
##print(statement[0:8])
##print(statement[-1])
##
##print(statement[-2])
##
##print(statement[-1:])
##
##print(statement[-2:])

##country = 'India is'
##
##print(len(country))
##print(dir(country))

##country='india is my country
##         and i love my country'
##
##print(country)

##country = '''India is my country
##and i love my country'''
##print (country)
##
##country = '''India is my country \
##and i love my country'''
##print (country)
##
##path = "c:\newfolder\time.txt"
##print (path)

##path =r"c:\newfolder\time.txt"
##print (path)

##country = input("Enter your name")
##print(country)
##print(type(country))

#var = "India is"
#for x in var:
#    if x =="i" or x=="a":
#        print("success")
#        break
#    else:
#        print("failure")

#var ="India is history"
#for x in enumerate(var):
 #   print (x)

#var ="India is history"
#for x ,y in enumerate(var):
#    print (x)
#    print(y)


#for x,y in enumerate(var):
#    if x%2 == 0:
#        print(x,y)

#for x in range(10):
 #   print(x)

#for x in range(1,10):
#    print(x)

#for x in range(0,10,2):
#    print(x)


#-------------List------------

#var =[]
#print(type(var))

#var=["dhoni","ashwin","rohit",7,8,10,"raina"]
#print(var[0])


#var[1]="kohli"
#print(var)


#deep copy
#var =["a","b","c"]
#var1 =var #deep copy
#print (var)
#print(var1)
#var[0]="z"
#print(var)
#print(var1)

#shallow copy

#var =["a","b","c"]
#var1 =var[:] #shallow copy
#print (var)
#print(var1)
#var1[0]="z"
#print(var)
#print(var1)

#var=['dhoni','kohli',"ashwin","rohit"]
#var.insert(1,"raina")
#print(var)
#var.append("welcome")
#print(var)
#var.append("welcome","India")

#var.append(["welcome","India"])
#print(var)

#var.extend(["welcome","India"])
#print(var)

#var=['dhoni','kohli',"ashwin","rohit"]
#var.pop()
#print(var)

#var.pop(0)
#print(var)

#var.remove("ashwin")
#print(var)

#var.clear()
#print(var)


#del var[0]
#print(var)

#var=['dhoni','kohli',"ashwin","rohit"]
#del(var)
#print(var)

#op=[0,2,4,6,8]

#op=[]
#for x in range(9):
#    if x%2 == 0:
#        op.append(x)
#print(op)

#output= [x for x in range(9) if x%2 == 0] #list Comprehension
#print(output)

#------------------tuple-------------
#var =("dhoni",)
#print(type(var))

#var = ("dhoni","kohli","dhoni")
#var[0]="raina"
#print (var)

#print(dir(var))
#print(var.count("dhoni"))

#var ="dhoni","kohli"
#print(var)

#a=("a",)
#b=("b",)
#print(a+b)


#----------------------------------Dictionary

#my_dict ={}
#print(type(my_dict))

#in dictionary no index based storage
#key and value pair
#Uniqueness
#hashing
#u cannot duplicate
#unordered collection

#my_dict ={"name":"mounika","lang":"python"}
#print(my_dict)

#"It will add data
#my_dict ={"name":"mounika","lang":"python"}
#my_dict['country']="India"
#print(my_dict)

#overides data
#my_dict ={"name":"mounika","lang":"python","country":"pak"}
#my_dict['country']="India"
#print(my_dict)

#my_dict ={"name":"mounika","lang":"python","country":"pak"}
#my_output = my_dict['lang']
#print(my_output)

#my_dict ={"name":"mounika","lang":"python","country":"pak","lang":"Java"}
#my_output = my_dict['lang']
#print(my_output)
#It will print only java as output because of uniqueness


#my_dict = {"Name":"dhoni",5:"Kohli",9.0:"ashwin",("a","b"):"raina",True:"saina"}
#print(my_dict)
#print(my_dict[("a","b")])
#print(my_dict[True])

#my_dict = {False:"dhoni",1:"kohli",1.0:"rohit"}
#print(my_dict[False])

#my_dict = {True:"dhoni",1:"kohli",1.0:"rohit"}
#print(my_dict[True])

my_dict={"name":["dhoni","kohli"],"age":{"number":[55,66,67]}}
#print(my_dict)
#print(my_dict['name'][1])
#print(my_dict['age']['number'][1])

#for x in my_dict:
 #   print(x)

#for x in my_dict.items():
 #   print(x)

#for x,y in my_dict.items():
 #   print(x)
  #  print(y)

#for x in my_dict.values():
 #   print(x)

#output ={0:0,1:1,2:4,3:9,4:16}
output={}

#for x in range(5):
#    output[x]=x*x

#print(output)

#output = {x:x*x for x in range(5)}

#print (output)

#var = {"nmae":"dhoni"}
#var1 = {"age":55}

#var.update(var1)
#print (var)

##var = {"nmae":"dhoni"}
##var1 = {"age":55}
##
##new = {**var,**var1}
##print(new)



##x= "Hello World" #str
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))

##x = 20	#int
##
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = 20.5	#float
##
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = 1j	#complex
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = ["apple", "banana", "cherry"]	#list
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = ("apple", "banana", "cherry")	#tuple
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = range(6)	#range
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = {"name" : "John", "age" : 36}	#dict
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = {"apple", "banana", "cherry"}	#set
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = frozenset({"apple", "banana", "cherry"})	#frozenset
###display x:
##print(x)
##
###display the data type of x:
##print(type(x)) 
##
##x = True	#bool
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##x = b"Hello"	#bytes
##
###display x:
##print(x)
##
###display the data type of x:
##print(type(x))
##
##Many Values to Multiple Variables
##
##x, y, z = "Orange", "Banana", "Cherry"
##print(x)
##print(y)
##print(z)

##One Value to Multiple Variables

##x= y= z = "Orange"
##
##print(x)
##print(y)
##print(z)
##
##Unpack a Collection
##
##
##fruits = ["apple", "banana", "cherry"]
##x, y, z = fruits
##print(x)
##print(y)
##print(z)

##Looping through a string
##for x in "banana":
##  print(x)


##x='python'
##y='awsome'
##
##print('python is' + y)
##print(x + y)
##x= "  python"
##
##print(x.strip())

##def My_Function():
##    print("Welcome to HDFC bank")
##
##My_Function()
##
##def My_Function(Name):
##    print("Hello ",Name," welcome to HDFC bank")
##
##My_Function('Dhoni')
##My_Function('Kohli')
##
##def My_Function(Name,Country):
##    print('Hello ',Name,'from',Country,' welcome to HDFC bank')
##
##My_Function('Dhoni',"India")
##My_Function('Kohli','aus')


##def My_Function(Name,Country="India"): #Default Argument
##    print('Hello ',Name,'from',Country,' welcome to HDFC bank')
##
##My_Function('Dhoni')
##My_Function('Kohli','aus')
##
##def My_Function(Name="Dhoni",Country="India"): #Default Argument
##    print('Hello ',Name,'from',Country,' welcome to HDFC bank')
##
##My_Function()
##My_Function('Kohli','aus')
##
##This below code will give error because we are passing default argument and calling
##country it won't replace with the country. it will call first argument itself



##Funciton with Keyword Argument

##def My_Function(Name,Country): #Default Argument
##    print('Hello ',Name,'from',Country,' welcome to HDFC bank')
##
##My_Function(Country = 'India',Name='Dhoni')
##My_Function('Kohli','aus')

##def My_Passed_Student(*names): ##*args
##    print(names)
##
##My_Passed_Student('kohli','Dhoni')
##My_Passed_Student('ashwin')
##oupt will be in form of tuple
##
##
##def My_Passed_Student(**names): ##*kwargs
##    print(names)
##
##My_Passed_Student(name='kohli',age=44)
##My_Passed_Student(name='ashwin',team="delhi")

##output will be dictionary

##def My_Score(Eng,Math):
##    total = Eng + Math
##    return
##print(My_Score(44,77))
##
##def My_Score(Eng,Math):
##    total = Eng +Math
##    return
##my_output =My_Score(44,77)
##print(my_output)
##
##def My_Score(Eng,Math):
##    total = Eng +Math
##    return total
##my_output =My_Score(44,77)
##print(my_output)
##
##def My_Score(Eng,Math):
##    total = Eng +Math
##    return total
##my_output =My_Score(44,77)
##print(my_output)

##def My_Score(Eng,Math,Name):
##    total = Eng +Math
##    return total,Name
##my_output =My_Score(44,77,"Dhoni")
##print(my_output)
####o/p will be in tuple 
##print(my_output[1])

##def My_Score(Eng,Math,Name):
##    total = Eng +Math
##    return total,Name
##my_total,My_name =My_Score(44,77,"Dhoni")
##print(my_total)
##print(My_name)

#Scoping #LEGB
##var =1000 #Global
##def fun():
##    var=100 #Enclosed
##    def new():
##        var=10 #Local
##        print(var)
##    new()
##fun()
##
##op = 10 #Local

##var =1000 #Global
##def fun():
##    var=100 #Enclosed
##    def new():
####        var=10 #Local
##        print(var)
##    new()
##fun()
##
##op = 100 #Enclosed
##
##var =1000 #Global
##def fun():
####    var=100 #Enclosed
##    def new():
####        var=10 #Local
##        print(var)
##    new()
##fun()
##
##op = 1000 #Global
##
##var=1000
##def fun():
##    var=var+10
##    print(var)
##fun()
####oup=local variable 'var' referenced before assignment

##var=1000
##def fun():
##    global var
##    var=var+10
##    print(var)
##fun()

##var=0
##def fun():
##    global var
##    
##    print("Hello",var)
##    var=var+1
##    
##    fun()
##
##fun()

var=0
def fun():
    global var
    
    print("Hello",var)
    var=var+1
    if var == 100:
        return
    
    fun()

fun()



























































































































 















































