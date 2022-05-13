import random

from PROJECT_part1 import kahlil, list_pairs, unique
from PROJECT_part2 import conditional_triple, weight_pair, list_triples
from PROJECT_part3 import syllables

#read the text file
with open(r"C:\Users\sharm\Desktop\Oscar Wilde.txt",encoding='utf8') as x:
    data = x.read()
    data = data.lower()
    oscar = data.split()
    oscar[0] = "Hélas!"
    
#It was easiest to just combine the state space of our two poets
combined = oscar + kahlil
combined_unique = unique(combined)
combined_pairs = list_pairs(combined)
combined_unique_pairs = unique(combined_pairs)
combined_triples = list_triples(combined)
combined_unique_triples = unique(combined_triples)

#Assigning probabilities to pairs
prob_pair = []
for pair in combined_unique_pairs:
    prob_pair.append(weight_pair(combined_pairs,pair[0],pair[1]))
    
#Initializing first pair  
poem_4 = []
first_pair = random.choices(combined_unique_pairs,prob_pair)
first_pair = first_pair[0]
poem_4.append([first_pair[0]])
poem_4.append([first_pair[1]])


#This section of the code works similar to parts 2 and 3. The only 
#Difference being that we now consider two poets instead of just one.
count=0
period_words = []
for triple in combined_unique_triples:
    diff_triples = [triple for triple in combined_unique_triples if (triple[0],triple[1]) == (poem_4[count][0],poem_4[count+1][0])]
    next_word = random.choices([diff_triples[i][2] for i in range(len(diff_triples))],[conditional_triple(combined,diff_triples[i][0],diff_triples[i][1],diff_triples[i][2]) for i in range(len(diff_triples))])
    poem_4.append(next_word)
    count+=1
    if next_word[0][len(next_word[0])-1] in ['.','?','!']:
        period_words.append(next_word)    
    if len(period_words) == 3:
        break


#10 syllables per line
i = 1
syl = 0
for elem in poem_4:    
    num = syllables(elem[0])
    syl += num
    if syl >= 10*i:
        poem_4.insert(poem_4.index(elem)+1,['\n'])
        i+=1    
  
#Capitalizing the "i's"
for word in poem_4:
    if word == ["i"]:
        poem_4[poem_4.index(word)] = ["I"] 
 
#Capitalize the first letter of every sentence.
poem_4[0][0] = poem_4[0][0].capitalize()        
for word in poem_4:
    if word in period_words[0:len(period_words)-1]:
        poem_4[poem_4.index(word)+1][0] = poem_4[poem_4.index(word)+1][0].capitalize()
        
#Combining words in poem_3 into single line.   
poem_4 = ' '.join(poem_4[i][0] for i in range(len(poem_4)))

#Ta-da 
print(poem_4)