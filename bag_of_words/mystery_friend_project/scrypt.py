from goldman_emma_raw import goldman_docs
from henson_matthew_raw import henson_docs
from wu_tingfang_raw import wu_docs
# import sklearn modules here:


# Setting up the combined list of friends' writing samples
friends_docs = goldman_docs + henson_docs + wu_docs
# Setting up labels for your three friends
friends_labels = [1] * 154 + [2] * 141 + [3] * 166

# Print out a document from each friend:




mystery_postcard = """
My friend,
From the 10th of July to the 13th, a fierce storm raged, clouds of
freeing spray broke over the ship, incasing her in a coat of icy mail,
and the tempest forced all of the ice out of the lower end of the
channel and beyond as far as the eye could see, but the _Roosevelt_
still remained surrounded by ice.
Hope to see you soon.
"""

# Create bow_vectorizer:

# Define friends_vectors:

# Define mystery_vector: 


# Define friends_classifier:

# Train the classifier:

# Change predictions:
predictions = ["None Yet"]

mystery_friend = predictions[0] if predictions[0] else "someone else"

# Uncomment the print statement:
#print("The postcard was from {}!".format(mystery_friend))