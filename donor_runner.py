from Trees.src.nodes.bst_node import BSTNode
from Trees.src.trees.bst_tree import BST
from Trees.src.donor_prog.donor import Donor
from typing import Tuple
import sys

def parse_line(line:str) -> Tuple[str]:
    name, amount = line.split(':')
    return  name, int(amount)


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
                print ("Wrong argument given for who command")
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
    results = []

    for donor in donors:
        tree.add_value (donor)

    #tree.get_node(18)

    if cmd == 'rich':
        print (tree.get_max_node().value)
    elif  cmd == 'cheap':
        print (tree.get_min_node().value)
    elif  cmd == 'all':
        tree.inorder(results)
        for x in results:
            print (x.value)
    elif  cmd == 'list_above':
        tree.inorder(results)
        no_match = True
        for x in results:
            if x.value.amount >= amount:
                print (x.value)
                no_match = False
                break
        if no_match:
            print ("No Match")

    elif  cmd == 'list_below':
        tree.inorder(results)
        no_match = True
        for x in reversed(results):
            if x.value.amount < amount:
                print (x.value)
                no_match = False
                break
        if no_match:
            print ("No Match")

    elif  cmd == 'who':
        tree.inorder(results)
        no_match = True
        for x in results:
            if x.value.amount == amount:
                print (x.value)
                no_match = False
                break
        if no_match:
            print ("No Match")

