class Student:
    school= "Ostad"
    # def yo(self):
        # print("YO!")
    @classmethod
    def change_school(cls):
        cls.school="Online Resource"
    def yo(self):
        print("YO!")  #Object Method /Instance Method

    def show_name(self):
        print(self.name)      #Object Method /Instance Method
    # def yo(self):
        # print("YO!")


s1=Student()
s2=Student()


# s1.name="Abu MOslem"
print(Student.school)
print(s1.school)
# s1.yo()
# s2.yo()
# print(s1.name)
print(s2.school)




s1.school="XYZ"
print(s1.school)
print(s2.school)

Student.school="ABC"
print(s2.school)
print(s1.school)
Student.change_school()
print(s2.school)
print(s1.school)