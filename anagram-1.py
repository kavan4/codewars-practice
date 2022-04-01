def anagrams(given_word, list_of_words):
    # sort the given word
    given_word = ''.join(sorted(given_word))


    # init temp arry for storing
    temp_arr = []

    #loop over list of words
    for word in list_of_words:
        #sort each word
        sorted_word  = ''.join(sorted(word))
        #init pointers
        i=0
        j=0
        # loop while it does not run out of chars
        while (i < len(given_word) and j < len(sorted_word)) :
            #compare chars. if match, increment both. else increment word
            if(given_word[i] == sorted_word[j]):
                i+=1
                j+=1
            else :
                j+=1
        
        #if word len is same and pointer values are same, add to temp list
        if ((i == j) and (len(word) == len(given_word))) :
            temp_arr.append(word)
        
    return temp_arr
            
        