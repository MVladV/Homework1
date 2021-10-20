import sys
import os.path

class Node:
   def __init__(self, code, price):
      self.left = None
      self.right = None
      if not isinstance(code, int):
            raise TypeError()
      elif not isinstance(price, int):
            raise TypeError()
      else:
        self.code = code
        self.price = price

# Insert Node
   def insert(self, code, price):
      if self.code:
         if code < self.code:
            if self.left is None:
               self.left = Node(code, price)
            else:
               self.left.insert(code, price)
         elif code > self.code:
            if self.right is None:
               self.right = Node(code, price)
            else:
               self.right.insert(code, price)
      else:
         self.code = code

# Print the Tree
    
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(f'{self.code} - {self.price}')
      if self.right:
         self.right.PrintTree()

# Find element 
             
   def find(self, num):
        if num < self.code:
            if self.left is None:
                print("Not Found")
            return self.left.find(num)
        elif num > self.code:
            if self.right is None:
                print("Not Found")
            return self.right.find(num)
        else:
            return self.price        
            

# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.code)
         res = res + self.inorderTraversal(root.right)
      return res

class main:
    try:
        root = Node(27, 450)
        root.insert(14, 9450)
        root.insert(35, 5530)
        root.insert(10, 4502)
        root.insert(19, 43250)
        root.insert(31, 4450)
        root.insert(42, 1450)
        print(root.inorderTraversal(root)) 
        print("All tree:\n")
        root.PrintTree()
        code = int(input("Code of element: "))
        num = int(input("Number of elements: "))
        price = int(root.find(code))
        result = num * price 
        print(f'Result: {result}')
    except Exception:
        print("Exeption!")
main()       

