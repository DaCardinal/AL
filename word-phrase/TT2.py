class Node():
   def __init__(self):
       # Note that using dictionary for children (as in this implementation) would not allow lexicographic sorting mentioned in the next section (Sorting),
       # because ordinary dictionary would not preserve the order of the keys
       self.children = {}  # mapping from character ==> Node
       self.value = None

def find(node, key):
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value

def insert(root, string, value):
    node = root
    index_last_char = None
    for index_char, char in enumerate(string):
        print(index_char, char)
        if char in node.children:
            node = node.children[char]
        else:
            index_last_char = index_char
            break

    # append new nodes for the remaining characters, if any
    if index_last_char is not None: 
        for char in string[index_last_char:]:
            node.children[char] = Node()
            node = node.children[char]

    # store value in the terminal node
    node.value = value

if __name__ == "__main__":
    root = Node()
    insert(root, "bd", "g")
    insert(root, "bd", "e")
    insert(root, "bdf", "h")
    print(root.children)
    print(find(root, "bd"))