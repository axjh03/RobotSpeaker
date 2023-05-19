import os
if __name__ == "__main__":
    while True:
        text = str(input("What do you want to say? "))
        query = "say" + " " + text
        os.system(query)
    