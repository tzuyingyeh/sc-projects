"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dict_list = []


def main():
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input('Find anagram for: ')
        if word == EXIT:
            break
        else:
            read_dictionary()
            find_anagrams(word)


def read_dictionary():
    global dict_list
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            dict_list.append(line)
    return dict_list


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    num_stack = [0]
    alphabet_list = []
    new_list = []
    for i in range(len(s)):
        alphabet_list.append(s[i])
    find_anagrams_helper(s, alphabet_list, [], new_list, num_stack)
    print(str(num_stack[0])+' anagrams:'+str(new_list))


def find_anagrams_helper(s, alphabet_list, current, new_list, num_stack):
    if len(current) == len(alphabet_list):
        word = ''
        for i in current:
            word += alphabet_list[i]
        if word not in new_list and word in dict_list:
            new_list.append(word)
            print('Searching...')
            print('Found:  '+word)
            num_stack[0] += 1
    else:
        for i in range(len(alphabet_list)):
            if i not in current:
                current.append(i)
                if has_prefix(current, alphabet_list) is True:
                    find_anagrams_helper(s, alphabet_list, current, new_list, num_stack)
                current.pop()


def has_prefix(sub_index, alphabet_list):
    """
    :param sub_index:
    :return:
    """
    sub_s = ''
    for i in sub_index:
        sub_s += alphabet_list[i]
    for word in dict_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
