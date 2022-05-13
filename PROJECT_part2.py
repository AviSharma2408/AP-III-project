import random

#Import necessary variables and functions 
from PROJECT_part1 import list_pairs, unique
from PROJECT_part1 import kahlil, kahlil_pairs,kahlil_unique_pairs

#Function to group triples of words from list
def list_triples(list):
    List = [list[i:i+3] for i in range(0, len(list)-2)]
    return List

#Unique pairs of triples
kahlil_triples = list_triples(kahlil)
kahlil_unique_triples = unique(kahlil_triples)

#This function gives you the probability of a word 'c' appearing 
#given the pair ('a','b') 
def conditional_triple(list,a,b,c):
    list_1 = list_pairs(list)
    count_ab = list_1.count([a,b])
    list_2 = list_triples(list)
    count_abc = list_2.count([a,b,c])
    if count_ab !=0:
        return count_abc/count_ab
    else:
        print("Pair not found")


#Function that assigns probability of a pair of words occuring 
#in a list of pairs
def weight_pair(list,a,b):
    Weight = list.count([a,b])/len(list)
    return Weight

#Assigning probability to all unique pairs
prob_pair = []
for pair in kahlil_unique_pairs:
    prob_pair.append(weight_pair(kahlil_pairs,pair[0],pair[1]))


#First psir in poem selected using using random.choices, weighted 
#by prob of pair occuring 
poem_2 = []
first_pair = random.choices(kahlil_unique_pairs,prob_pair)
first_pair = first_pair[0]
poem_2.append([first_pair[0]])
poem_2.append([first_pair[1]])

#After initializing a pair, each successive word is weighted by the 
#conditional probability that the word occurs given the previous pair
#of words. The process stops just as in PART 1.
count=0
period_words = []
for triple in kahlil_unique_triples:
    diff_triples = [triple for triple in kahlil_unique_triples if (triple[0],triple[1]) == (poem_2[count][0],poem_2[count+1][0])]
    next_word = random.choices([diff_triples[i][2] for i in range(len(diff_triples))],[conditional_triple(kahlil,diff_triples[i][0],diff_triples[i][1],diff_triples[i][2]) for i in range(len(diff_triples))])
    poem_2.append(next_word)
    count+=1
    if next_word[0][len(next_word[0])-1] in ['.','?','!']:
        period_words.append(next_word)
    if len(period_words) == 4:    
        break
    
#Capitalizing the "i's"
for word in poem_2:
    if word == ["i"]:
        poem_2[poem_2.index(word)] = ["I"] 
 
#Capitalize the first letter of every sentence.
poem_2[0][0] = poem_2[0][0].capitalize()        
for word in poem_2:
    if word in period_words[0:len(period_words)-1]:
        poem_2[poem_2.index(word)+1][0] = poem_2[poem_2.index(word)+1][0].capitalize()
  
#Combining words in poem_2 into single line    
poem_2 = ' '.join(poem_2[i][0] for i in range(len(poem_2)))


#print(poem_2)
