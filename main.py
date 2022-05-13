import DataStructure as ds

tree = ds.RedBlackTree()  # initialize RB-tree
DICTIONARY_NAME = "EN-US-Dictionary"


def readFile(fileName):
    file = open(fileName, "r")
    for i in file:
        tree.insert(i.rstrip('\n'))
    file.close()


while True:
    print("What do you want to do?")
    option = input(
        "1- Load \"" + DICTIONARY_NAME + "\"\t2- Print size of the Dictionary\n"
        "3- Insert Word             \t4- Look-up a Word\n"
        "5- Print Tree Height       \t6- Exit\n"
        "> ")

    if option == '1':
        readFile(DICTIONARY_NAME + ".txt")
        print(DICTIONARY_NAME + " loaded successfully!")

    elif option == '2':
        print(DICTIONARY_NAME + ' currently has ' + str(tree.number_of_nodes) + ' words!')

    elif option == '3':
        s = str(input("Enter the word you want to insert: "))
        if tree.search(s.strip().lower()):
            print("Word is already in the dictionary!")
        elif len(s) > 0 and not s.isspace():
            tree.insert(s.strip().lower())
            print('\"' + s + '\" inserted Successfully')
        else:
            print('Invalid entry')

    elif option == '4':
        s = str(input("Enter the word you want to look-up: "))
        if tree.search(s.strip().lower()):
            print("FOUND \"" + s + '\"!')
        else:
            print("\"" + s + '\" DOES NOT EXIST IN THE DICTIONARY')

    elif option == '5':
        print(tree.heightOfTree(tree.root, 0))

    elif option == '6':
        print("Thank you for using our application! :)")
        break

    print()
