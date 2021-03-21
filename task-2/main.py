file_name = "my_quote.txt"

new_file = open(file_name, "w")
new_file.close()


def update_file(file_name, quote):
    with open(file_name, "a") as f:
        f.write("This is an update\n")
        f.write(quote)
        f.write("\n\n")


for i in range(3):
    quote = input("Enter your favourite quote: ")
    update_file(file_name, quote)

new_file = open(file_name, "r")
print(new_file.read())
new_file.close()
