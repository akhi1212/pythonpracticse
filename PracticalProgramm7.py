"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
"""

from collections import Counter
if __name__ == '__main__':
    n = int(input("Please enter your number: "))
    arr = Counter(map(int, n.split())).keys()
    arr.sort()
    print(arr[-2])