# https://youtu.be/0yyX5utQ4Bc
# https://youtu.be/0CknqzGde-M

"""
Module for find_recent_cooding_books function

Author: John
Date: 220727
"""

def find_recent_coding_books(recent_books_pth, coding_book_pth):
    '''
    Takes data from pths and returns the interction containing recent_coding_books
    
    Args:
        recent_books_pth: (str) path for file containing all recent books
        coding_books_pth: (str) path for file containing all coding books
    Return:
        recent_coding_books (set) takes intersection of data in both paths
    '''
    with open(recent_books_pth, encoding='UTF8') as pth_one:
        recent_books = pth_one.read().split('\n')
    with open(coding_book_pth, encoding='UTF8') as pth_two:
        coding_books = pth_two.read().split('\n')
    recent_coding_books =  set.intersection(set(recent_books),set(coding_books))
    return recent_coding_books

if __name__ == "__main__":
    RECENT_CODING_BOOKS = find_recent_coding_books('books_published_last_two_years.txt',
                                                   'all_coding_books.txt')
    print(RECENT_CODING_BOOKS)

# make your code reusable by creating a function
# if __name__ == "__main__"
# running your script from terminal : python script_name.py
# Two ways to automate clean code are with:
# 1.pylint script_name.py
# 2.autopep8 --in-place --aggressive --aggressive script_name.p
