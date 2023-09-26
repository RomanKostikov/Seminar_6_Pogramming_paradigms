# ● Контекст
# В каждом телефоне есть это замечательное приложение.
# Секундомер - это программа, которая засекает сколько
# времени прошло от момента запуска до момента остановки.
# Также, как правило там присутствует функция “паузы”,
# которая позволяет временно приостановить секундомер, с
# возможностью продолжить отсчет в будущем.
# ● Ваша задача
# Реализовать секундомер на любом языке программирования
# в любой парадигме. Секундомер должен поддерживать
# следующий функционал:
# ○ Запуск
# ○ Пауза
# ○ Выход из паузы
# ○ Остановка

import time as ttt

print('Нажмите ENTER для начала или CTRL + C(CTRL + F2) чтобы остановить')

while 1:

    try:

        input()

        starttime = ttt.time()

        print('Работаем')

        while 1:
            print('Прошло: ', round(ttt.time() - starttime, 0), 'сек.', end="\r")

            ttt.sleep(1)

    except KeyboardInterrupt:

        print('Остановленно')

        endtime = ttt.time()

        print('Итого:', round(endtime - starttime, 2), 'сек.')

        break

# /** JAVA на python аналогичный алгоритм, только синтаксис другой
# * Реализовать секундомер. Секундомер должен поддерживать следующий функционал:
# * - Запуск
# * - Пауза
# * - Выход из паузы
# * - Остановка
# */

# public class Main {
# public static void main(String[] args) {
# Stopwatch stopwatch = new Stopwatch(); // Создаем объект секундомера
# // Thread thread = new Thread(() -> { // Поток вывода работы секундомера
# // while (true) {
# // try {
# // Thread.sleep(5000); // Искусственная пауза, что бы успеть ввести команду
# // } catch (InterruptedException e) { // Прерывание работы потока через исключение
# // System.out.println("Секундомер остановлен");
# // System.out.println((stopwatch.getTime() / 1_000) + " сек");
# // break;
# // }
# // System.out.println((stopwatch.getTime() / 1_000) + " сек"); // Вывод в консоль
# // }
# // });
# // thread.start(); // Старт потока вывода времени секундомера
# System.out.println("""
# Список команд:
# Запуск - запуск секундомера;
# Пауза - приостановить запущенный секундомер;
# Продолжить - продолжить работу приостановленного секундомера;
# Стоп - остановить секундомер;
# Введите команду: """);
# boolean flag = true;
# while (flag) { // Бесконечный цикл ожидание ввода команды от пользователя
# Scanner scanner = new Scanner(System.in);
# String commandUser = scanner.nextLine().toLowerCase().strip();
# switch (commandUser) {
# case "запуск" -> stopwatch.start();
# case "время" -> System.out.println((stopwatch.getTime() / 1000) + " сек.");
# case "пауза" -> stopwatch.pause();
# case "продолжить" -> stopwatch.removePause();
# case "стоп" -> {
# stopwatch.stop();
# flag = false;
# }
# default -> System.out.println("Неизвестная команда");
# }
# }
# // thread.interrupt(); // При выходе из бесконечного цикла прерываем поток вывода
# }
# }
#
# package task1;
#
# /**
# * Класс секундомера
# */
# public class Stopwatch {
# private long timeStart = 0;
# private long timeStop = 0;
# private long timePauseStart = 0;
# private long timePauseStop = 0;
# private long timePaused = 0;
# private boolean isRunning;
#
# /**
# * Запуск секундомера
# */
# public void start() {
# this.timeStart = System.currentTimeMillis();
# this.isRunning = true;
# }
#
# /**
# * Остановка секундомера
# */
# public void stop() {
# this.timeStop = System.currentTimeMillis();
# this.isRunning = false;
# }
#
# /**
# * Получение времени
# *
# * @return время в миллисекундах
# */
# public long getTime() {
# if (isRunning) {
# return System.currentTimeMillis() - timeStart - timePaused;
# } else {
# return (timeStop - timeStart) - (timePaused);
# }
# }
#
#
# /**
# * Постановка на паузу
# */
# public void pause() {
# if (isRunning) {
# this.timePauseStart = System.currentTimeMillis();
# this.timeStop = System.currentTimeMillis();
# this.isRunning = false;
# }
# }
#
# /**
# * Снятие с паузы
# */
# public void removePause() {
# if (!isRunning) {
# this.timePauseStop = System.currentTimeMillis();
# this.timePaused += timePauseStop - timePauseStart;
# this.isRunning = true;
# }
# }
# }
# Сергей Акопян https://pastebin.co