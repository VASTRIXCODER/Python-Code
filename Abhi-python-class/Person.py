class Person:
    counter = 0
    def __init__(self,name):
        self.name = name
        Person.counter += 1 #Means Person.counter = Person.counter + 1
    @staticmethod # @staticmethod is a decorater used to create static functions or methods
    def getPersonObjectCount():
        return Person.counter
person1 = Person("JaQuavion")
person2 = Person("BonQueQue")
person3 = Person("DeShawn")
person4 = Person("Taquavion")
objectCounter = Person.getPersonObjectCount()
print("Total numeber of objects or instances created for our 'Person' class:",objectCounter)
print("Name of Objects:",person1.name,',',person2.name,',',person3.name,',',person4.name)
#for fun!
#print("🥶🦧🫡🦾💰😇🙂🤣😎")
'''
In this example, We have created a 'Person' Class a static variable 'counter' to track the number of instances or objects and a static method
'getPersonObjectCount()' to return counter value[means how many objects or instances were created for the class which will be determined through Person.counter+=1
inside constructer block]




'''

