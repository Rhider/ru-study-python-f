class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if input_list:
            max_elem = input_list[0]

            for el in input_list:
                if el > max_elem:
                    max_elem = el

        return [max_elem if el > 0 else el for el in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def binarySearch(input_list: list[int], left: int, right: int, query: int) -> int:
            if left > right:
                return -1

            mid = left + (right - left) // 2

            if input_list[mid] == query:
                return mid
            if input_list[mid] > query:
                return binarySearch(input_list, left, right - 1, query)
            else:
                return binarySearch(input_list, mid + 1, right, query)

        if input_list:
            return binarySearch(input_list, 0, len(input_list) - 1, query)
        return -1
