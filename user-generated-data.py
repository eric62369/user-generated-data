def print_list_contents(data_list):
    print("Data contents: [")
    for data in data_list:
        print("    " + data, end="")
    print("]")

file_name = "None"
user_file = input("Which file to add to? (yes.txt or no.txt)\n")
if user_file == "yes.txt" or user_file == "no.txt":
    file_name = user_file
else:
    raise ValueException("Did not give yes.txt or no.txt")

print("Opening up: %s" % file_name)

# Store all data to be added
data_list = []

with open(file_name, 'a') as file:
    user_message = input("Starting now: Type in '<quit>' to stop the session.\n")
    while not user_message == "<quit>":
        data_list.append(user_message + ",\n")
        user_message = input("Added '" + user_message + "'\n")
    file.writelines(data_list)

print(file_name, "successfully closed.")
print("Added", len(data_list), "new items during this session.")
print_list_contents(data_list)
