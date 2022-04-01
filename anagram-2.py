def anagrams(word, words) :
    anags = [w for w in words if sorted(w) == sorted(word)]
    return anags