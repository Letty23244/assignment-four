#Dictionaries
#key value pair
#syntax
# keys can be type int string and float they cannot use lists turples
student={
    'name':'Gillian' ,'age':22, 'location':'muyenga'
}
print(student)
print(student['name'])
print(student['age'])
print(student['location'])

fruits={1:"apple",2:"orange",3:"banana"}
print(fruits)
#print the keys of the student dictionary
student.keys()
print(student.keys())

#print the length pf the dictionary
len(student)
print(len(student))

#add a key contact to the student dictionary
student['contact'] ='0750767890'
print(student)

#update the student name gillian to Apio Gillian
student['name'] ='Apio Gillian'
print(student)
#print all the student valuesof the dictionary
print(student.values())

# remove the contact key from the dictionary
#we can use delete remove and pop to remove a key from the dictionary
student.pop('contact')
print(student)
