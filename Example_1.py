""" 
My library helpful in this tasks. You need to generate somthing like this:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Before i hardcode English alphabet in some variable, but now it looks like this:"""
from Alphabet import English


alphabeth = English()
n = int(input("Give me a number - "))
srting = []
answer = []
for i in range(0, n):
    srting.append(alphabeth.lowerсhars()[i])
s = '-'.join(srting)
new_line = s[::-1] + s[1:]
answer.append(new_line)
n -= 1
j = 2
while n > 0:
    delete = srting.pop(0)
    s = '-'.join(srting)
    new_line = '-'*j+s[::-1]+s[1:]+'-'*j
    answer.append(new_line)
    j += 2
    n -= 1
for i in range(len(answer)-1, -1, -1):
    print(answer[i])
for i in range(1, len(answer)):
    print(answer[i])
