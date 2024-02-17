# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class City:
    def __init__(self, population: int, square: float):
        """
        Создание и подготовка к работе объекта "Город"
        :param population: Население города
        :param square: Площадь города
        Примеры:
        >>> city = City(500, 354)  # инициализация экземпляра класса
        """
        if not isinstance(population, (int)):
            raise TypeError("Население должно быть типа int")
        if population < 0:
            raise ValueError("Население города не должно быть отрицательным числом")
        self.population = population

        if not isinstance(square, (int, float)):
            raise TypeError("Площадь города должна быть int или float")
        if square <= 0:
            raise ValueError("Площадь города должна быть положительным числом")
        self.square = square

    def population_growth(self, population_gro: int):
        """
        Рост населения города.
        :param population_gro: Прирост населения
        :return: Актуальное население города
        Примеры:
        >>> city = City(500, 435)
        >>> city.population_growth(200)
        """
        if not isinstance(population_gro, (int)):
            raise TypeError("Прирост населения должен быть типа int")
        ...

    def increasing_the_area(self, area: float):
        """
        Увеличение площади города.
        :param area: Добавленная площадь
        :return: Актуальная площадь города
        Примеры:
        >>> city = City(500, 564)
        >>> city.population_growth(200)
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Добавляемая площадь должна быть типа int или float")
        ...

class Cat:
    def __init__(self, name: str, colour: str, age: int):
            """
            Создание и подготовка к работе объекта "Кошка"
            :param name: Имя кошки
            :param colour: Цвет кошки
            :param age: Возраст кошки
            Примеры:
            >>> cat = Cat("Мурка","белый",5)  # инициализация экземпляра класса
            """

            if not isinstance(age, int):
                raise TypeError("Возраст кошки должен быть типа int")
            if age <= 0:
                raise ValueError("Возраст кошки должен быть положительным числом")
            self.age = age

            if not isinstance(colour, str):
                raise TypeError("Цвет кошки должен быть типа str")
            self.colour = colour

            if not isinstance(name, str):
                raise TypeError("Имя кошки должно быть типа str")
            self.name = name

        def say_meow(self) -> str:
            """
            Функция воспроизводит мяуканье кошки
            :return: Имя_кошки(name) сказала мяу
            Примеры:
            >>> cat = Cat("Мурка","белый",5)
            >>> cat.say_meow()
            """
            ...

        def human_age(self) -> int:
            """
            Функция, которая определяет,сколько кошеке лет в пересчёте на человечесий возраст
            :return: Человеческий возраст эквивалентный возрасту кошки
            Примеры:
            >>> cat = Cat("Мурка","белый",5)
            >>> cat.human_age()
            """

            ...

        def colour_match(self, kitten_colour: str) -> bool:
            """
            Функция, определяющая совпадает ли цвет кошки с цветом её котёнка
            :param kitten_colour: Цвет котёнка
            :return: Совпадает ли цвет кошки с цветом её котёнка
            Примеры:
            >>> cat = Cat("Мурка","белый",5)
            >>> cat.colour_match("серый")
            """
            if not isinstance(kitten_colour, str):
                raise TypeError("Цвет котёнка должен быть типа str")
            self.kitten_colour = kitten_colour
            ...

class Book:
    def __init__(self, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param name:  Название книги
        :param pages: Количество страниц в книге
        Примеры:
        >>> book = Book('Book', 100)
        """
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должен быть типа int')
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages

    def rename_book(self, name: str) -> None:
        """
        Функция которая меняет название книги
        :param name: Новое название книги
        Примеры:
        >>> book = Book('Book', 100)
        >>> book.rename_book('Hitchhiker')
        """
        ...

    def publish_book(self) -> int:
        """
        Функция которая публикует книгу
        :return: Идентификатор новой публикации
        Примеры:
        >>> book = Book('Book', 100)
        >>> publication_id = book.publish_book()
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
        pass