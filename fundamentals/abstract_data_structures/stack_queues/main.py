from classes import stackClass, queueClass

def main():

	print("running...")

	nameStack = stackClass()
	print(nameStack.pop())	
	nameStack.push('Andy')
	nameStack.push('Ian')
	nameStack.push('Nate')
	nameStack.push('Päherdin')
	print(nameStack.pop())


	nameQueue = queueClass()
	print(nameQueue.dequeue())
	nameQueue.enqueue('Andy')
	nameQueue.enqueue('Ian')
	nameQueue.enqueue('Nate')
	nameQueue.enqueue('Päherdin')
	print(nameQueue.dequeue())

if __name__ == '__main__':
	main()