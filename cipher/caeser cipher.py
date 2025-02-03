def encrypt(text, s):
  result = ""
  for char in text:
    if 'A' <= char <= 'Z': 
      # Calculate the position of the character (0-25)
      p = ord(char) - ord('A')
      # Apply the Caesar Cipher formula
      c = (p + s) % 26
      # Convert back to character
      result += chr(c + ord('A'))
    else:
      result += char 
  
  return result

# Check the above function
text = "HLO"
s = 4
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))
