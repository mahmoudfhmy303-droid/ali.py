class Student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade


    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_grade(self):
        return self.grade    

s1 = Student("Ali Ahmed", 2501123, 15)

print("Name:", s1.get_name())
print("ID:", s1.get_id())
print("Grade:", s1.get_grade())