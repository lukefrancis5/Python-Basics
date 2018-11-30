# Get user email address
email = input("What is your email ?:").strip()

# Slice out username
user = email[:email.index("@")]

# Slice domain name
domain = email[email.index("@") + 1:]

# Format message
output = "Your username is {} your domain name is {}".format(user,domain)

# Display output message
print(output)
