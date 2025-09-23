text = input("Enter your text: ")
#text = "Hello world! Hello Python world." ---(использовал для тестов)---

#lst = text.split() 

counts = {}
for word in text.split:
    word = word.lower().strip(",.{}[]()!?")
    
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
    #if word:
    #   counts[word] = count.get(word, 0) + 1     ---(узнал в чат гпт)---

sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True) # ---(Сам ещё не проходил, но нашёл в интернете и подстроил под себя (можно было сортировать пузырьком))---
print(sorted_words)