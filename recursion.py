class Node(object):
    """ Node for a linked list """

    def __init__(self, data):
        """ Create a node instance with no next node"""

        self.data = data
        self.next = None

    def __repr__(self):

        return "<Node: {data}>".format(data=self.data)

    def add_node(self, node):
        """ Add a next node to this node"""

        self.next = node

    def traverse_recursively(self):
        """Traverse a Node's path recursively and print out each node's data.

        >>> apple = Node("apple")
        >>> berry = Node("berry")
        >>> cherry = Node("cherry")
        >>> apple.add_node(berry)
        >>> berry.add_node(cherry)
        >>> apple.traverse_recursively()
        apple
        berry
        cherry

        """
     
        if self.data is None:
                return 
        if self.data is not None:
            #print self.data
            return self.data
        return traverse_recursively(self.next)


    ### I don't understand why this is only returning apple. When I take away the return and put print - it then says traverse_recursively is undefined? WHY?!Looking at the 
    ### demo it seems like this should work 
        pass


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
