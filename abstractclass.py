from abc import ABC,abstractmethod
class abstractclass(ABC):
    def print(self,x):
        print("Value= ",x)

    @abstractmethod
    def task(self):
        print("We are inside abstract task")

class testclass(abstractclass):
    def task(self):
        print("We are inside test_class task")

object1=testclass()
object1.task()
object1.print(100)