#strings are immutable sequences

# 1. Some of the methods offered by strings are:

# capitalize() – changes all string letters to capitals;
# center() – centers the string inside the field of a known length;
# count() – counts the occurrences of a given character;
# join() – joins all items of a tuple/list into one string;
# lower() – converts all the string's letters into lower-case letters;
# lstrip() – removes the white characters from the beginning of the string;
# replace() – replaces a given substring with another;
# rfind() – finds a substring starting from the end of the string;
# rstrip() – removes the trailing white spaces from the end of the string;
# split() – splits the string into a substring using a given delimiter;
# strip() – removes the leading and trailing white spaces;
# swapcase() – swaps the letters' cases (lower to upper and vice versa)
# title() – makes the first letter in each word upper-case;
# upper() – converts all the string's letter into upper-case letters.

# 2. String content can be determined using the following methods (all of them return Boolean values):

# endswith() – does the string end with a given substring?
# isalnum() – does the string consist only of letters and digits?
# isalpha() – does the string consist only of letters?
# islower() – does the string consists only of lower-case letters?
# isspace() – does the string consists only of white spaces?
# isupper() – does the string consists only of upper-case letters?
# startswith() – does the string begin with a given substring?




# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))

# multiline string

ms = ''' This is 
a multiline string'''
ms2 = """ This also is
 a multiline string"""
print(ms,ms2,sep="\n")

# string are indexed
ms = '# string are indexed'
for ix in range(len(ms)):
    print(ms[ix], end =' ')
print()
for ch in ms:
    print(ch,end=' ')
print()

#Slices - same as list


# in & not in
print('string' in ms)
print('st' not in  ms)

#index
print(ms.index('s'))

#string to list
print(list(ms))

#count
print('n comes',ms.count('n'), 'times')

#capitalize
print("aBcd".capitalize()) # Abcd

#lower 
print("ABc  to lower =>","ABc".lower())

#endwith
print('abc ends with "bc" is','abc'.endswith('bc'))

#find
print('bc is present at index','abc'.find('bc'), 'in abc')
print('d is not present in "abc" so the index is', 'abc'.find('d'))

#isalnum
print("abc123 is alphanumeric =>","123".isalnum())

#isdigit
print("123 is digit only=>","123".isdigit())

#isalpha
print("abc is alphabetic only =>", "abc".isalpha())

#islower
print('abc is lower =>', 'abc'.islower())

#isupper
print("ABc is upper only =>", "ABc".isupper())

#isspace
print('"  " is space whitespace only =>',"  ".isspace() )

print(",".join(["one","two","three"]))