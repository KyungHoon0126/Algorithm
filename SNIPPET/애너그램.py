def are_anagrams(a, b):
    return sorted(a) == sorted(b)


print(are_anagrams('listen', 'silent'))
print(are_anagrams('pop', 'odd'))
print(are_anagrams('hello', 'hxxxx'))
