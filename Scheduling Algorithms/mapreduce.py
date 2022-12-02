
  
sent = """ deer bear river
car car river
deer car bear  """
wordlist=[]
print("Performing map function") 
for line in sent.splitlines():
    
    line = line.strip()
    words = line.split()
    
    for word in words:
        wordlist.append(word)
        print(word, 1)

current_word = None
current_count = 0
word = None
count = 1
wordlist.sort()  
print("Performing reduce function")
 
for word in wordlist:  
    # this if statement only works because Hadoop sorts map output by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count = current_count+ count
    else:
        if current_word:
            print(current_word, current_count)
        current_count = count
        current_word = word
#printing last word  
if current_word == word:
    print (current_word, current_count)