import random
from PROJECT_part1 import kahlil, kahlil_pairs, kahlil_unique_pairs


from PROJECT_part2 import conditional_triple
from PROJECT_part2 import kahlil_triples, kahlil_unique_triples, prob_pair

"""
Function to approximately count syllables in a word. This is done by
counting first letter vowels, the number of occurences where a vowel
appears after a consonant, and disregarding any "e's" that appear
at the end of a word. It isn't perfect, but works quite well.
"""
def syllables(word):
    count = 0
    vowels = "aeiouyAEIOUY"
    if word[0] in vowels:
        count += 1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            count += 1
            if word.endswith("e"):
                count -= 1
    return count

#Now we initialize the first pair of the poem as in part 2. 
poem_3 = []
first_pair = random.choices(kahlil_unique_pairs,prob_pair)
first_pair = first_pair[0]
poem_3.append([first_pair[0]])
poem_3.append([first_pair[1]])

#The following is identical to part 2 
count=0
period_words = []
for triple in kahlil_unique_triples:
    diff_triples = [triple for triple in kahlil_unique_triples if (triple[0],triple[1]) == (poem_3[count][0],poem_3[count+1][0])]
    next_word = random.choices([diff_triples[i][2] for i in range(len(diff_triples))],[conditional_triple(kahlil,diff_triples[i][0],diff_triples[i][1],diff_triples[i][2]) for i in range(len(diff_triples))])
    poem_3.append(next_word)
    count+=1
    if next_word[0][len(next_word[0])-1] in ['.','?','!']:
        period_words.append(next_word)    
    if len(period_words) == 3:    
        break
    
    
#Counter for syllables. I have picked 10 syllables per line.
i = 1
syl = 0
for elem in poem_3:    
    syl += syllables(elem[0])
    if syl >= 10*i:
        poem_3.insert(poem_3.index(elem)+1,['\n'])
        i+=1
        continue

      
#Capitalizing the "i's"
for word in poem_3:
    if word == ["i"]:
        poem_3[poem_3.index(word)] = ["I"] 
 
#Capitalize the first letter of every sentence.
poem_3[0][0] = poem_3[0][0].capitalize()        
for word in poem_3:
    if word in period_words[0:len(period_words)-1]:
        poem_3[poem_3.index(word)+1][0] = poem_3[poem_3.index(word)+1][0].capitalize()
        


#Combining words in poem_3 into single line.   
poem_3 = ' '.join(poem_3[i][0] for i in range(len(poem_3)))
 
#print(poem_3)
