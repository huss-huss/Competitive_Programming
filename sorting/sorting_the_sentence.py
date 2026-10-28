class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """

        arrayOfWords = s.split()
        results = [""] * len(arrayOfWords)
        for word in arrayOfWords:
            index = int(word[-1]) - 1
            results[index] = word[0:len(word)-1]
        sentence = " ".join(results)
        return sentence
