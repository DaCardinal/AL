import functools
import operator

class CondensedTrie:
    def __init__(self):
        self.root = PhraseNode("")

    def add(self, tweet):
        (lastSharedNode, remainingSuffix) = self.computeDeepestCommonNodeAndSuffix(self.root, tweet)

        if(lastSharedNode.linkMap != 0):
            self.replaceOrRegister(lastSharedNode)
        
        self.addSuffix(lastSharedNode, remainingSuffix)
    
    def replaceOrRegister(self, node):
        child = node.lastAdded

        if (len(child.linkMap) != 0):
            replaceOrRegister(child)

        candidateChildren = register.get(child.label)

class PhraseNode(object):

    def __init__(self, label):
        self.label = label
        self.inCount = 0
        self.linkMap = {}
        self.lastAdded = {}

    def neighbor(self, term):
        if self.linkMap.get(term):
            return linkMap.get(term)
        else:
            self.lastAdded = PhraseNode(term)
            self.linkMap[term] = self.lastAdded
            return self.lastAdded
    
    def addCount(self, delta = 1):
        self.inCount += delta
    
    def __eq__(self, other):

        if isinstance(other, PhraseNode):
            if (this.hashCode != other.hashCode):
                return False
            elif(this.label != other.label):
                return False
            else:
                self.compareLinkMaps(this.linkMap, other.linkMap)
        else:
            return False
    
    def pointerHashCode(self):
        return self.__hash__()

    def foldl(self, func, acc, xs):
        return functools.reduce(func, xs, acc)

    def __hash__(self):
        foldlMap =  {k.__hash__() ^ v.pointerHashCode() for k, v in self.linkMap.items()}
        return self.foldl(operator.xor, self.label.__hash__(), foldlMap)

    def compareLinkMaps(self, lmap1, lmap2):

        if(lmap1.size != lmap2.size):
            return False
        
        for key in lmap1.keys():
            entry1 = lmap1[key]

            if lmap2.get(key1):
                matched = lmap2.get(key1) == entry1
            else:
                matched = False

            if(not matched):
                return False
        
        return True

# driver function
def main():
    p = PhraseNode("label a")
    c = PhraseNode("label a")
    print p.pointerHashCode()
    print c.pointerHashCode()
 
if __name__ == '__main__':
    main()