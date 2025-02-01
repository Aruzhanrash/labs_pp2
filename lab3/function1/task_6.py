def reverse_words(sentence):
    words = sentence.split() 
    words.reverse()  
    return words  

input_sentence = input("Enter a sentence: ")
print(reverse_words(input_sentence))
