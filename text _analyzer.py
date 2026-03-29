text=input("Enter a paragraph:")
char_count=len(text)
print("Characters:",char_count)
words=text.split()
words_count=len(words)
print("word count",words_count)
sentence_count=text.count('.')+text.count('!')+text.count('?')
print("sentence count",sentence_count)
freq={}
for word in words:
    word=word.lower()
    freq[word]=freq.get(word,0)+1
most_common=max(freq,key=freq.get)
clean_text=text=text.replace(" ","").lower()
if clean_text == clean_text[ : :-1]:
    palindrome=True
else:
    palindrome=False  
reversed_words=[word[ : :-1]for word in words]
reversed_text=" ".join(reversed_words)
numbers=[]
for char in text: 
    if char.isdigit():
        numbers.append(char)
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for char in text.lower():
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print("Most common word:",most_common)
print("Plindrome: ",palindrome)
print("Reversed words:",reversed_text)
print("Numbers",numbers)
print("Vowels:",vowel_count)
print("consonant: ",consonant_count)






