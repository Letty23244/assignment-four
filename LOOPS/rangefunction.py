#rangefunction
#range()[iterates through squences] for loops
#particular range of squence :lists, string
name = "birungi"
for item in name:
    print(item)

Marks =[60, 70,80]
for mark in Marks:
    print(mark)

#using a function
def total_marks():
    marks = [60,70,80]
    sum = 0
    for mark in marks:
        sum += mark
    print(f"the total_marks is:{sum}")
total_marks()    

#Ranges is a function taking in a parameter ie
#range(start, stop,step)
#basic examples
# using a loop print all  numbers from 0 to 6
for num in range(7):
    print(num)
   # 1 to 10 
for num in range(11):
    print(num)

#print numbers from 1 to 20
for num in range( 1 ,21):
    print(num)

#print the  following range of even numbers (2,4,6,8,10)
def even_numbers():
    for num in range(2,11,2):
        print(num)
even_numbers()

#print the following range of odd numbers
def odd_numbers():
    for odd in range(1,12,1):
        print(odd)
odd_numbers() 

#lists and turples
# similarity both are ordered both are indexed
#difference lists are mutable and turples are unmutable 
# lists use[]while turples()
products = ['pen' ,'pencil' ,'books']
color =('red', 'green','pink')
# add rubber to the product list
products.append('rubber')
print(products)

products.insert(3,'ruler')
print(products)

# display the length
len(products)
print(len(products))

#add purple to the color


new_colors =list(color) 
print(type(new_colors)) 

new_colors.append('purple')
print(new_colors)
#coverting the list back to a turple
color =tuple(new_colors)
print(color)
    
fruits = ('apple',) # incase it has one name we use a comma 
print(fruits , type(fruits))   

#SETS
#Immutable
#unorder
#syntax of set they use {}

#Dictionaries
#key value pair
#syntax
# keys can be type int string and float they cannot use lists turples
student={
    'name ':'Gillian' ,'age':22, 'location':'muyenga'
}
print(student)
fruits={1:"apple",2:"orange",3:"banana"}
print(fruits)