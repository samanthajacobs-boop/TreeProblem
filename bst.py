from Trees.src.nodes.bst_node import BSTNode
from Trees.src.trees.bst_tree import BST

if __name__ == '__main__':
    a = BSTNode(50)
    b = BSTNode(40)
    c = BSTNode(35)
    d = BSTNode(37)
    e = BSTNode(45)
    f = BSTNode(90)

    a.left = b
    b.left = c 
    c.right = d
    b.right = e

    print ( "create tree with 5 nodes")
    tree = BST(a)
    print ("len ex 5: ", len(tree))
    print ("add node", tree.add_value(100))
    print ("len ex 6: ", len(tree))
    print ("remove node", tree.remove_value(50))
    print ("len ex 5: ", len(tree))

    results = []
    tree.inorder(results)
    for x in results:
        print (x.value)


    print ("\n Testing adding children")
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
    m = BSTNode(45, children=[a])
    tree1 = BST(m)
    print ("len ex 6: ", len(tree1))
    results = []
    tree1.inorder(results)
    for x in results:
        print (x.value)
    del m
    m = BSTNode(65, children=[a,f])
    tree1 = BST(m)
    print ("len ex 7: ", len(tree1))
    results = []
    tree1.inorder(results)
    for x in results:
        print (x.value)

    print ("\n Testing adding parent")
    p = BSTNode(200)
    n = BSTNode(75, children=[m,g],parent=p)
    tree2 = BST(p)
    print ("len ex 10: ", len(tree2))
    results = []
    tree2.inorder(results)
    for x in results:
        print (x.value)


    tree = BST()
    print( "Empty tree len", len(tree))
    print( "Empty tree hieght", tree.height())

    tree = BST(a)
    print ("Tree height:", tree.height())
    print ("Tree length:", len(tree))
    node_min = tree.get_min_node()
    print ("Tree min:", node_min.value) 
    node_max = tree.get_max_node()
    print ("Tree max:", node_max.value)


    node_45 = tree.get_node(45)
    print ("Tree 45", node_45.value)
    node_50 = tree.get_node(50)
    print ("Tree 50", node_50.value)
    print ("add node")
    tree.add_value(100)
    print ("Tree height:", tree.height())
    print ("Tree length:", len(tree))


    new_tree = BST()

    new_tree.add_value(100)
    new_tree.add_value(75)
    new_tree.add_value(200)
    new_tree.add_value(300)
    new_tree.add_value(30)
    new_tree.add_value(30)
    new_tree.add_value(20)

    print ("Test get mode with key 200")
    node_get_200 = new_tree.get_node(200)
    print ("results", node_get_200.value)

    print ("Tree height:", new_tree.height())
    print ("Tree length:", len(new_tree))

    print ("new_tree added value")
    node_100 = new_tree.get_node(100)
    node_100 = new_tree.get_node(30)

    print ("new_tree 100", node_100.value)
    print ("new_tree 75", new_tree.get_node(75).value)
    print ("new_tree 20", new_tree.get_node(20).value)

    print ("removing 20")
    new_tree.remove_value(20)
    print ("Tree height:", new_tree.height())
    print ("Tree length:", len(new_tree))
 #   print ("new_tree get 20", new_tree.get_node(20).value)

    print ("new_tree get 200", new_tree.get_node(200).value)
    print ("removing 200")
    new_tree.remove_value(200)
    print ("Tree height:", new_tree.height())
    print ("Tree length:", len(new_tree))
#    print ("new_tree get 200", new_tree.get_node(200).value)

    results = []
    new_tree.inorder(results)
    for x in results:
        print (x.value)

    print ("new_tree added 80")
    new_tree.add_value(80)
    results = []
    new_tree.inorder(results)
    for x in results:
        print (x.value)

# remove a double node
    print ("removing 75")
    new_tree.remove_value(75)
    print ("Tree height:", new_tree.height())
    print ("Tree length:", len(new_tree))
    results = []
    new_tree.inorder(results)
    for x in results:
        print (x.value)

# remove root
    print ("removing 100")
    new_tree.remove_value(100)
    print ("Tree height:", new_tree.height())
    print ("Tree length:", len(new_tree))
    results = []
    new_tree.inorder(results)
    for x in results:
        print (x.value)
