<h1>Отчет</h1>

Имеем 2 версии фильтра для фотографий - оптимизированный filter.py и первоначальный old_filter.py
Сравнивать их будем на примере этого изображения

![Screenshot](img2.jpg)

_____

Вот время выполнения работы filter

![Screenshot](screenshots/filter_results.png)

и вот время выполнения работы old_filter

![Screenshot](screenshots/old_filter_results.png)

Казалось бы, где оптимизация? Но версия filter.py предполагает ввод 4х переменных. Поэтому, чтобы замерить время работы кода без этих погрешностей добавим еще один файл - filter_with_filename.py, в котором заранее будут указаны имя input-файла "img2", имя output-файла "res.jpg", размер блока 10, 50 градаций серого. Тогда без временных затрат на ввод данных будут следующие результаты:

![Screenshot](screenshots/filter_with_filename_results.png)

Все всё понимают - матричные преобразования numpy на 2 порядка эффективнее ручных вычислений двумя циклами

Этот фильтр из такой фотографии

![Screenshot](img2.jpg)

Делает такую

![Screenshot](res.jpg)
_____

Теперь займемся выделенными функциями count_average_brightness и applying_the_filter. Допишем документацию и doc-тесты

![Screenshot](screenshots/doctest_for_count_average_brightness.png)
![Screenshot](screenshots/doctest_for_applying_the_filter.png)

______

Результат работы с отладчиком:

![Screenshot](screenshots/work_with_PDB.png)
