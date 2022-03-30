class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
#Linked List object which is made up of Node objects        
class LinkedList: 
    def __init__(self):
        #Set head to the first Node object
        self.head = ListNode()
    #insert function to add new Nodes to list
    def insert(self, data):
        new_node = ListNode(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    #performs an insert of data into the respected place in the list rather then at the end by default
    def sortedInsert(self,data):
        if not self.head.next:
            self.insert(data)
        new_node = ListNode(data)
        #handles if the new node is larger then the first data node *discount dummy head*
        if self.head.next.data > new_node.data:
            new_node.next = self.head.next
            self.head.next = new_node
        curr = self.head.next
        while curr.next != None:
            if new_node.data < curr.next.data:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
        if curr.data < new_node.data:
            new_node.next = curr.next
            curr.next = new_node

    #delete a specific node from the list
    def delete(self, data):
        #if list is empty just return
        if not self.head.next:
            return
        curr = self.head.next
        prev = None
        while curr.next != None:
            if curr.next.data == data:
                prev = curr
                curr = curr.next
                prev.next = curr.next
                curr.next = None
                return
            curr = curr.next
        #if we didn't break out of function then we didn't find it
        print("The node with the data ", data, " doesn't exist in this list")

    #Return the length of the List
    def length(self):
        curr = self.head.next
        total = 1
        while curr.next != None:
            total += 1
            curr = curr.next
        return total

    #display List
    def printList(self):
        nodeList = []
        curr = self.head.next
        while curr != None:
            nodeList.append(curr.data)
            curr = curr.next
        print (nodeList)

    #HELPER FUNCTION: GET MIDDLE NODE
    def getMid(self,head) -> ListNode:
        if not head:
            return head
        slow, fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    #HELPER FUNCTION: MERGE TWO LINKED LISTS:
    def merge(self,l1,l2):
        curr = dummy = ListNode()
        while l1 and l2:
            if l1.data <= l2.data:
                curr.next = l1
                l1 = l1.next if l1.next else None
            else:
                curr.next = l2
                l2 = l2.next if l2.next else None
            curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return dummy.next

    def sortList(self): 
        if self.head:
            self._sortList(self.head)
    
    def _sortList(self, head):
        #base case
        if not head or not head.next:
            return head
        #splitting list in two halves    
        #utilizing a helper function to get the middle node of the list
        middle = self.getMid(head)
        temp = middle.next
        middle.next = None
        middle = temp
        #now we wanna recurse to break each node to individual nodes from left to right
        left = self._sortList(head)
        right = self._sortList(middle)
        #now we need to merge the two left and right nodes using another helper function
        sortedList = self.merge(left,right)
        return sortedList

    def mergeTwoLists(self,l2):
        if self.head and self.head and l2 and l2.next:
            self._mergeTwoLists(self.head,l2)
        
    def _mergeTwoLists(self, h1,h2):
        dummy = ListNode()
        if not h1 and h2:
            return h2
        if not h2 and h1:
            return h1
        if not h1 and not h2:
            return
        l1 = self._sortList(h1)
        l2 = self._sortList(h2)
        dummy.next = self.merge(l1.next,l2.next)
        return dummy.next

    def reverseList(self):
        if self.head and self.head.next:
            self.head.next = self._reverseList(self.head.next)
            return self.head
    def _reverseList(self,h):
        if not h:
            return h
        curr = h
        prev = None
        next = curr
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    #function to determine if linked list is a palindrome
    def isPalindrome(self):
        if not self.head.next:
            return True
        left = self.head.next    
        middle = self.getMid(self.head.next)
        temp = middle.next
        right = self._reverseList(temp)
        while (right != None):
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True

    def rotate(self, k):
        if self.head:
            self._rotate(k)
    
    def _rotate(self,k):
        #Edge case is that if k == 0 then theres no rotations needed
        if k == 0:
            return self.head
        #We need to get the end node of the list aka the tail for later
        tail = self.head
        length = self.length()
        while tail.next:
            tail = tail.next
        #using our length function we can also get length for later use
        #since my length function starts at zero we wanna increment one more time cause we technically
        #start at the 1th node but we have to ignore the dummy header
        #We do this cause if k which is how many rotations is the same or longer then the list
        #we need to mod it because if k == length then no need to rotate 
        #Or if k > length we need to mod to get the remainder to determine the rotations
        k %= length
        if k == 0:
            return self.head
        #start iterating again till you get to the kth node
        cur = self.head.next
        #This essentially gets us to the kth node at the end of the list
        for i in range(length-k-1):
            cur = cur.next
        new_head = cur.next
        tail.next = self.head.next
        self.head.next = new_head
        cur.next = None


