...
Is Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
...

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {} #declaring hashtable for each

        for i in range(len(s)): #iterating through string
            countS[s[i]] = 1 + countS.get(s[i], 0) #getting hash counts of each value
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
