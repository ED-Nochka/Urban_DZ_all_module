class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, '')
                words = text.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        find_words = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                find_words[file_name] = words.index(word.lower()) + 1
        return find_words

    def count(self, word):
        count_words = {}
        for words, file_name in self.get_all_words().items():
            words_count = file_name.count(word.lower())
            count_words[words] = words_count
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

print()

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
