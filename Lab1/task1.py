# task1

# pass the list of arguments from the console
import sys 
# calculation of mathematical expression
try:
    print(eval(' '.join(sys.argv[1]+sys.argv[2]+sys.argv[3]))) 
except Exception:
    print("Exeption!")
