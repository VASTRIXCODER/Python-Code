#working with arithimetic operators (+,-,*,/(division operator),//(floor division operator),%(modulus divison operator),**(power operator)) 

print(9/2)
print(9.0/2)
print(9/2.0)
print(9.0/2.0)

print(9//2)
print(9.0//2)
print(9//2.0)
print(9.0//2.0)


print(3//7)#while working with floor division operator, if numerator is less than denominator, result will be 0.



print(9%2)
print(3%7)#while working with modulus division, if the numerator is less than denominator, then the output always will be numerator.



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#working with relational or comparision operators(>,<,>=,<=,==,!=)# these operators will be comparing one operand with another operand and produce a bool (TRUE OR FALSE) result
print(3>2)
print(3<2)
print(3>=2)
print(3<=2)
print(3==2)
print(4==4)
print(3!=2)
print(3!=3)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Working logical operators(logical AND operator(and),logical OR operator(or), logical NOT operator(not))
'''
and: if one or both of the values are false, the output will be false.
or: if both values of the or logical operator are false, then the output will be false.
not:(compliment operator): 
'''
#AND
print(7>6 and 9!=8) 
print(8==8 and 9!=9)
print(9==8 and 5!=100)
print(9!=9 and 0>0)
#OR
print(5>1 or 2<7)
print(5>1 or 2>7)
print(5<1 or 2<7)
print(5<1 or 2>7)
#NOT compliment operator
print(not(3>2))
print(not(9==9 and 8!=7 and 3>=2))#if "and", "or", and "not" operators are used more than once in the same expression, then it is called as chaining of operators.
print(not(3>2 and 4>3 or 5<2))

#Working with assignment operators(+=,-=,*=,//=,%=,**=,=)
m = 10
n = m
p = m*n+2*n
a = 2
a+=5 #means a = a+5
print(a)
a //= 2 # a = a/2 floor division --> (no decimal)
print(a)
p = 3
p**=2 # p = 3^2
print(p)
p%=2
print(p)
b = 2
b-=3
print(b)
b*=2
print(b)
#Working with membership operators(in,not in)
list = [10,11,12,13,14,15]

print(10 in list)
print(20 in list)

print(10 not in list)
print(20 not in list)


'''
An operator is a special symbol that is used to perform operation on operands.
2+3---> here, 2 and 3 are operands.
a = 10
b = 20
a*b--> here, a and b are operands.
An operand can be a variable or can be a value.
Python supports various operators such as:
1) Arithimetic operators
2) Relational or comparision operators
3) Logical operators
4) Assignment operators
5) Membership operators
-
6) Identity operators
7) Bitwise operators
-
'''
#commented above

