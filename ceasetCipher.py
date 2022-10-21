# Julius Caesar protected his confidential information by encrypting it using a cipher.
# Caesar's cipher shifts each letter by a number of letters.
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
def CeaserCipher(s, k):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = abc.upper()
    encrypted = ""
    for i in range(len(s)):
        if s[i] in abc:
            encrypted += abc[(((abc.find(s[i]))+k) % 26)]
        elif s[i] in ABC:
            encrypted += ABC[(((ABC.find(s[i]))+k) % 26)]
        else:
            encrypted += s[i]
    return (encrypted)


print(CeaserCipher("There's s-a-starman", 3))
