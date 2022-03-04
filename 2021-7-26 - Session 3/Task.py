e = 2.718281828459045
pi = 3.141592653589793
gravity = 9.8
k = 9*10**9
plank = 6.63e-34  # OR 6.63*(10**-34)


def printeven (listname) :
    for i in listname :
        if type(i) == int and i%2 == 0 :
            print(i)

            
def searchforelement (listname,element) :
    for i in listname :
        if i == element :
            return True
        elif type(i) == list :
            for j in i :
                if j == element :
                    return True
    
    return False


def mathoperations () :
    z = input("Please choose the operation {+,-,*,/} :")
    if z not in ["+","-","*","/"] :
        print("You enter unknown operation")
        return None
    
    x = float(input("Please enter the first number :"))
    y = float(input("Please enter the second number :"))
    
    if z == "+" :
        R = x + y
    elif z == "-" :
        R = x - y
    elif z == "*" :
        R = x * y
    elif z == "/" :
        R = x / y

    print("Result =",x,z,y,"=",R)


class Constant(object):
    __slots__ = ()
    pi = 3.14
        
class Const:
    def get(self):
        self.__pi = 3.14
        print ("pi = " + str(self.__pi))
