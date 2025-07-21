import re

text = "My name is Sivaraj. My email is sivaraj@example.com and my website is https://sivaraj.dev"

# Regex pattern to match email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all matches
matches = re.findall(pattern, text)

# Print results
print("Matches found:")
for match in matches:
    print(match)
