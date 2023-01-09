class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.deque = []  
        self.k = k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque = [value] + self.deque
            return True
        return False


        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        return False
        
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        return False
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        return False
        

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.deque) > 0:
            return self.deque[0]
        return -1
        

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.deque) > 0:
            return self.deque[-1]
        return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.deque) == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.deque) == self.k
        

