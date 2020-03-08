from Trees.src.nodes.bst_node import BSTNode
from Trees.src.trees.bst_tree import BST
from Trees.src.donor_prog.donor import Donor
from typing import Tuple
import sys

def parse_line(line:str) -> Tuple[str]:
    name, value = line.split(':')
    return  name, int(value)


if __name__ == '__main__':
    donors = []

    file_name = "Trees/src/donor_prog/donor_files/donor10.txt"
    with open ( file_name ) as file:

        for line in file:
            donor = Donor(*parse_line(line))
            donors.append(donor)


    for donor in donors:
        print (donor)

    tree = BST()

    for donor in donors:
        tree.add_value (donor)

    print ("find len",len(tree))
    print ("find height",tree.height())
    print ("find 19",tree.get_node(19).value)
    print ("find 1742",tree.get_node(1742))


    print (len(sys.argv), sys.argv,sys.argv[1])


#    if len(sys.argv) == 2:

