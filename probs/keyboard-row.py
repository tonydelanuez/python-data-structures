class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        ok_words = []
        letters_1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        letters_2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        letters_3 = ["z", "x", "c", "v", "b", "n", "m"]
        for word in words:
            print(word)
            in_top = True
            if word.lower()[0] in letters_1:
                selected_letters = letters_1
            elif word.lower()[0] in letters_2:
                selected_letters = letters_2
            elif word.lower()[0] in letters_3:
                selected_letters = letters_3
            else: 
                return False
            for char in word.lower()[1::]:
                if(char not in selected_letters):
                    in_top = False
            if in_top:
                ok_words.append(word)
        return ok_words