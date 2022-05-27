import random

#read the text file
with open(r"C:\Users\sharm\Desktop\Kahlil Gibran.txt",encoding='utf8') as x:
    data = x.read()
    data = data.lower()
    kahlil = data.split()
    kahlil[0] ="the"


#Construct function to identify distinct elements      
def unique(list):
    unique_list=[]
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list        
            
#This gives me the list of distinct words (S)            
kahlil_unique = unique(kahlil)            
    
    
#pairs of words function  
def list_pairs(list):
    List = [list[i:i+2] for i in range(len(list)-1)]
    return List

#To get unique pairs of words 
kahlil_pairs = list_pairs(kahlil)
kahlil_unique_pairs = unique(kahlil_pairs)

#This function gives you the probability of a pair of words "a" and "b"
#appearing together 
def conditional(list,a,b):
    count_a = list.count(a)
    list_2 = list_pairs(list)
    count_pair = list_2.count([a,b])
    if count_a != 0:
        return count_pair/count_a
    else:
        print("Word not found")

#Function that assigns probability of a word occuring in a list
def weight(list,word):
    weight = list.count(word)/len(list)
    return weight

# Applying weight() to words in kahlil_unique
probs = []
for word in kahlil_unique:
    probs.append(weight(kahlil,word))   

        
#First word in poem selected using using random.choices, weighted 
# by prob of word 
poem_1 = []
first = random.choices(kahlil_unique,probs)
poem_1.append(first)


"""
Successive words are weighted by the conditional probability of them
occuring given the previous word. Also,I have created a list called
period_words, to capture the words ending with a sentence finisher.
The current max length is 1, i.e. one sentence, but this can be
changed if you want a longer poem.
"""
count=0
period_words = []
for pair in kahlil_unique_pairs:
    diff_pairs = [pair for pair in kahlil_unique_pairs if pair[0] == poem_1[count][0]]
    next_word = random.choices([diff_pairs[i][1] for i in range(len(diff_pairs))],[conditional(kahlil,diff_pairs[i][0],diff_pairs[i][1]) for i in range(len(diff_pairs))])
    poem_1.append(next_word)
    count+=1
    if next_word[0][len(next_word[0])-1] in ['.','?','!']:
        period_words.append(next_word)
    if len(period_words) == 1:
        break
    
#To find average length of a sentence
avg_sentence_length = len(poem_1)/len(period_words)

#Capitalizing the "i's"
for word in poem_1:
    if word == ["i"]:
        poem_1[poem_1.index(word)] = ["I"] 


#Capitalize the first letter of every sentence.
poem_1[0][0] = poem_1[0][0].capitalize()        
for word in poem_1:
    if word in period_words[0:len(period_words)-1]:
        poem_1[poem_1.index(word)+1][0] = poem_1[poem_1.index(word)+1][0].capitalize()
 

#Combining words in poem_1 into single line.   
poem_1 = ' '.join(poem_1[i][0] for i in range(len(poem_1)))

#Run the next line if you want the output
#print(poem_1)


    
