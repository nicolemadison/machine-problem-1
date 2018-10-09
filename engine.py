######REQ1######
def dictionary_input(filename):
    file_input = open(filename, 'r')
    dictionary_list = list()
    for line in file_input:
        line = line.split()
        dictionary_list.append(line)
    file_input.close()
    return dictionary_list	

#------------------------------------------------------------------------------------------------------------------------------#

######REQ2######
def picking_words():
    t = int(input())
	for i in range(t):
	    position = input()
	    position_list = [int(x) for x in position.split()]
	   
	    output_list = list()
	    for j in range (len(position_list)):
		index = position_list[j]                ##GETTING INDEX OF NUMBER FROM position_list
		result = dictionary_list[index]         ##GETTING ENTRY FROM dictionary_list
		output_list += result.split()

	    wordlist = ""
	    for word in output_list:
		wordlist += word + " "
    return wordlist.rstrip()				##RETURNS WORDS FROM dictionary_list FROM GIVEN STRING OF POSITION NUMBERS

#------------------------------------------------------------------------------------------------------------------------------#

######REQ3######	"MODE1"
def search_anagram():
    t = int(input())
    for i in range(t):
        query = input()
        query = sorted(query)
        query = "".join(query)
            
        output_list = []    
        if query in reference:
            indices = [i for i, x in enumerate(reference) if x == query]
            
            for index in indices:
                result = dictionary_list[index]         ##GETTING ENTRY FROM DICTIONARY LIST 
                output_list += result.split()
               
            wordlist = ""
            for word in output_list:
                wordlist += word + " "
    return wordlist.rstrip()				##RETURNS ALL VALID ANAGRAMS FROM dictionary_list GIVEN ONE WORD

#------------------------------------------------------------------------------------------------------------------------------#

######REQ4######	"MODE2"
def combine_words():
    t = int(input())
        for i in range (t):
	    words = input()
	    words = words.split()  
	    game_list = list()

	    for j in words:
		for k in j:
		    count_word = j.count(k)
		    count_comb = game_list.count(k)
		    if count_word > count_comb:
			for l in range (count_word - count_comb):
			    game_list.append(k)
	    game_list = "".join(sorted(game_list))
	    return game_list				##RETURNS SET OF SCRAMBLED LETTERS GIVEN STRING OF WORDS
            
#------------------------------------------------------------------------------------------------------------------------------#

######REQ5######
def check_words():
    t = int(input())
	for i in range (t):
	    words = input()
	    words = words.split() 
	    scrambled, basis = words[0], words[1]
    	    basis = basis.lower()
            outcome = False

	    dictionary_input(filename)   		###CALLING REQ1 FUNCTION
					  		###THIS MUST RETURN THE dictionary_list
	    for line in dictionary_list:
		if basis == line.rstrip():
            	    outcome = True
	    
	    for j in word:
		if scrambled.count(j) > basis.count(j):
		    outcome = False
	    return outcome				##RETURNS OUTCOME EITHER TRUE / FALSE

#------------------------------------------------------------------------------------------------------------------------------#	

######REQ6######
def calc_score(word):
	
	score = 0
	
	scores = {
	'e':1, 'a':1, 'i':1, 'o':1, 'u':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1,
	'd':2, 'g':2,
	'b':3, 'c':3, 'm':3, 'p':3,
	'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
	'k':5,
	'j':8, 'x':8, 
	'q':10, 'z':10
	}
	
	for letter in word:
		score += scores[letter]
		
	return score
