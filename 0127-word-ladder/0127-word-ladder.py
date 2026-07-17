from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        q=deque([(beginWord,1)])
        visited={beginWord}
        while q:
            word,steps=q.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord=word[:i]+ch+word[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        q.append((newWord,steps+1))
        return 0

'''BFS explores:
all words at distance 1
then distance 2
then distance 3

So first time reaching endWord
= shortest transformation.

Let:
N = number of words
L = word length

Time:
O(N × L × 26)'''