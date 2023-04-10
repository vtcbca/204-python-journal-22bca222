#WRITE A SCRIPT TO ENTER ANY SENTENCE AND PRINT THOSE WORD WHICH IS PALINDROM.

def palindrom(word):
   return word == word[::-1]
sentc = [w for w in input ("enter a sentence:  ").split() if palindrom(w)]
print("there are {} palindroms in your sentence:\n".format(len(sentc)))
for pal in sentc:
    print(" {} is palindrom.".format(pal))
