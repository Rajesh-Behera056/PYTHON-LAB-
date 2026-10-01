sequence = "PythonProgramming"

unique = list(dict.fromkeys(sequence))

uppercase = list(map(str.upper,unique))
lowercase = list(map(str.lower,unique))

print("Original Sequence:",sequence)
print("Uppercase:",uppercase)
print("Lowercase:",lowercase)