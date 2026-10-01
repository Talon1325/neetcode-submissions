class PrefixTree:

    def __init__(self):
        self.pretree = []

    def insert(self, word: str) -> None:
        self.pretree.append(word)

    def search(self, word: str) -> bool:
        if word in self.pretree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.pretree:
            if prefix in word:
                return True
        return False
        