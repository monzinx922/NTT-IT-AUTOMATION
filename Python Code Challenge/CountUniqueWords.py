# Challenge: Write a python function to count the number of unique words and how often each occurs
# input: path to a text file
# output: print message with: total number of words, top 20 most frequent words, number of occurences for top 20

def count_word(file_path):
    # open file for read
    with open(file_path,"r", encoding="utf-8") as file:
        lines = file.read()

        lines_split = lines.split()

        print("total words = ",len(lines_split))
        counter = {}
        for word in lines_split:
            # check only lower text convert them all to lower
            word = word.lower()

            # Count the word to dictionary, if it has not the word yet, set it value to 1 (it will error so I use try and except)
            try:
                counter[word] += 1
            except:
                counter[word] = 1
        
        # Sort dictionary and get only top 20
        top_20 = sorted(counter.items(),key=lambda x: x[1], reverse=True)[:20]

        print("TOP 20 Words using in this file")

        for key,value in top_20:
            print(f"{key} : {value}")

        

count_word("100-0.txt")