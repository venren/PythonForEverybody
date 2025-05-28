import unittest

def shortestDistance(doc : str, word1: str, word2: str):
    wordSplit = doc.split()
    wordMap = {}
    runningCharCount = 0

    for i, w in enumerate(wordSplit):
        if w not in wordMap:
            init = list()
            init.append(runningCharCount)
            wordMap[w] = init
        else:
            wordMap[w].append(runningCharCount)
        
        runningCharCount += len(w) + 1 ## +1 for space

    if word1 not in wordMap or word2 not in wordMap:
        return -1
    
    word1IndexList = wordMap[word1]
    word2IndexList = wordMap[word2]

    ## we have 3 options here
    ## word 1 is before word 2 -- proceed 
    ## word 2 is before word 1 -- ignore 
    ## there are many different world and we are in one of the world People are 
    ## not sure which world they are in So we need to find the where are and shortest distance between the two world
    ## word 1 - are word 2 - world
    ## ordering = [word11, word21, word12, word22, word13, word23, word14, word15, word24]


    ## orderingw1 = [1,7,14,20,29]
    ## orderingw2 = [5,13,19, 37]
    
    match = []
    for i in range(len(word1IndexList)):
        for j in range(len(word2IndexList)):
            if word1IndexList[i] <= word2IndexList[j]:
                match.append(abs(word1IndexList[i] - word2IndexList[j])-1)
    
    return min(match) if len(match) > 0 else -1
    
class TestShortestDistance(unittest.TestCase):

    # def test_basic_case(self):
    #     doc = "the quick brown fox jumps over the lazy dog"
    #     print(shortestDistance(doc, "quick", "fox"))
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), 11)

    # def test_same_words_adjacent(self):
    #     doc = "the quick quick fox"
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), 5)

    # def test_words_far_apart(self):
    #     doc = "the quick brown fox jumps over the lazy dog"
    #     self.assertEqual(shortestDistance(doc, "the", "dog"), 7)

    def test_words_in_reverse_order(self):
        doc = "fox brown quick"
        print("I am testing 4 \n")
        self.assertEqual(shortestDistance(doc, "quick", "fox"), -1)

    def test_words_not_present(self):
        doc = "the quick brown fox"
        print("I am testing 3 \n")
        self.assertEqual(shortestDistance(doc, "cat", "dog"), -1)

    # def test_one_word_not_present(self):
    #     doc = "the quick brown fox"
    #     self.assertEqual(shortestDistance(doc, "quick", "dog"), -1)

    # def test_repeated_words(self):
    #     doc = "the quick brown quick fox brown the quick"
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), 0)

    def test_same_word_multiple_times(self):
        doc = "the quick quick quick"
        print("I am testing 2 \n")
        self.assertEqual(shortestDistance(doc, "quick", "quick"), 0)

    # def test_empty_document(self):
    #     doc = ""
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), -1)

    # def test_document_with_only_one_word(self):
    #     doc = "quick"
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), -1)

    # def test_document_with_only_target_words(self):
    #     doc = "quick fox"
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), 0)

    # def test_document_with_target_words_separated_by_one_word(self):
    #     doc = "quick brown fox"
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), 1)

    # def test_document_with_target_words_at_the_beginning_and_end(self):
    #     doc = "quick a b c d e f g fox"
    #     self.assertEqual(shortestDistance(doc, "quick", "fox"), 7)

    # def test_document_with_same_target_words(self):
    #     doc = "the quick quick fox"
    #     self.assertEqual(shortestDistance(doc, "quick", "quick"), 0)

    # def test_document_with_same_target_words_separated(self):
    #     doc = "the quick brown quick fox"
    #     self.assertEqual(shortestDistance(doc, "quick", "quick"), 1)

if __name__ == '__main__':
    unittest.main()