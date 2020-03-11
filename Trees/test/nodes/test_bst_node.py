import unittest
from typing import Optional, Callable, TypeVar, Generic
from Trees.src.errors import EmptyTreeError, MissingValueError
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')



class TestBSTNode(unittest.TestCase):
   def test_add_node_with_children(self):
       a = BSTNode(50)
       b = BSTNode(40)
       c = BSTNode(35)
       d = BSTNode(37)
       e = BSTNode(45)
       f = BSTNode(90)
       g = BSTNode(150)

       a.left = b
       b.left = c
       c.right = d
       b.right = e

       m =BSTNode(45, children = [a])

       tree = BST(m)
       self.assertEqual(len(tree), 6)

   def test_add_node_with_two_children(self):
       a = BSTNode(50)
       b = BSTNode(40)
       c = BSTNode(35)
       d = BSTNode(37)
       e = BSTNode(45)
       f = BSTNode(90)
       g = BSTNode(150)

       a.left = b
       b.left = c
       c.right = d
       b.right = e

       m = BSTNode(65, children = [a,f])
       tree1 = BST(m)
       self.assertEqual(len(tree1), 7)

   def test_add_parent(self):
       a = BSTNode(50)
       b = BSTNode(40)
       c = BSTNode(35)
       d = BSTNode(37)
       e = BSTNode(45)
       f = BSTNode(90)
       g = BSTNode(150)

       a.left = b
       b.left = c
       c.right = d
       b.right = e

       p = BSTNode(200)
       n = BSTNode(75, children = [f, g], parent = p)

       tree2 = BST(p)
       self.assertEqual(len(tree2), 4)


if __name__ == '__main__':
   unittest.main()
