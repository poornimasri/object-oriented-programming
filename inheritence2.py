class person(object):
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number

    def display(self):
        print(self.name)
        print(self.id_number)

class employe(person):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,id_number)

object1=employe("Rahul",90010,200000,"intern")
object1.display()

        