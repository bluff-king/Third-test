class Node:
 def __init__(self,v):
  self.value = v
  self.next = None 

def InsertFirst(h, v):
 # create a new node having value v
 # insert this new node to the first position of the list 
 # h: pointer/reference to the first node of the inputl list 
 # return the pointer/reference to the first node of the resulting list 
 nod = Node(v)
 nod.next = h # let nod.next point to the same location as h  
 return nod # nod will be the pointer/reference to the first node (element) of the resulting list 

def PrintList(h):
 # h is the pointer/reference to the first element of the input linked list 
 # print the values of all elements of the linked  list to stdout 
 p = h 
 while p != None:
  print(p.value, end = ' ')
  p = p.next
  
 print('')
 
def InsertLastRecursive(h, v):
 nod = Node(v)
 if h == None:
  return nod 
 h.next = InsertLastRecursive(h.next,v)
 return h 

def Find(h, v):# return a poitner to the node having value v in the list headed by h 
 p = h 
 while p != None:
  if p.value == v:
   return p
  p = p.next 
 return None

 
def InsertAfter(h, u, v):
 # create a new node having value u 
 # insert this new node right-after the node having value v in this list headed by h 
 # return the pointer/reference to the first node of the resulting list 
 # support values must be all-different 
 q = Find(h, u) 
 if q != None:# the node having value u exists, do not insert one more 
  return h 

 p = Find(h,v) 
 if p == None: #  the node having value v does not exist, do not insert 
  return h  
 
 q = Node(u) # create node: allocate memory, assign values 
 q.next = p.next 
 p.next = q 
 return h  
 
h = None 
'''
h = InsertFirst(h,1)
h = InsertFirst(h,2)
h = InsertFirst(h,3)
h = InsertFirst(h,4)
'''
for v in range(1,11):
 h = InsertLastRecursive(h,v) #InsertFirst(h,v) 
 
PrintList(h)  
h = InsertAfter(h, 11, 9)
PrintList(h) 