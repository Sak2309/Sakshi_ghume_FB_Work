#without changing origal chages functionality
def demo(fun):
    print("this is demo..")
    print("next line")
    fun()
    print("end of demo")

def great():
    print("good morning")

demo(great)