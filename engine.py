
def dictionaryinput(filename):
  file_input = open(filename, 'r')
  dictionary_list = list()
  for line in file_input:
    line = line.split()
    dictionary_list.append(line)
