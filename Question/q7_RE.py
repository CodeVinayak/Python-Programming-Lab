import re

text = """Hello world! 
Hello, how are you? 
I hope you are doing well. 
Hello, it's a beautiful day."""

print("Counting the Hello word using regular expression :")
count = re.findall("hello", text, re.IGNORECASE)
print(len(count))

print("Original Text is : "+text)
print("Replacing Hello word with Hi word using regular expression :")
replaced_text = re.sub("Hello", "Hi", text)
print(replaced_text)