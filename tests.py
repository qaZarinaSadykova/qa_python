import pytest
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
        # добавляем две книги
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # устанавливаем книге жанр - Фантастика
    def test_set_book_genre_fantasy(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"

    # получаем жанр книги - Ужасы
    def test_get_book_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        assert collector.get_book_genre("Оно") == "Ужасы"

    # выводим список книг с определнным жанром - Фантастика
    @pytest.fixture
    def filled_collector(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        collector.add_new_book("Мы")
        collector.set_book_genre("Мы", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        return collector

    @pytest.mark.parametrize("genre, expected", [("Фантастика", ["1984", "Мы"]), ("Ужасы", ["Оно"])])
    def test_get_books_with_specific_genre_fantasy(self, filled_collector, genre, expected):
        assert filled_collector.get_books_with_specific_genre("Фантастика") == ["1984", "Мы"]

    # выводим словарь из всех жанров в добавленных книгах
    def test_get_books_genre_in_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        assert collector.get_books_genre() == {"1984": "Фантастика", "Оно": "Ужасы"}

    # выводим книги для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.books_genre = {
            "1984": "Фантастика",
            "Незнайка": "Мультфильмы",
            "Эркюль Пуаро": "Детективы",
            "Маленький принц": "Мультфильмы",
            "Оно": "Ужасы"
        }
        assert set(collector.get_books_for_children()) == {"1984", "Незнайка", "Маленький принц"}

    # добавляем книгу в избранное: Незнайка
    def test_add_book_in_favorites_when_book_exists_and_not_in_favorites(self):
        collector = BooksCollector()
        collector.books_genre = {
            "1984": "Фантастика",
            "Незнайка": "Мультфильмы",
            "Оно": "Ужасы"
        }
        collector.favorites = []
        collector.add_book_in_favorites("Незнайка")
        assert collector.get_list_of_favorites_books() == ["Незнайка"]

    # удаляем книгу из избранного: Незнайка
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.favorites = ["1984", "Незнайка", "Оно"]
        collector.delete_book_from_favorites("Незнайка")
        assert "Незнайка" not in collector.favorites

    # удаляем книгу из избранного: проверяем оставшийся список
    def test_delete_book_from_favorites_show_list_result(self):
        collector = BooksCollector()
        collector.favorites = ["1984", "Незнайка", "Оно"]
        collector.delete_book_from_favorites("Оно")
        assert collector.get_list_of_favorites_books() == ["1984", "Незнайка"]

    # Получаем список избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.favorites = ["1984", "Маленький принц", "Mы"]
        assert collector.get_list_of_favorites_books() == ["1984", "Маленький принц", "Mы"]
