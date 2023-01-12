"""
My understanding of a palindrome is:
A palindrome is a number that is the same
when spell foward or backword.

If that is the case, this code should work.

Note: Both case must match for it to be a palindrome.

Meaning Aba is not the same as aba
"""
def solution(palindrome):
    # To start with, an empty string or a single character would be a palindrome
    if len(palindrome) <= 1:
        return 1
    # Since we cannot use a loop
    #Check if the starting and ending string are identical
    # If it is not, lets just retrun zero immediately
    if palindrome[0] != palindrome[-1]:
        return 0
    # If the first test casse passes we can now check for the remaining string character
    return solution(palindrome[1:-1])



print(solution("Racecar"))  # it's not palindrome so it prints prints 0
print(solution("Racecar"))  # it's palindrome so it prints prints 1
print(solution("a"))  # it's is a single character so it prints prints 1
print(solution(""))  # it's an empty string so it prints prints 1
