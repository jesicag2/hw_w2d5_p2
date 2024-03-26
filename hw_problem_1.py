#HW2_P1: Product Review Analysis

# Task 1: Keyword Highlighter
'''
Write a program that searches through a series of product reviews for keywords 
such as "good", "excellent", "bad", "poor", and "average". Print out each review 
with the keywords in uppercase so they stand out.
'''

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]
for review in reviews:
    for keyword in keywords:
        if keyword in review:
            new_review = review.replace(keyword, keyword.upper())
    print(new_review)


# Task 2: Sentiment Tally
'''
Develop a function that tallies the number of positive and negative words in each 
review. Use a predefined list of positive and negative words to check against. 
The function should return the count of positive and negative words for each review.
'''
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def pos_neg_count(reviews):
    for review in reviews:
        positive_count = 0  
        negative_count = 0  
        review_lower = review.lower() 
        for positive in positive_words:
            if positive.lower() in review_lower:
                positive_count += 1
        for negative in negative_words:
            if negative.lower() in review_lower:
                negative_count += 1
        print(f"Positive word count in this review is: {positive_count}")
        print(f"Negative word count in this review is: {negative_count}")

pos_neg_count(reviews)


# Task 3: Review Summary
''' 
Implement a script that takes the first 30 characters of a review and appends "…" to 
create a summary. Ensure that the summary does not cut off in the middle of a word.
'''
