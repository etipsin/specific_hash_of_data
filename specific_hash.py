import json


class DumpsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SpecificHash:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__words"):
            with open('words_alpha.txt') as word_file:
                valid_words = word_file.read().split()

            cls.__words = valid_words
            cls.__dataset_word_count = len(valid_words)

        return super(SpecificHash, cls).__new__(cls)

    def __init__(self, data, count_words=3, separator="-", count_options=3):
        self.__data = self.__serialize(data)
        self.__count_words = count_words
        self.__separator = separator
        self.__count_options = count_options

    @property
    def __length(self):
        return len(self.__data)

    def set_data(self, data):
        self.__data = self.__serialize(data)

    def set_count_words(self, count_words):
        self.__count_words = count_words

    def set_separator(self, separator):
        self.__separator = separator

    def set_count_options(self, count_options):
        self.__count_options = count_options

    @staticmethod
    def __serialize(data):
        """Сериализация"""
        if isinstance(data, str):
            return data
        if isinstance(data, (list, dict, int, float)):
            return json.dumps(data)
        elif hasattr(data, "dumps"):
            return data.dumps()
        else:
            raise DumpsError("Ошибка сериализации")

    def __get_word_by_index(self, index):
        """Получение слова из набора слов"""
        return self.__words[index]

    def __break_data(self):
        """Разбивка исходных данных по n-граммам (символам)"""
        return [self.__data[i:i + self.__count_words] for i in range(0, self.__length, self.__count_words)]

    def __get_positions(self):
        """Получение позиций слов в наборе"""
        data = self.__break_data()
        result, prev = [], 1
        while len(result) < self.__count_words:
            prev = prev % self.__dataset_word_count
            for indx, letters in enumerate(data, 1):
                if len(letters) > 1:
                    for w in letters:
                        r = ord(w) * indx * prev
                        prev = r
                else:
                    r = ord(letters) * indx
                    prev = r

                result.append(r)

                if len(result) >= self.__count_words:
                    break

        return result

    def __normalize_positions(self, data):
        """Нормализация позиций"""
        return list(map(lambda x: x % self.__dataset_word_count if x > self.__dataset_word_count else x, data))

    def get_hash(self):
        """Формирование хэша"""
        positions = self.__get_positions()
        positions = self.__normalize_positions(list(map(lambda x, y: (x + y)**3, positions, range(len(positions)))))
        result = []
        for _ in range(self.__count_options):
            current_hash = []
            for pos in positions:
                current_hash.append(self.__get_word_by_index(pos).title())

            positions = self.__normalize_positions(list(map(lambda x, y: (x + y)**3, positions, range(len(positions)))))

            result.append(self.__separator.join(current_hash))

        return result
