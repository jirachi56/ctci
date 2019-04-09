#week 1
#Jaysun Balakrishnan 4/2/19

from collections import Counter

'''1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''
def isUnq(s):
    print(len(set(s)) == len(s))

#kinda messy
def isUnqq(s):
    for c in s:
        cnt = 0
        for i in range(len(s)):
            if c == s[i]: cnt += 1
        if cnt >1: return False
    return True

print(isUnqq('frankk'))
'''
1.2
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
permutation example set, tse
'''

#not perfect, would need to do this with recursion
def isPerm(s1,s2):
    return (Counter(s1) == Counter(s2))

'''    for c in s1:
        if c in s2: isPerm(s1[1:],s2[1:])
        else: return False
    if len(s1)==len(s2): return True
    else: return False
'''
print(isPerm('ees', 'ess'))


'''
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words
'''
#basically you can just check if this is a palindrome or not? because if it is a palindrome it is by default a permutation of the palindrome
def palPerm(s):
    s == s[::-1]

'''
1.5 There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
'''

def oneEdit(original, changed):
    m = len(original)
    n = len(changed)

    if abs(m - n) > 1:
        return false

    count = 0    # Count of isEditDistanceOne

    i = 0
    j = 0
    while i < m and j < n:
        # If current characters dont match
        if original[i] != changed[j]:
            if count == 1:
                return false

            # If length of one string is
            # more, then only possible edit
            # is to remove a character
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:    # If lengths of both strings is same
                i+=1
                j+=1

            # Increment count of edits
            count+=1

        else:    # if current characters match
            i+=1
            j+=1

    # if last character is extra in any string
    if i < m or j < n:
        count+=1

    return count == 1

bark barak

'''
1.7  Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''
#kinda wack
def rot(a1):


'''
1.9 Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
call to isSubs t rin g [e.g., "wate r bottle " is a rotation of 'erbottlewat"),
'''
def isSubstring(s1,s2):

    tmp = s1 + s1
    if (tmp.count(s2) != 0): return True
