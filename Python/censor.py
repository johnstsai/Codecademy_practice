#censor
#You're doing great with these string function challenges. Last one!
#1.Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. 
#For example:

#censor("this hack is wack hack", "hack")
#should return:
#"this **** is wack ****"
#Assume your input strings won't contain punctuation or upper case letters.
#The number of asterisks you put should correspond to the number of letters in the censored word.

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
print censor("damn it", "damn")