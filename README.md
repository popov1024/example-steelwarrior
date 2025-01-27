# Задача D. Стальной охотник

В августе к 10-летию игры `World of Tanks` в ней появился обновленный режим `Стальной охотник`. В этом режиме каждый играет сам за себя и побеждает тот, кто останется последним выжившим на поле боя. Сражение происходит на городской карте, на которой в том числе есть несколько удобных позиций для танков для ведения огня (для простоты будем считать, что все эти позиции расположены в одну линию слева направо). Каждая из этих позиций защищена справа – это означает, что в танк можно попасть только если по нему стреляют из позиции левее данного танка. Алиса решила взять 10 таких позиций и поставить туда по одному танку каждого уровня (в игре всего 10 уровней танков – с первого по десятый). Будем считать, что любой танк не может пробить броню любого другого танка уровнем выше. После расстановки танков Алиса заметила, что некоторые танки могут пробить другие танки. Она решила случайным образом равновероятно взять два танка и, если один из них может получить урон от другого, поменять эти два танка местами. Очевидно, что после такой перестановки эти танки уже не смогут пробить друг друга. Алиса продолжила выполнять эту операцию (случайно выбирать два танка и, если необходимо, менять их местами) N раз до тех пор, пока не наступит мир – ни один из танков не может повредить другой. Так как пары танков выбираются случайным образом, то N – это случайная величина. Найдите ее математическое ожидание.
Входные данные
В первой строке находится одно целое число t (1 <= t <= 40) – количество тестовых примеров. Далее в каждой из 𝑡 строк записаны через пробел ровно 10 целых чисел ai (1 <= ai <= 10, все ai различны) – уровни танков, расположенных в позициях в указанном порядке.
Выходные данные
В каждой из 𝑡 строк выведите математическое ожидание случайной величины 𝑁 для каждого тестового примера из входных данных. Это значение должно быть округлено до 6 знаков после запятой, при этом все 6 знаков дробной части должны быть напечатаны, а целая и дробная части разделены точкой.
Пример
Входные данные

```text
2
1 2 3 4 5 6 7 8 10 9
1 2 3 4 5 6 7 8 9 10
```

Выходные данные

```text
45.000000
0.000000
```

## Примечание

Внимание! В этой задаче возможность прохождения всех тестов решениями на языке Python не гарантируется.
В первом примере только танк 10 уровня может пробить танк 9 уровня. Поэтому, чтобы поменять их местами, в среднем Алисе нужно выбрать 45 случайных пар танков (так как 𝐶2_10 = 45). Во втором примере ни один танк
не может повредить другой – у каждого танка справа только танки большего уровня.
Как отправить решение?
Ваше решения должно представлять собой консольную программу на одном из доступных языков программирования (`C++11` или `Python 3.6`). Программа должна считывать из консоли входные данные (гарантируется, что при проверке решения они будут в точности в том формате и в тех диапазонах, как это описано в секции «Входные данные») и выводить ответ в консоль в описанном в условии формате. Лишние пробелы в конце строк будут игнорироваться. Для отправки решения вам нужно выбрать в системе задачу, язык программирования, и отправить исходный файл с кодом. Он будет проверен системой на серии тестов. Тест считается пройденным, если программа вывела правильный ответ и уложилась в ограничения по времени работы и используемой памяти. За каждый пройденный тест начисляется один балл. Результаты первых 10 тестов вы сможете увидеть в системе. Первый тест всегда из условия задачи. Общий результат по задаче определяется по решению, набравшему максимальное количество баллов. Количество попыток не ограничено.
