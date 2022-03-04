gravity = 9.8
e = 2.7
k = 9*10**9
plank = 6.63e-34

def divide(x,y) :
    z = x / y
    print(z)
    
def find (List , element) :
    for i in range (0,len(List)) :
        if List[i]==element :
            print("Element is found")

def add (List,element) :
        if element not in List :
            List.append(element)
            print("Element is added")
            print(List)
        else :
            print("Element is already in the list")
