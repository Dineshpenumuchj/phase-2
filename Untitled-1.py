"""class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printPreorder(root):
    if root==None:
        return
    print(root.data)
    printPreorder(root.left)
    printPreorder(root.right)

def printinorder(root):
    if root==None:
        return
    printinorder(root.left)
    print(root.data,end=",")
    printinorder(root.right)

def printpostorder(root):
    if root==None:
        return
    printpostorder(root.left)
    printpostorder(root.right)
    print(root.data,end=",")
obj1=Node(100)
obj2=Node(21)
obj3=Node(-151)
obj4=Node(87)
obj5=Node(12)
obj6=Node(52) 
obj7=Node(8)
obj8=Node(27)
obj9=Node(28)
obj10=Node(7)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10

printPreorder(obj1)
print()
printinorder(obj1)
print()
printpostorder(obj1)
print(5)"""

"""class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printLevelorderTraversal(root):
    if root==None:
        return
    Q=[root]
    result=[]
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        for i in range (n):
            currNode=Q.pop(0)
            subResult.append(currNode.data)
            if currNode.left!=None:
                Q.append(currNode.left)
            if currNode.right!=None:
                Q.append(currNode.right)  
            result.append(subResult)
    print(result)
obj1=Node(100)
obj2=Node(21)
obj3=Node(-151)
obj4=Node(87)
obj5=Node(12)
obj6=Node(52) 
obj7=Node(8)
obj8=Node(27)
obj9=Node(28)
obj10=Node(7)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10

printLevelorderTraversal(obj1)"""
 #level order traversal
"""class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printLevelOrderTraversal(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to subResult)
            subResult.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)    
 
    print(result)
 
def printLeftView(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to result)
            if i == 0:
                result.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
    print("Left view is:", result)
 
def printRightView(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1 (Deleting)
            currNode = Q.pop(0)
 
            # step-2 (Appending to result)
            if i == n - 1:
                result.append(currNode.data)
 
            # step-3 (Enquing the left child)
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step-4 (Enquing the right child)
            if currNode.right != None:
                Q.append(currNode.right)
 
    print("Right view is:", result)
 
#      12 
#     5  8 
#   -1 2   89
obj1 = Node(12)
obj2 = Node(5)
obj3 = Node(8)
obj4 = Node(-1)
obj5 = Node(2)
obj6 = Node(89)
obj1.left = obj2
obj1.right = obj3 
obj2.left = obj4
obj2.right = obj5
obj3.right = obj6
 
# printPreorder(obj1)
# print()
# printInorder(obj1)
# print()
# printPostorder(obj1)
# print()
 
printLeftView(obj1)
printRightView(obj1)"""

"""class TreeNode:
    print(root.val,end=",")
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def printinorder(root):
    if root==None:
        return
    printinorder(root.left)
    printinorder(root.right)

def insertIntoBST(root,val):
    if root==None:
        return TreeNode(val)
    elif root.val>val:
        root.left=insertIntoBST(root.left,val)
    else:
        root.right=insertIntoBST(root.right,val)
    return root
        
nums = [10, 8, 12, 5, 23, 20]
root = None
for ele in nums:
    root = insertIntoBST(root,ele)
printinorder(root)"""

#delete Node in BTS
"""class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def printinorder(root):
    if root==None:
        return
    printinorder(root.left)
    print(root.val,end=",")
    printinorder(root.right)

def insertIntoBST(root,val):
    if root==None:
        return TreeNode(val)
    elif root.val>val:
        root.left=insertIntoBST(root.left,val)
    else:
        root.right=insertIntoBST(root.right,val)
    return root
def deletedNodeFromBST(root,val):
    if root==None:
        return None
    elif root.val>val:
        root.left=deletedNodeFromBST(root.left,val)
    elif root.val<val:
        root.right=deletedNodeFromBST(root.right,val)
    else:
        if root.left==None and root.right==None:
            return None
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
         
        curr=root.right
        while curr.left!=None:
            curr=curr.left
             
        root.val=curr.val
        root.right=deletedNodeFromBST(root.right,curr.val)
    return root

nums = [10, 8, 12, 5, 23, 20]
root = None
for ele in nums:
    root = insertIntoBST(root,ele)
printinorder(root)
print()
root=deletedNodeFromBST(root,20)
printinorder(root)"""

# Adjacency Matrix
 """n, m = map(int, input().split())
 matrix = []
 for i in range(n):
     row = [0] * n 
      [0, 0, 0, 0, 0]
     matrix.append(row)
 
 print(matrix)  
 for i in range(m):
     u, v = map(int, input().split())
     matrix[u][v] = 1 
     matrix[v][u] = 1  
  print(matrix)
 
 
# Adjacency List Construction 
n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
print(adj)
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
print(adj)"""
 
 
 
def initiateBFSTraversal(node, visited, adj, result):
    Q = [node]
    visited[node] = True 
 
    while len(Q) > 0:
        curr = Q.pop(0)
        result.append(curr)
        for neighbour in adj[curr]:
            if visited[neighbour] == False:
                visited[neighbour] = True 
                Q.append(neighbour)
 
 
def printBFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateBFSTraversal(node, visited, adj, result)
 
    print("BFS traversal is: ", result)


n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
printBFSTraversal(adj, n)
























