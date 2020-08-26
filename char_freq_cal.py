#This code counts characters and print out a frequency for each type
def get_char_num(a):

'''
Args:
- char_str(string): character array

returns
''':
    dict_char = dict()
    for char in char_str:
        if char not in dict_char:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_relative_freq(char_dict):
'''
documentation
'''
    print('freqs')
    total = float(sum([dict[char] for char in char_dict.keys()]))
    for char in char_dict.keys():
        print(char + ':' + str(char_dict[char]/total))

get_relative_freq(get_char_num('ATCTGACGCGCGCCGC'))
