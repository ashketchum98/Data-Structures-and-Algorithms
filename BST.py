class Node:
	def __init__(self,data=None):
		self.data=data
		self.lchild=None
		self.rchild=None

class BST:
	
	def __init__(self):
		self.root=None

	def search(self,root,item):

		if root==None:
			return 0

		elif root.data==item:
			return 1

		if root.data<item:
			return a.search(root.rchild,item)

		else:
			return a.search(root.lchild,item)

	def insert(self,root,data):
		
		pos = a.search(self.root,data)

		if pos==1:
			print("Value exists !!! Try another")

		else:
			if self.root==None:
				self.root=Node(data)

			elif root.data<data:
				if root.rchild==None:
					root.rchild=Node(data)
				else:
					a.insert(root.rchild,data)

			else:
				if root.lchild==None:
					root.lchild=Node(data)
				else:
					a.insert(root.lchild,data)

	def traverse(self,root):
		if root==None:
			return
		else:	
			a.traverse(root.lchild)
			print(root.data)
			a.traverse(root.rchild)

a= BST()
ch='y'
while ch=='y':
	print("Menu")
	print("1 : Search")
	print("2 : Insert")
	print("3 : Traverse")
	choice=int(input("Enter your choice : "))
	if choice==2:
		item=int(input("Enter data to be inserted : "))
		a.insert(a.root,item)
	elif choice==1:
		data=int(input("Enter data to be Searched : "))
		pos=a.search(a.root,data)
		if pos==1:
			print("Value found")
		else:
			print("Value not Found")
	elif choice==3:
		a.traverse(a.root)
	else:
		print(" !!! Wrong choice !!!")

	ch=input("Do you want to continue : (y/n) ")	                          



