# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./Reading-Text-Files/story.txt") as f:
        lines = f.read()

        print(lines)
    return "Hello World"
    
read_file_content("./Reading-Text-Files/story.txt")


def count_words():
    text = read_file_content("./Reading-Text-Files/story.txt")
    # [assignment] Add your code here
    file = open("./Reading-Text-Files/story.txt", "rt")
    data = file.read()
    words = data.split()
    
    count=0
    for word in words:
        count += 1
        print(f"line {count}: {word}")
   
    return {"as": 10, "would": 20}


count_words()