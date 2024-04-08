# Convert to a vector of words, removing periods
library(stringi)

# Example sentence
test.sentences <- c("This is an example sentence with periods.Tried sentence to word tokenization")


stringi::stri_extract_all_words(test.sentences)
print("hi5")