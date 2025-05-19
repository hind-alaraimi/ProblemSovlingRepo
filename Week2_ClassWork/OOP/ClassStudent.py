class Student:
    def __init__(self,name,marks):
        self._name = name
        self.__marks = marks
    # Getter:
    def get_name(self):
        return self._name
    #Setter:
    def set_name(self,nname):
        self._name = nname

    def _displayStudent(self):
        return (f"Name: {self._name} - Mark: {self.__marks}")
    
s1 = Student("Hala",80)
print(s1._displayStudent())
s1.set_name("Mohammed")
print(s1.get_name())
