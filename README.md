# Задача
 Написать программу, которая будет запускать процесс и с указанным интервалом времени собирать о нём следующую статистику:
 - Загрузка CPU (в процентах);
 - Потребление памяти: Working Set и Private Bytes (для Windows-систем) или Resident Set Size и Virtual Memory Size (для Linux-систем);
 - Количество открытых хендлов (для Windows-систем) или файловых дескрипторов (для Linux-систем).
 
 Сбор статистики должен осуществляться всё время работы запущенного процесса. Путь к файлу, который необходимо запустить, и интервал сбора статистики должны указываться пользователем. Собранную статистику необходимо сохранить на диске. Представление данных должно в дальнейшем позволять использовать эту статистику для автоматизированного построения графиков потребления ресурсов.
_____
# Описание программы
 Программа принимает 3 аргумента:
 - Интервал сбора информации, секунды.
 - Путь к исполняемому файлу тестируемой программы
 - Путь к XML файлу с собранными данными
 
 Сбор статистики прекращается если тестируемый процесс остановлен
 ### Пример параметров
 > 5 notepad.exe log.xml
