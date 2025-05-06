#Exercise 3: Working on a paragraph
#Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
#Paste it to your code, and store it in a variable.
#Let’s analyze the paragraph. Print out a nicely formatted message saying:
#How many characters it contains (this one is easy…).
#How many sentences it contains.
#How many words it contains.
#How many unique words it contains.
#Bonus: How many non-whitespace characters it contains.
#Bonus: The average amount of words per sentence in the paragraph.
#Bonus: the amount of non-unique words in the paragraph.

interesting_paragraph = (
    "artificial intelligence (AI), the ability of a digital computer or computer-controlled robot to perform tasks "
    "commonly associated with intelligent beings. The term is frequently applied to the project of developing systems "
    "endowed with the intellectual processes characteristic of humans, such as the ability to reason, discover meaning, "
    "generalize, or learn from past experience. Since their development in the 1940s, digital computers have been "
    "programmed to carry out very complex tasks—such as discovering proofs for mathematical theorems or playing chess—"
    "with great proficiency. Despite continuing advances in computer processing speed and memory capacity, there are as "
    "yet no programs that can match full human flexibility over wider domains or in tasks requiring much everyday "
    "knowledge. On the other hand, some programs have attained the performance levels of human experts and professionals "
    "in executing certain specific tasks, so that artificial intelligence in this limited sense is found in applications "
    "as diverse as medical diagnosis, computer search engines, voice or handwriting recognition, and chatbots."
)

# How many characters it contains
print("Number of characters:", len(interesting_paragraph))

# How many sentences it contains
sentences = interesting_paragraph.split(".")
# Remove empty strings caused by trailing periods
sentences = [s for s in sentences if s.strip()]
print("Number of sentences:", len(sentences))

# How many words it contains
words = interesting_paragraph.split()
print("Number of words:", len(words))

# How many unique words it contains
unique_words = set(words)
print("Number of unique words:", len(unique_words))

# Bonus: How many non-whitespace characters it contains
non_whitespace_characters = len(interesting_paragraph.replace(" ", ""))
print("Number of non-whitespace characters:", non_whitespace_characters)

# Bonus: The average amount of words per sentence in the paragraph
average_words_per_sentence = len(words) / len(sentences)
print("Average amount of words per sentence in the paragraph:", average_words_per_sentence)

# Bonus: The amount of non-unique words in the paragraph
non_unique_words = len(words) - len(unique_words)
print("Number of non-unique words:", non_unique_words)
