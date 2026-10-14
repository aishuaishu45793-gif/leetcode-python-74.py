# Program 146: Check Anagrams

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")