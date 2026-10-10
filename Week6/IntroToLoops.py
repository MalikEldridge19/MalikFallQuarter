prompt = input("Do you want to print the list? yes or no?")
geniuses = ["Jeremy", "Kevin", "DJ", "Tyson", "Tayvion",]

while (prompt == "yes"):
    for genius in geniuses: 
        print(genius)
    prompt = input("Do you want to print the list again? yes or no?")
