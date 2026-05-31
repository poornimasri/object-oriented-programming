class myclass:
    __privar=27
    def __prineth(self):
        print("I am inside my class")

    def hello(self):
        print("private variable value=",myclass.__privar)

object1=myclass()
object1.hello()
object1.__prineth
        