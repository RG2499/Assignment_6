'''
CIS 122 Fall 2018 Lab 7
Author: Jacob Rammer
Partner: None
Description: Display the stats of the file
'''


def count():
    """Count the lines in txt file
    Count the number of lines in the text file
    :return: Line count
    """
    fin = open("words_alpha.txt")
    line_count = 0
    for line in fin:
        line = line.strip()
        line_count += 1
    fin.close()
    return line_count


def longest_word():
    """Find longest word
    Find the longest word in the text file
    :return: The longest word as a string
    """
    doc_longest_word = ""
    fin = open("words_alpha.txt")
    for line in fin:
        line = line.strip()
        if len(line) > len(doc_longest_word):
            doc_longest_word = line
    fin.close()
    return doc_longest_word
    #  print("Longest word is: ", longest_word, " (", len(longest_word), ")", sep="")


def shortest_word():
    """Find the shortest word
    Find a word that is the shortest and break instantly
    :return:  Shortest word as a string
    """
    doc_shortest_word = ' '
    fin = open("words_alpha.txt")
    for line in fin:
        line = line.strip()
        if len(line) <= len(doc_shortest_word):
            doc_shortest_word = line
            break
    fin.close()
    return doc_shortest_word
    #  print("Shortest word is: ", shortest_word, " (", len(shortest_word), ")", sep="")


def is_palindrome():
    """Determine if a word is a palindrome
    Search whole document for palindromes (words that are the same reversed)
    :return: Number of palindromes
    """
    line_count = count()
    palindrome = 0
    fin = open("words_alpha.txt")
    for line in fin:
        line = line.strip()
        p_word = line[::-1]
        if line == p_word:
            palindrome += 1
    fin.close()
    return palindrome
    #  print("Palidromes: ", palindrome, "(", round(palindrome / line_count * 100, 2), "%)", sep="")


def calculate_start_char():  # Incomplete
    fin = open("words_alpha.txt")
    a = 0
    for line in fin:
        line = line.strip()
        if line[0:1] == "a":
            a += 1
    print(a)


def print_results():
    """Print results
    Call all the functions in program and calculate the results
    :return: Void (as of now)
    """
    line_count = count()
    doc_longest_word = longest_word()
    doc_shortest_word = shortest_word()
    palindrome = is_palindrome()

    print("Longest word is: ", doc_longest_word, " (", len(doc_longest_word), ")", sep="")
    print("Shortest word is: ", doc_shortest_word, " (", len(doc_shortest_word), ")", sep="")
    print("Palidromes: ", palindrome, "(", round(palindrome / line_count * 100, 2), "%)", sep="")


# count()
# longest_word()
# shortest_word()
# is_palindrome()
# print_results()
calculate_start_char()
