from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_books_rating_one(self):
        collector = BooksCollector()
        collector.add_new_book('Джедайские техники')
        assert collector.books_rating['Джедайские техники'] == 1

    def test_add_new_book_books_add_same_books_not_impossible(self):
        collector = BooksCollector()
        collector.add_new_book('Джедайские техники')
        collector.add_new_book('Джедайские техники')
        assert collector.books_rating['Джедайские техники'] == 1

    def test_set_book_rating_range_max10(self):
        collector = BooksCollector()
        collector.add_new_book('Корги по имени Генри')
        collector.set_book_rating('Корги по имени Генри', 10)
        assert collector.books_rating['Корги по имени Генри'] == 10

    def test_set_book_rating_range_11_show_error(self):
        collector = BooksCollector()
        collector.add_new_book('Мир глазами кота Боба')
        collector.set_book_rating('Мир глазами кота Боба', 11)
        assert collector.books_rating['Мир глазами кота Боба'] != 11

    def test_set_book_rating_not_exists_book_show_empty(self):
        collector = BooksCollector()
        collector.set_book_rating('Коты и кошки', 5)
        assert collector.books_rating == {}

    def test_get_book_rating_show_book_with_rating_2(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Сборник рассказов')
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Война и мир', 9)
        collector.set_book_rating('Сборник рассказов', 1)
        collector.set_book_rating('Мастер и Маргарита', 2)
        collector.get_books_rating()
        assert collector.books_rating.get('Мастер и Маргарита') == 2

    def test_get_books_with_specific_rating_only_rating_3(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Сборник рассказов')
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Война и мир', 3)
        collector.set_book_rating('Сборник рассказов', 7)
        collector.set_book_rating('Мастер и Маргарита', 4)
        collector.get_books_with_specific_rating(3)
        assert len(collector.get_books_with_specific_rating(3)) == 1 and collector.get_books_with_specific_rating(
            3) == ['Война и мир']

    def test_get_books_with_specific_rating_only_rating_11_show_error(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Сборник рассказов')
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Война и мир', 3)
        collector.set_book_rating('Сборник рассказов', 11)
        collector.set_book_rating('Мастер и Маргарита', 4)
        collector.get_books_with_specific_rating(11)
        assert len(collector.get_books_with_specific_rating(11)) == 0 and collector.get_books_with_specific_rating(11) == []

    def test_get_books_with_specific_rating_only_rating_0_show_error(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Сборник рассказов')
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Война и мир', 0)
        collector.set_book_rating('Сборник рассказов', 11)
        collector.set_book_rating('Мастер и Маргарита', 4)
        collector.get_books_with_specific_rating(0)
        assert len(collector.get_books_with_specific_rating(11)) == 0

    def test_get_books_rating_add_three_books_show_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Белый Бим черное ухо')
        collector.add_new_book('Два капитана')
        collector.add_new_book('Вишневый сад')
        assert len(collector.get_books_rating()) == 3

    def test_get_books_rating_add_zero_books_show_zero_books(self):
        collector = BooksCollector()
        assert len(collector.get_books_rating()) == 0

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тихий Дон')
        collector.add_new_book('Гарри Поттер и Философский камень')
        collector.add_book_in_favorites('Тихий Дон')
        assert len(collector.favorites) == 1 and collector.favorites == ['Тихий Дон']

    def test_add_book_in_favorites_add_not_exsits_book_show_error(self):
        collector = BooksCollector()
        collector.add_new_book('Путь домой')
        collector.add_new_book('Гарри Поттер и Тайная комната')
        collector.add_book_in_favorites('Тихий Дон')
        assert collector.favorites == []

    def test_delete_book_from_favorites_delete_exsits_book(self):
        collector = BooksCollector()
        collector.add_new_book('К себе нежно')
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('К себе нежно')
        collector.delete_book_from_favorites('Гарри Поттер и Узник Азкабана')
        assert len(collector.favorites) == 1 and collector.favorites == ['К себе нежно']

    def test_delete_book_from_favorites_delete_not_exsits_book(self):
        collector = BooksCollector()
        collector.add_new_book('К себе нежно')
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        collector.delete_book_from_favorites('К себе нежно')
        assert len(collector.favorites) == 1 and collector.favorites == ['Гарри Поттер и Узник Азкабана']

    def test_get_list_of_favorites_books_add_two_books_show_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Сборник рецептов')
        collector.add_new_book('Гарри Поттер и Кубок Огня')
        collector.add_book_in_favorites('Гарри Поттер и Кубок Огня')
        collector.add_book_in_favorites('Сборник рецептов')
        collector.get_list_of_favorites_books()
        assert len(collector.favorites) == 2 and collector.favorites == ['Гарри Поттер и Кубок Огня',
                                                                         'Сборник рецептов']
