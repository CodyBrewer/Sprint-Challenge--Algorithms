'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0 
    def count_th_inner(word):
        nonlocal count
        
        if len(word) == 0:
            return count
        
        if word[-2:] == 'th':
            count_th_inner(word[:-2])
            count += 1
        else:
            count_th_inner(word[:-1])

        return count
    
    return count_th_inner(word)