class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalnum() and i != " ":
                word += i
        word = word.lower()
        middle = [word[i] for i in range(int(len(word)/2))]
        secmiddle = [word[i] for i in range(int(len(word)/2), len(word))]
        revmid = middle[::-1]
        print(word)
        print(len(word))
        print(type(len(word)/2))
        print(len(word)/2)
        if len(word)/2 == int(len(word)/2):
            if secmiddle == revmid:
                return True
        else:
            if secmiddle[1:len(secmiddle)] == revmid[0:len(middle)]:
                return True
            else:
                print(secmiddle[1:len(secmiddle)])
                print(revmid[0:len(middle)])
                print(secmiddle)
                print(revmid)
                return False



        return False