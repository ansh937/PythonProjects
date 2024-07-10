with open("story.txt","r")as f:
  story=f.read()
  
  
  words = set()
  start_of_word = -1
  '''Initializing start_of_word to -1 serves as a clear indicator that no start tag < has been encountered yet. Once a start tag is found, it is set to a valid index. After extracting a word, it is reset to -1 to search for new start tags. This mechanism ensures the code correctly identifies and processes words enclosed in < and >.'''

  target_start = "<"
  target_end = ">"

  
  #we have to find where the the angle bracket is 
  for i,char in enumerate(story):#*This enumertae() function provide both index and value if your iterating through the list eg below 
    if char == target_start:
        start_of_word = i#The line start_of_word = i is used to store the index of the opening tag < when it is encountered in the string. This index is stored so that when the corresponding closing tag > is found, the substring between these two indices (inclusive) can be extracted.
    if char == target_end and start_of_word != -1:#Checks if the current character char is > and start_of_word is not -1 (indicating a < was previously found).
        word = story[start_of_word: i + 1]#Extracts the word from the story string, from the index start_of_word to i + 1 (inclusive of >).
        words.add(word)#Adds the extracted word to the words set.
        start_of_word = -1#Resets start_of_word to -1 to look for the next word.
        
        
  answers = {}#Initializes an empty dictionary named answers to store user inputs corresponding to each word.

for word in words:#Loops through each word in the words set.
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer#stores the user's input in the answers dictionary, with the word as the key.

for word in words:#Loops through each word in the words set.
    story = story.replace(word, answers[word])#Replaces each occurrence of word in the story string with the corresponding value from the answers dictionary.

print(story)


'''eg 
# Sample list
fruits = ['apple', 'banana', 'cherry']

# Using enumerate to get index and value
for index, fruit in #*enumerate(fruits):
    print(index, fruit)
Output:

Copy code
0 apple
1 banana
2 cherry
    '''
    
