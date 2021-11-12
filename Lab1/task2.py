# task2

# pass the list of arguments from the console
import sys 
# function for the amount
def add(a, b): 
    return a + b
# function for the difference
def diff(a, b): 
    return a - b
# function for share    
def div(a, b): 
    return a / b
# function for multiplication    
def mult(a, b): 
    return a * b    

try:    
    s2 = ' ,:@.-()/'
    if(sys.argv[1]=="add"):
        print(add(int(sys.argv[2]),int(sys.argv[3])))
    elif(sys.argv[1]=="diff"):
        print(diff(int(sys.argv[2]),int(sys.argv[3])))
    elif(sys.argv[1]=="div"):
        print(div(int(sys.argv[2]),int(sys.argv[3])))
    elif(sys.argv[1]=="mult"):
        print(mult(int(sys.argv[2]),int(sys.argv[3])))        
except Exception:
    print("Exception!")   