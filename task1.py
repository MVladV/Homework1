# task1

import sys # pass the list of arguments from the console

try:
    print(eval(' '.join(sys.argv[1]+sys.argv[2]+sys.argv[3]))) # calculation of mathematical expression
except Exception:
    print("Exeption!")
