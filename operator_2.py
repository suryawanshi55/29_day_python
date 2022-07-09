# p=int(input("enter the value of p:"))enter the value of p:34
# print(f"the value of p is{p}")the value of p is34
# p+=2 
# print("the value of p after p+=2 is {}".foemat(p))   36
# p-=4
# print("the value of p after p-=4 is {}".format(p))    30
# p*=6
# print("the value of p after p*=6 is {}".format(p))   204
# p**=2
# p/=2
# print("the value of p after p/=2 is {}".format(p))   17

# ....rational/comparision operators.....
# a=int(input("enter the value of a:"))#enter the value of a:6
# b=int(input("enter the value of b:"))#enter the value of b:8
# print(f"the value of{a}<{b} is {a<b}")   #the value of6<8 is True
# print(f"the value of {a}<={b} is {a<=b}")#the value of 6<=8 is True
# print(f"the value of {a}>={b} is {a>=b}")#the value of 6!=8 is True
# print(f"the value of {a}!={b} is {a!=b}")   #the value of 6!=8 is True

# a=int(input("enter the value of a:"))#enter the value of a:4
# b=int(input("enter the value of b:"))#enter the value of b:9
# print("the value of %d<%d=%d"%(a,b,a<b))
# print("the value of a=%d , b=%d and a<b=%d"%(a,b,a<b))    # the value of a=4 , b=9 and a<b=1
# print("the value of a=%d , b=%d and a>b=%d"%(a,b,a<=b))    #the value of a=4 , b=9 and a>b=1
# print("the value of a=%d , b=%d and a>=b=%d"%(a,b,a>=b))   # the value of a=4 , b=9 and a>=b=0
# print("the value of a=%d , b=%d and a!=b=%d"%(a,b,a!=b))   #the value of a=4 , b=9 and a!=b=1
# print("the value of a=%d , b=%d and a==b=%d"%(a,b,a==b))     #the value of a=4 , b=9 and a==b=0

# .......logical operator......
# a=int(input("enter the value of a:"))          #enter the value of a:8
# b=int(input("enter the value of a:"))          #enter the value of a:4
# print (" The value of a<b and b>a is {}".format(a<b and b>a))  #  The value of a<b and b>a is False  
# print (" The value of a>b and a<b is {}".format(a>b and a<b))   #  The value of a>b and a<b is False
# print (" The value of a!=b and a==b is {}".format(a!=b and a==b))# The value of a!=b and a==b is False
# print (" The value of a==b or a>bis {}".format(a==b or a>b))   # The value of a==b or a>bis True  
# print (" The value of a!=b or a<b is {}".format(a!=b or a<b))  # The value of a!=b or a<b is True 
# print (" The opposite of {}!={} is {}".format(a,b,not a!=b))   # The opposite of 8!=4 is False
       
#   .........Bitwise operator.......
# a=int(input("enter the value of a:"))      # enter the value of a:14
# b=int(input("enter the value of b:"))     #  enter the value of b:12
# c=int(input("enter the value of c:"))      # enter the value of c:16
# print("the value of {} & {} is {}".format(a,b,a&b))   #  the value of 14 & 12 is 12
# print("the value of {} | {} is {}".format(a,b,a|b))    # the value of 14 | 12 is 14

# Note- the formula for negation (-) is -(value+1)

# print("the value of ~{} is {}".format(a,~a)) # the value of ~14 is -15
# print("the value of ~{} is {}".format(c,~c))  ## the value of ~16 is -17

# .......Identity operator.....
# a=20
# b=20
# if(a is b):
#     print ("a & b do not have same Identity")
# else :
#     print("a and b do not have same Identity")     #a & b do not have same Identity
# if ( id(a) == id(b) ):
#     print("a and b do not have same identity")
else:
    # print ("a and b do not have same identity")     a and b do not have same identity
    