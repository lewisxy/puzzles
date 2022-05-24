"""
Copyright (c) 2022 lewisxy

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Puzzle URL:
# https://www.youtube.com/watch?v=bOXCLR3Wric

# p[i] at k = number of subsets among all subsets of {1, ..., k}
# in which the sum of all elements of that subset = i mod 5

# divisible by d
d = 5
# compute p among all subsets of {1, ..., n}
n = 2000

# initialize p at k = 0
p = [1, 0, 0, 0, 0]

# p[i+1] = p[i] + p[table[k % 5][i]]
table = [[0, 1, 2, 3, 4],
         [4, 0, 1, 2, 3],
         [3, 4, 0, 1, 2],
         [2, 3, 4, 0, 1],
         [1, 2, 3, 4, 0]]

# compute p at k = n by looping n times from p at k = 0
for k in range(n):
    p_next = list(p)
    for i in range(d):
        p_next[i] += p[table[k % 5][i]]
    p = p_next

print(p[0])

# some verifications
# sum of p at k = 2000 should be equal to 2^2000
#res = p[0] + p[1] + p[2] + p[3] + p[4]
#print(res == 2 ** 2000)
