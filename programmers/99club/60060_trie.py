class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0

    def insert(self,word):
        curr = self
        for i in word:
            curr.count += 1
            if not i in curr.child:
                curr.child[i] = Trie()
            curr = curr.child[i]
        curr.count += 1

    def search(self, word):
        curr = self
        for i in word:
            if i =="?":
                return curr.count
            if i not in curr.child:
                return 0
            curr = curr.child[i]


        return curr.count


def solution(words, queries):
    TrieRoot = [Trie() for _ in range(10000)]
    ReTrieRoot = [Trie() for _ in range(10000)]

    answer = []

    for i in words:
        TrieRoot[len(i)-1].insert(i)
        ReTrieRoot[len(i)-1].insert(i[::-1])

    for i in queries:
        if i[0] != "?":
            res = TrieRoot[len(i)-1].search(i)

        else:
            res = ReTrieRoot[len(i)-1].search(i[::-1])

        answer.append(res)

    return answer
