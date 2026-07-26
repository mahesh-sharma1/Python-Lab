def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# Test with different strings
# words = ["Python", "Hello", "Madam", "12345"]
word = input("Enter a string: ")
# for word in words:
print(f"Original: {word} -> Reversed: {reverse_string(word)}")