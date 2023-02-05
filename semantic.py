import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# I think it's interesting how 'cat' and 'monkey' are considered more similar
# than 'monkey' and 'banana', even though I would consider them more similar:
# monkeys are well associated with bananas and the only similarity a cat and a monkey have
# is that their both animals.

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# working with vectors
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# working with sentences
sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
"Hello, there is my car",
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

