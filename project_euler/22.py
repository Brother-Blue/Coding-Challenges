"""
Using res/names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by 
its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

def value_of_names(file_path):
    with open(file_path, "r") as f:
        lines = f.readline().split(",")
        # Split the read line into a list
        names = [name.strip("\"") for name in lines]
        # Sort one of the lists
        names.sort()
        score = 0
        for name in names:
            name_val = 0
            # index +1 because the question does not consider index 0
            name_index = names.index(name) + 1
            # Convert all names to uppercase to avoid different case values: a vs A
            for ch in name.upper():
                # A = 65 on ascii table
                name_val += (ord(ch) - 64)
            score += (name_val * name_index)
        print(f"Name score: {score}")

if __name__ == '__main__':
    value_of_names("../res/names.txt")