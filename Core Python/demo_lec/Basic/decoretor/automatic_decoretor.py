def decoretor(fun):
    #print("this is drcoretor")
    def wrapp():
        print("wrapper function")
        fun()
        print("end wrapper function")
    return wrapp

@decoretor
def great():
    print("Good morning")

great()