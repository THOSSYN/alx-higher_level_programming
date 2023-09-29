#!/usr/bin/python3
"""Defines a node of a singly linked list"""


class Node:
    """Represents a Node object from the class"""

    def __init__(self, data, next_node=None):
        """
        Initializes an object instance of a class

        Args:
            data (int): The data part of the node
            next_node: is the link to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets or retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets value to data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Gets or retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets value to next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the LinkedList instance"""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
        list (increasing order)

        Args:
            value: Is the value of the data part of node
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            cur = self.head
            while cur.next_node is not None and isinstance(cur.next_node, Node) and value >= cur.next_node.data:
                cur = cur.next_node
            new_node.next_node = cur.next_node
            cur.next_node = new_node

    def __str__(self):
        """Prints the entire linked list"""
        nodes = []
        cur = self.head
        while cur is not None:
            nodes.append(str(cur.data))
            cur = cur.next_node
        return "\n".join(nodes)
