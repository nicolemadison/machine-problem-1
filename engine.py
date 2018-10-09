
def dictionary_input(filename):
  file_input = open(filename, 'r')
  dictionary_list = list()
  for line in file_input:
    line = line.split()
    dictionary_list.append(line)


def calcscore(word):
	
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

def picking_words()
    t = int(input())
	for i in range(t):
	    position = input()


	    position_list = [int(x) for x in position.split()]
	    #print("position list: " + str(position_list))

	    output_list = []
	    for j in range (len(position_list)):
		index = position_list[j]                ## GETTING INDEX OF NUMBER FROM POSITION LIST
		result = dictionary_list[index]         ## GETTING ENTRY FROM DICTIONARY LIST 
		output_list += result.rsplit()

	    wordlist = ""
	    for word in output_list:
		wordlist += word + " "
    return wordlist.rstrip()



def search_anagram()
    t = int(input())
    for i in range(t):
        query = input()
        query = sorted(query)
        query = "".join(query)
            
        output_list = []    
        if query in reference:
            indices = [i for i, x in enumerate(reference) if x == query]
            
            for index in indices:
                result = dictionary_list[index]         ## GETTING ENTRY FROM DICTIONARY LIST 
                output_list += result.rsplit()
               
            wordlist = ""
            for word in output_list:
                wordlist += word + " "
    return wordlist.rstrip()
