# from class

with open("emails.txt") as file:
    emails = file.read()

# So the problem we encountered is thhat the emaisl are one big long string, we need to split them into individual elements
# the split function can split a vairables contents based on an argument. in this case it splits at commas and the space after them
# also turns the huge string into an array automatically
duplicate_emails = emails.split(", ")

clean_email_list = []

for email in duplicate_emails:
    if email not in clean_email_list:
        clean_email_list.append(email)

print(clean_email_list)


with open ("duplicate_free_emails.txt", "w") as file:
    for email in clean_email_list:
        file.write(email)
        file.write("\n")
