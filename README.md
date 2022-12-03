# qa_python

============================= test session starts ==============================
platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10
cachedir: .pytest_cache
rootdir: /Users/katamosiyash/yandex/qa_python
collected 17 items                                                             

tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED     [  5%]
tests.py::TestBooksCollector::test_add_new_book_books_rating_one PASSED  [ 11%]
tests.py::TestBooksCollector::test_add_new_book_books_add_same_books_not_impossible PASSED [ 17%]
tests.py::TestBooksCollector::test_set_book_rating_range_max10 PASSED    [ 23%]
tests.py::TestBooksCollector::test_set_book_rating_range_11_show_error PASSED [ 29%]
tests.py::TestBooksCollector::test_set_book_rating_not_exists_book_show_empty PASSED [ 35%]
tests.py::TestBooksCollector::test_get_book_rating_show_book_with_rating_2 PASSED [ 41%]
tests.py::TestBooksCollector::test_get_books_with_specific_rating_only_rating_3 PASSED [ 47%]
tests.py::TestBooksCollector::test_get_books_with_specific_rating_only_rating_11_show_error PASSED [ 52%]
tests.py::TestBooksCollector::test_get_books_with_specific_rating_only_rating_0_show_error PASSED [ 58%]
tests.py::TestBooksCollector::test_get_books_rating_add_three_books_show_three_books PASSED [ 64%]
tests.py::TestBooksCollector::test_get_books_rating_add_zero_books_show_zero_books PASSED [ 70%]
tests.py::TestBooksCollector::test_add_book_in_favorites_add_one_book PASSED [ 76%]
tests.py::TestBooksCollector::test_add_book_in_favorites_add_not_exsits_book_show_error PASSED [ 82%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_delete_exsits_book PASSED [ 88%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_delete_not_exsits_book PASSED [ 94%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_add_two_books_show_two_books PASSED [100%]

============================== 17 passed in 0.01s ==============================
