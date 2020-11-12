# Get the file
file = open('')


# [INIT] Declare a list
wordList = list()

for line in file:
    # CREATE AN ARRAY & call it lineWordArray
    lineWordArray = line.rstrip().split()

    # Ready each value in the array created within this loop
    for word in lineWordArray:
        # Check if it is in the list i created above
        if word in wordList:
            continue
        else :
            wordList.append(word)

# Organize the list
wordList.sort()

# Print final array!
print('finalWordList:', wordList)
