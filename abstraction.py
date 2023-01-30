from abc import ABC, abstractclassmethod


# abstract class
# has a method/fun whose definition is given in child
class Department:
    salary = 100000

    @abstractclassmethod
    def departmentInfo(self):
        pass

    @abstractclassmethod
    def newAbs(self):
        pass

    def newFun(self):
        print("another function")

class Marketing_department(Department):
    salary = 2000

    def departmentInfo(self):  # must be implimented to create an object
        print("implimented in child class")

    def newAbs(self):
        print("new abstract method")
    
    def newFun(self):
        print("another function")
class Hr(Marketing_department):
    # inherited marketing_depart which has already implimented the abs functions
    # so no need to impliment again the abfuns
    pass


md1 = Marketing_department()
md1.departmentInfo()
md1.newFun()

hr = Hr()

