in_str = input("Enter a string: ")

# via iterating
new_str = ""
for c in in_str:
    new_str += c if c.isalpha() else "*"
print("New string: ", new_str)

# one liner
# new_str = "".join([c if c.isalpha() else "*" for c in in_str])

# via indexing
new_str = ""
for i in range(len(in_str)):
    new_str += in_str[i] if in_str[i].isalpha() else "*"
print("New string: ", new_str)
