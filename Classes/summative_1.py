import re
from collections import Counter

# Function to count specific words
def count_specific_word(article, specific_word):
    # Converts inputs into strings (ensures the function works even if non-string is passed)
    article_str = str(article)
    search_word_str = str(specific_word)
    
    # Extract all words (letters, numbers, underscore). Ignores punctuation.
    article_str_as_ls = re.findall(r'\w+', article_str)
    length_of_article_str_as_ls = len(article_str_as_ls)

    # Counters
    word_count = 0
    specific_word_count = 0

    # Loop through each word in the article
    while word_count < length_of_article_str_as_ls:

        # Current word matches the search word, increase counter
        if article_str_as_ls[word_count] == search_word_str:
            specific_word_count = specific_word_count + 1
        word_count = word_count + 1
    
    return specific_word_count

# Function to identify most common word
def identify_most_common_word(article):
    article_str = str(article)

    # If string empty-> return none
    if article_str == "":
        return None
    else:
        # Extract words
        article_str_as_ls = re.findall(r'\w+', article_str)
        counts_dict = Counter(article_str_as_ls) # Counts frequency of each word

        max_frequency_element = max(counts_dict.items(),key= lambda item:item[1])


        most_common_words_ls = []

        # Multiple words share same max frequency return all of them
        for element, freq in counts_dict.items():

            if freq == max_frequency_element[1]: 
                most_common_words_ls.append(element)

        return most_common_words_ls

# Calculate average word length
def calculate_average_word_length(article):
    article_str = str(article)

    # Empty string -> return zero
    if article_str == "":
        return 0
    else:
        
        article_str_as_ls = re.findall(r'\w+', article_str)
        length_of_article_str_as_ls = len(article_str_as_ls)

        lengths_of_words_ls = []

        # Store length for each word
        for word in article_str_as_ls:
            length_of_word = len(word)
            lengths_of_words_ls.append(length_of_word)

        # Compute average
        average_word_length = sum(lengths_of_words_ls) / length_of_article_str_as_ls

        return average_word_length

# Counting paragraphs
def count_paragraphs(article):
    article_str = str(article)
    
    # if empty string return 1
    if article_str == "":
        return 1
    else:
        # Split paragraph by blank line 
        article_str_as_ls = re.split(r'\n\n', article_str)
        number_of_paragraphs = len(article_str_as_ls)

        return number_of_paragraphs

# Counting sentences 
def count_sentences(article):
    article_str = str(article)

    if article_str == "":
        return 1
    else:
        """ 
        The pattern matches anything that begins with a capital letter, 
        followed by anything excluding . or ! or ?, followed by . or ! or ?
        """
        article_str_as_ls = re.findall(r'[A-Z][^\.!?]*[\.!?]', article_str)

        number_of_sentences = len(article_str_as_ls)

        return number_of_sentences

#Test cases for article
result1_1 = count_specific_word("This is a test.","test")
result1_2 = count_specific_word("apple apple banana banana banana","banana")
result1_3 = count_specific_word("","test")

result2 = identify_most_common_word("apple apple banana banana banana")

result3_1 = calculate_average_word_length("This is a test.")
result3_2 = calculate_average_word_length("apple apple banana banana banana")
result3_3 = calculate_average_word_length("")

result4_1 = count_paragraphs("This is a test.")
result4_2 = count_paragraphs("apple apple banana banana banana")
result4_3 = count_paragraphs("")

result5_1 = count_sentences("This is a test.")
result5_2 = count_sentences("apple apple banana banana banana")
result5_3 = count_sentences("")

print(result1_1)
print(result1_2)
print(result1_3)

print(result2)

print(result3_1)
print(result3_2)
print(result3_3)

print(result4_1)
print(result4_2)
print(result4_3)

print(result5_1)
print(result5_2)
print(result5_3)



    




