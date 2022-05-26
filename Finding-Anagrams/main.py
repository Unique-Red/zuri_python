# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if (sorted(word) == sorted(anagram)):
        print("anagrams")
        return True
    else:
        print("not anagram")
        return False



word = "red"
anagram="rex"
find_anagram(word, anagram)

