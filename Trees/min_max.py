# This is in my bst_node.py file

    def get_min_node(self) -> Generic[T]:
        if self.left is None:
            return self
        else:
            self.get_min_node(self.left)

#I call if from my bst_tree.py file with this code
 def get_min_node(self) -> BSTNode[T]:
        if self.root is None:
            raise MissingValueError()
        else:
            return self.root.get_min_node(self.root)

#It can find the min node, but it won't return a node, it just keeps giving 
#NoneType
