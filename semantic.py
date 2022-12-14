import spacy

nlp = spacy.load("en_core_web_md")

tokens = nlp('cat apple monkey banana ')

# Spacy will determine how similar the words are in the tokens variable
for token1 in tokens:
    for token2 in tokens:
        print(token1," - ", token2, "Similarity = ", token1.similarity(token2))

# The result of the above code showed how spacy was able to determine similarities based on whether words
# were related in a way such as whether they belong in the animal group. Spacy was also able to determine the
# behaviours of the animal with other words such as how monkeys eat bananas. This increased the similarity score
# between the two.

# -------------------------------------------------------------------------------
print("\nSecond example\n")

tokens_test2 = nlp('Human Computer Games Television ')

# Spacy will determine how similar the words are in the tokens_test2 variable
for token1 in tokens_test2:
    for token2 in tokens_test2:
        print(token1," - ", token2, "Similarity = ", token1.similarity(token2))

# In this second example we see a low score for all of these matches, however the highest score to the human was a
# computer. This is very interesting as a computer and a human both have the ability to learn and store
# information. Whether Spacy recognises this is fascinating.

# ----------------------------------------------------------------------

# en_core_web_sm compared to en_core_web_md:

# After testing both of these, I can see that en_core_web_sm seems to find less similarities between differing words
# compared to en_core_web_md. Despite this, en_core_web_sm does seem to run/load faster than en_core_web_md, making
# en_core_web_sm a better choice for faster results, however a reduction in accuracy would be the compromise for that.

