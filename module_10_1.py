from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.now()
time_res = time_stop - time_start
print(f'Работа потоков {time_res}')

time2_start = datetime.now()
thr_f1 = Thread(target=write_words, args=(10, "example5.txt"))
thr_f2 = Thread(target=write_words, args=(30, "example6.txt"))
thr_f3 = Thread(target=write_words, args=(200, "example7.txt"))
thr_f4 = Thread(target=write_words, args=(100, "example8.txt"))

thr_f1.start()
thr_f2.start()
thr_f3.start()
thr_f4.start()

thr_f1.join()
thr_f2.join()
thr_f3.join()
thr_f4.join()

time2_stop = datetime.now()
time2_res = time2_stop - time2_start
print(f'Работа потоков {time2_res}')
