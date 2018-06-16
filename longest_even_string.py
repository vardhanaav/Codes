import sys, random

#print the first longest even string, for last put >=
max_len = -9999
string = input().split(" ")
for s in string:
    if len(s)%2 == 0 and len(s) > max_len:
        max_len = len(s)
        max_str = s

print(list(reversed(string)))
print(max_len, max_str)

