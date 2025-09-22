text = """Hello, world! Hello Python.
This is a test. Hello - test."""

lines = text.split('\n')

counts = {}

for line in lines:
    tokens = line.split()
    for token in tokens:
        token = token.lower().strip(".,!?;:\"'()[]{}")

        if token:
            if token in counts:
                counts[token] += 1
            else:
                counts[token] = 1

total_words = sum(counts.values())
unique_words = len(counts)

top_words = []
for word in counts:
    top_words.append((counts[word], word))

top_words.sort(reverse = True)

print("Total word count: ", total_words)
print("Number of unique words: ", unique_words)
print("Top 5 words:")
for count, word in top_words[:5]:
    print(word, '-', count)

