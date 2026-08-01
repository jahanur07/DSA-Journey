import queue

stack=queue.LifoQueue()
stack.put(9)
stack.put(7)
print(list(stack.queue))
stack.get()
print(list(stack.queue))