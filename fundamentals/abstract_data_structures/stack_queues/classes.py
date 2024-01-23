class stackClass:

	def __init__(self):
		self.stack = []
	
	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		return False
	
	def push(self, element):
		self.stack.append(element)

	def pop(self):
		if not self.isEmpty():
			return self.stack.pop()
		

class queueClass:

	def __init__(self):
		self.queue = []
	
	def isEmpty(self):
		if len(self.queue) == 0:
			return True
		return False
	
	def enqueue(self, element):
		self.queue.append(element)
	
	def dequeue(self):
		if not self.isEmpty():
			return self.queue.pop(0)