"""Single unit Linked List"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

"""Head element is the first element in the list"""
class LinkedList(object):
    def __init__(self, head=None):
        self.head  = head

    def append(self, new_element):
        """
        Again, this part is really important, so don't rush through it.
         Take the code line-by-line and make sure everything makes sense.
          If the LinkedList already has a head, iterate through the next 
          reference in every Element until you reach the end of the list. 
          Set next for the end of the list to be the new_element.
           Alternatively, if there is no head already, you should just 
           assign new_element to it and do nothing else.
        """
        current = self.head # current element

        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else: 
            self.head = new_element

            class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next