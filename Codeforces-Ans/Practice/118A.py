s = input()
vowels = set('aeiouy')
print(''.join('.'+c.lower() for c in s if c.lower() not in vowels))