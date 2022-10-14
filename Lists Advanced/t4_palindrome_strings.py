sequence_of_words = input().split()
palindrome = input()
list_of_palindromes = [pal for pal in sequence_of_words if pal == pal[::-1]]
palindrome_count = [pal for pal in sequence_of_words if pal == palindrome]
print(list_of_palindromes)
print(f"Found palindrome {len(palindrome_count)} times")