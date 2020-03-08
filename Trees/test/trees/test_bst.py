import unittest
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode


class TestBST(unittest.TestCase):
    def test_create_empty_tree(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)

    def test_create_tree(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)


    def test_tree_not_eq(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)

    def test_max(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(tree.get_max_node().value, 100)
        tree.add_value(80)
        self.assertEqual(tree.get_max_node().value, 100)
        tree.add_value(200)
        self.assertEqual(tree.get_max_node().value, 200)

    
    def test_max_empty(self):
        tree = BST()
        self.assertEqual(tree.get_max_node(), None)


    def test_min_test(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(tree.get_min_node(), 100)
        tree.add_value(80)
        self.assertEqual(tree.get_min_node(), 80)
        tree.add_value(200)
        self.assertEqual(tree.get_min_node(), 80)
        tree.add_value(60)
        self.assertEqual(tree.get_min_node(), 60)
        tree.add_value(90)
        self.assertEqual(tree.get_min_node(), 60)

    def test_min_empty(self):
        tree = BST()
        self.assertEqual(tree.get_min_node(), None)

#    def length_test(self):

#    def length_test_empty(self):

#    def height_test(self):
    
#    def height_test_empty(self):

#    def get_node(self):

#    def get_node_empty(self):

if __name__ == '__main__':
    unittest.main()
