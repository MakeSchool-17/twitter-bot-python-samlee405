from __future__ import print_function

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        if self.head == None:
            return 0
        else:
            length = 1

            node = self.head
            while node.next != None:
                length += 1
                node = node.next

            return length

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        length = self.length()

        if length == 0:
            self.head = Node(item)
            self.tail = Node(item)
        else:
            node = self.head
            while node.next != None:
                node = node.next

            node.next = Node(item)
            self.tail = Node(item)

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        length = self.length()
        node = Node(item)

        if length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        previousNode = None
        currentNode = self.head

        while currentNode != None:
            if currentNode.data == item:
                if (previousNode == None) and (currentNode.next == None): # Item is the only item in the linked list
                    self.head = None
                    self.tail = None
                    return

                if previousNode == None: # Item is found in the first node and no previous node exists

                    self.head = currentNode.next
                    return

                if (previousNode != None) and (currentNode.next != None): # Item is not on either extremity
                    previousNode.next = currentNode.next
                    return

                if (currentNode.next == None): # Item is found in the last node.
                    previousNode.next = None
                    self.tail = previousNode
                    return

            previousNode = currentNode
            currentNode = currentNode.next

        raise ValueError("Item not found")


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        currentNode = self.head

        while currentNode != None:
            if quality(currentNode.data):
                return currentNode.data

            currentNode = currentNode.next

        return None

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    # test_linked_list()

    ll = LinkedList()
    ll.append('A')
    ll.append('B')
    ll.append('C')
    ll.delete('C')
    print(ll)
