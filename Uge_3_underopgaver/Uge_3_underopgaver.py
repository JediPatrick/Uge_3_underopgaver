import matplotlib.pyplot as plt
from wordcloud import WordCloud

from Uge_3_underopgave_2 import underopgaveTO
from Uge_3_underopgave_3 import underOpgaveTre



#open file with 
listOfNames = []
with open('names.txt', 'r') as file:
    for line in file:
        stringName = str(line.strip())
        stringName = stringName.replace(" ", "").replace(".", "").replace("-", "")
        listOfNames.append(stringName)


#sort names alphabetical
listOfNames.sort()
#output names to file
with open('namesSortedAlphabetical.txt', 'w') as file:
    for name in listOfNames:
        file.write(f"{name}\n")

#sort names by length
def lenghtOfName(e):
    return len(e)

listOfNames.sort(key=lenghtOfName)

#output names to file
with open('namesSortedByLength.txt', 'w') as file:
    for name in listOfNames:
        file.write(f"{name}\n")

dictOfLetters = {}
wordCloudString = ""
for name in listOfNames:
    char_array = list(name)
    for char in char_array:
        char = char.lower()
        wordCloudString += f" {char}"
        if char in dictOfLetters:
            dictOfLetters[f"{char}"] += 1
        else:
            dictOfLetters[f"{char}"] = 1
keys = list(dictOfLetters.keys())   
values = list(dictOfLetters.values())

plt.bar(keys, values, color='blue', alpha=0.7, edgecolor='black')

# Add title and labels
plt.title('Bar Chart Example (Soejlediagram)')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.grid(axis='y', alpha=0.75)
fname = "soejlediagram.png"
plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)




wordcloud = WordCloud(width=1600, height=800, background_color='white', 
                      colormap='viridis', random_state=41, max_words=10000, stopwords=set()).generate(wordCloudString)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.title('Word Cloud of letters')
fname = "wordcloud.png"
plt.savefig(fname, transparent=None, dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto', backend=None)

#plt.hist(data, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
underopgaveTO()
underOpgaveTre()
