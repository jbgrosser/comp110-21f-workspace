"""Counting letters in a string."""

__author__ = "730475279"


# Begin your solution here...
letter: str = input("What letter do you want to seach for?: ")
word: str = input("Enter a word: ")
count: int = 0
i: int = 0
while letter != word[i]:
    i = i + 1
count = i + 1
print("Count: " + str(count))