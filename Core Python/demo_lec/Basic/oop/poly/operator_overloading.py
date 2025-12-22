class Time:
    
    def __init__(self,m,s,h):

        self.m=m
        self.s=s
        self.h=h
    
    def __add__(self, other):

        s = self.s + other.s 
        m = s // 60
        s = s % 60
    
        m = m + self.m + other.m
        h = m // 60
        m = m % 60

        h = h + self.h + other.h 

        return f'{h} : {m} : {s}'

t1 = Time(10,45,30)
t2 = Time(5,25,40)
print(t1 + t2)
        