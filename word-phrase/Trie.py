# Python program for insert and search
# operation in a Trie
 
class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = {}
        self.links = set([])
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
 
class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
        self.links = set([])
 
    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return ord(ch)
 
 
    def insert(self,key, idx):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        self.links.add(idx)
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children.get(index):
                pCrawl.children[index] = self.getNode()
                pCrawl.links.add(idx)
            else:
                pCrawl.links.add(idx)
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
 
    def search(self, key):
         
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        pattern = ''
        match = False

        for level in range(length):
            index = self._charToIndex(key[level])
            pattern += chr(index)
            
            if not pCrawl.children.get(index):
                return False
            else:
                match = True
            pCrawl = pCrawl.children[index]
        
        # return pCrawl != None and pCrawl.isEndOfWord
        return (pCrawl, pattern)

    def hasPattenMatch(self, key):
        searchList = self.search(key)

        if(searchList):
            item = searchList[0]
            pattern = searchList[1]
            for k,v in item.children.items():
                return (item.children[k].links, pattern)
        else:
            return False

 
# driver function
def main():
 
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any", "by","their"]
    # keys = ["Adam has a' basketball", "Adam has a' football", "Maria has a car"]
    output = ["Not present in trie", "Present in trie"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for key in keys:
        t.insert(key, keys.index(key))
 
    # Search for different keys
    # print("{} ---- {}".format("the",output[t.search("the")]))
    # print("{} ---- {}".format("these",output[t.search("these")]))
    # print("{} ---- {}".format("their",output[t.search("their")]))
    # print("{} ---- {}".format("thaw",output[t.search("thaw")]))
    # item = t.search("Adam has a'")
    # print("{} ---- {}".format("Adam has a",output[item != None and item.isEndOfWord ]))
    print(t.hasPattenMatch("the"))
 
if __name__ == '__main__':
    main()