#This code counts characters and print out a frequency for each type
def get_char_num(a):

'''
Args:
- char_str(string): character array

returns:
    dict_char = dict()
    for char in char_str:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
