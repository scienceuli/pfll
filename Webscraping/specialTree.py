# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 01:43:16 2018

@author: Maame Yaa Osei and Ariel Arman Woode
"""

import json

writeFile = open('myjson.json', 'w')


class Node:
    """
     A Node class used to build a specialised tree. Each node holds data on its children,
     the data to be inserted under every heading and the current path to insert new nodes/
     data into.
    """

    def __init__(self, title):
        """
        The constructor for the node class. this creates an empty node.

        :param title: The name or heading by which to identify the given node.
        """
        self.children = {}                  # Dictionary holding all logical children of the given node
        self.title = title                  # The heading of the given node.
        self.level = 0                      # The nodes destined level. to be calculated using count of #.
        self.latest = None                  # The latest node to be added to a given node's children.
        self.data = None                    # The data, or lines, that go under the given heading.

    def setChild(self, child):
        """
        Method used to set new child of a node.

        :param child: The child to be set for a given node
        """
        self.children[child] = child.data
        self.latest = child

    def __str__(self, depth=0):
        """
        String method to print a node

        :param depth: The depth of a given node
        :return: Returns string representation of a node
        """

        ret = ""
        ret += '\t' * depth + '{' + str(self.title) + ":" + '\n' + str(self.data) + '\n'
        for node in self.children:
            ret = node.__str__(depth=depth + 1)

        return ret


class Tree:
    def __init__(self):
        """
        Constructor for a tree class. This creates a specialised tree and initializes a root node.
        """
        self.root = Node('tree')
        self.dict = {}

    def recurse_insert(self, parent, root, pair):
        """
        Method to insert a node into tree appropriately using recursion. This method works
        by using the level of the heading (# count) to determine where to place a new node.
        The insertion location is decided by a `latest` variable that keeps track of the latest node,
        and thus the logical parent of the new node.

        :param parent: Holds reference to the dictionary to be converted to a json
        :param root: Holds reference to current node
        :param pair: A tuple containing a key value pair to be used in creating nodes and node data
        :return: Returns the root of the tree.
        """
        key = pair[0]                       # The key or heading to be added.
        c = key.count("#")                  # The current heading level.

        # Base case. This is where a new node is created and added to the tree.
        if root is None:
            key = key.replace('#', '')[:-2] # Formatting key.
            newNode = Node(key)
            newNode.level = c
            root = newNode
            root.data = pair[1]

            # Adding new data to final dictionary.
            parent[key] = {}
            parent[key]['values'] = root.data
            return root
        else:
            if c > root.level:
                if root.latest is None:
                    root.setChild(self.recurse_insert(parent, None, pair))
                else:
                    if c == root.latest.level:
                        root.setChild(self.recurse_insert(parent, None, pair))

                    elif c > root.latest.level:
                        parent = parent[root.latest.title]
                        (self.recurse_insert(parent, root.latest, pair))

    def insert(self, pair):
        """
        Makes a call to recursive method to insert a node into a tree
        :param pair: Key-value pair containing key and data of a node
        """
        self.recurse_insert(self.dict, self.root, pair)

    def flag2(self, position):
        """
        Function to check for a heading or sub-heading in a sub-dictionary
        :param position: Sub-dictionary to be checked
        :return: Boolean value representing if a heading or sub-heading exists or not
        """
        for i in position.keys():
            if isinstance(position[i], dict):
                return True

    def clean_recurse(self, position, prePos=None, key=None):
        """
        Recursive function to clean up dictionary by removing 'before' keys from subheadings without children
        :param position: Sub-dictionary currently being worked in
        :param prePos: Parent dictionary of currently dictionary being worked within
        :param key: Current heading
        """
        match = self.flag2(position)
        if match:
            [self.clean_recurse(position[i], position, i) for i in position if isinstance(position[i], dict)]
        else:
            pos = prePos[key]
            temp = pos['values']
            prePos[key] = temp

    def clean(self):
        """
        Makes call to function to clean up dictionary by removing 'values' keys from subheadings without children
        """
        self.clean_recurse(self.dict, list(self.dict.keys())[0])

    def __str__(self):
        """
        String representation of a tree object
        :return: Returns dictionary of tree and writes to .json file
        """
        myjson = json.dumps(self.dict, indent=4)
        writeFile.write(str(myjson))
        return str(self.dict)
