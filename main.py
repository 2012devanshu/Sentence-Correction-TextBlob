
__author__ : "@rockdevu"

#pip install textblob
from textblob import TextBlob as tb
print("\n")
text = tb(input("Enter sentence : "))
print("\n")
print("Corrected Sentence : ", text.correct())
print("\n")
