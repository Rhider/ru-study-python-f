from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        filter_list = list(
            filter(
                lambda film: "," in film["country"] and film["rating_kinopoisk"] not in ("", "0"),
                list_of_movies,
            )
        )
        ratings = list(map(lambda film: float(film["rating_kinopoisk"]), filter_list))
        average_rating = sum(ratings) / len(ratings)

        return average_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        filter_list = list(
            filter(
                lambda film: film["rating_kinopoisk"] not in ("", "0")
                and float(film["rating_kinopoisk"]) >= rating,
                list_of_movies,
            )
        )
        if filter_list:
            ratings = list(map(lambda film: film["name"].count("и"), filter_list))
            count_letters = sum(ratings)
            return count_letters

        return 0
