# python numerid data  types
# out1 = 1  # int data type
# out2 = True # bool data type 
# out3 = 10.235 # float data type
# out4 = 10+3j  # complex data type
# print("the type of variable habing value ",out1,"is",type(out1))
# print("the type of variable habing value ",out2,"is",type(out2))
# print("the type of variable habing value ",out3,"is",type(out3))
# print("the type of variable habing value ",out4,"is",type(out4))


# string data types 

# str='dilkhush kumar'
# print(str)  # prints complere string
# print(str[0]) # prints first character of the string
# print(str[2:5]) #print characters starting from 3rd to 5th 
# print(str[2:])  # print string starting from 3rd character
# print(str * 2)  # print string two times
# print(str + "dil happy") # print concatenated string


# python sequence data types
# list data type
# Tuple data type
# Range data type


# python List data type
# list=['abcd',654, 23.43, 'dilkhush', 70.34]
# tinylist=[123,'kumar']
# print(list)  # prints complere list
# print(list[0]) # prints first character of the list
# print(list[1:5]) #print characters list from 2rd to 3th 
# print(list[2:])  # print list starting from 3rd character
# print(list * 2)  # print list two times
# print(list + tinylist) # print concatenated list



# tuple data type
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')

# print (tuple)               # Prints the complete tuple
# print (tuple[0])            # Prints first element of the tuple
# print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
# print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
# print (tinytuple * 2)       # Prints the contents of the tuple twice
# print (tuple + tinytuple)   # Prints concatenated tuples



# range data types
# for i in range(10):
#   print(i)


# for i in range(2,10):
#   print(i)


# for i in range(1,10,2):
#   print(i)



# dictionary data type
# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"

# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


# print (dict['one'])       # Prints value for 'one' key
# print (dict[2])           # Prints value for 2 key
# print (tinydict)          # Prints complete dictionary
# print (tinydict.keys())   # Prints all the keys
# print (tinydict.values()) # Prints all the values


# set data type
# set1 = {123, 452, 5, 6}
# set2 = {'Java', 'Python', 'JavaScript'}

# print(set1)
# print(set2)
# print(type(set1))



# boolean data type

# a= 2
# b=4
# # Following also prints the same
# print(a==b)
# # Returns False as a is None
# a = None
# print(bool(a))
# # Returns false as a is an empty sequence
# a = ()
# print(bool(a))
# # Returns false as a is 0
# a = 0.0
# print(bool(a))
# # Returns false as a is 10
# a = 10
# print(bool(a))


# data types conversion 

print("Conversion to integer data type")
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int("55")   # c will be 3

print (a)
print (b)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

print("Conversion to string")
a = str(1)     # a will be "1" 
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)