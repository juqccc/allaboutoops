def count(s):
    new_dict = {}
    if not s:
        return {}
    for letter in s:
       if letter in new_dict:
           new_dict[letter] += 1
       else:
           new_dict[letter] = 1
       print(new_dict)
    return new_dict






print(count('abaabbaabnnbaa')) #output {'a': 2, 'b': 1}


