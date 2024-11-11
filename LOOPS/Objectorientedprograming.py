#oop(object oriented programing)
#it always has a class and object
#a class always has properties/attributes
# objects come from class
# methods are action of the class

#syntax of oop
#creating a class
#cohort class

    #Name
    #description
    #start_date
    #end_date
    #total_student
# within the cohort class 
# # add a constructor for the cohort class
# add a method to the class that print the cohort name and the total number of students
# create a new insistance of the cohort    

class Cohort:
  def __init__(self, name, description,start_date,end_date):
      self.name=name
      self.description =description
      self.start_date =start_date
      self.end_date =end_date
cohort4 = Cohort("leticia", "student at witu","20/8/2024" ,"25/06/2026")
print(cohort4.name)
print(cohort4.description)
print(cohort4.start_date)
print(cohort4.end_date)

#b
class cohort:
   def __init__(self, cohort_name, total_number_of_student):
       self.cohort_name=cohort_name
       self.total_number_of_student= total_number_of_student
   def myfun(self):
      print("the cohort name is " + self.cohort_name +" total number of student is " + str(self.total_number_of_student))
d=cohort("cohortfour" ,57)       
d.myfun()  

#c
class Cohort_five:
  def __init__(self, name, description,start_date,end_date ):
      self.name=name
      self.description =description
      self.start_date =start_date
      self.end_date =end_date
    
cohort4 = Cohort("dorcus", "student at witu","20/8/2025" ,"25/06/2027")
print(cohort4.name)
print(cohort4.description)
print(cohort4.start_date)
print(cohort4.end_date)

          
      
      
   