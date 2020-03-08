from Trees.src.nodes.bst_node import BSTNode
from Trees.src.trees.bst_tree import BST
from Trees.src.donor_prog.donor import Donor
from typing import Tuple
import sys

def parse_line(line:str) -> Tuple[str]:
    name, value = line.split(':')
    return  name, int(value)


if __name__ == '__main__':

    #print (len(sys.argv), sys.argv,sys.argv[1])
    cmd = ""
    amount = 0

    if len(sys.argv)  < 3:
        print ("Not enough command line arugments:",sys.argv)
        exit()
    else:
        file_name = sys.argv[1]   
        if sys.argv[2] == 'all':
            cmd = 'all'
        elif sys.argv[2] == 'cheap':
            cmd = 'cheap'
        elif sys.argv[2] == 'rich':
            cmd = 'rich'
        elif sys.argv[2] == 'who':
            if len(sys.argv) == 4:     # extra who arg
                cmdstring = sys.argv[3]
                if cmdstring[0] == '+':
                    cmd = 'list_above'
                    amount = int(cmdstring)
                elif cmdstring[0] == '-':
                    cmd = 'list_below'
                    amount = int(cmdstring)*-1
                else:
                    cmd = 'who'
                    amount = int(cmdstring)
            else:
                print ("Wrong argument given for who cmmand")
                exit()

        else:
            print ("Wrong aurgments given:", sys.argv)
            exit()

    #print("CMD and amount",cmd,amount) 
    donors = []

    #file_name = "Trees/src/donor_prog/donor_files/donor10.txt"
    with open ( file_name ) as file:

        for line in file:
            donor = Donor(*parse_line(line))
            donors.append(donor)


    #for donor in donors:
    #    print (donor)

    tree = BST()

    for donor in donors:
        tree.add_value (donor)

    if cmd == 'rich':
        print (tree.get_max_node().value)
    elif  cmd == 'cheap':
        print (tree.get_min_node().value)
    elif  cmd == 'all':
        for x in tree:
            print (x)
        
    print ("find len",len(tree))
    print ("find height",tree.height())
    print ("find 19",tree.get_node(19).value)
    print ("cheap",tree.get_min_node().value)
    print ("rich",tree.get_max_node().value)
    print ("find 1742",tree.get_node(1742))

