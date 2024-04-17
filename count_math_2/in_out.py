from data_classes import Response, Single_request, Sys_request
from data_functions import functions, systems
from methods import iterations_method_system, half_division_method, iterations_method


def read(paint):
    try:
        if int(input("Введите 1 для ввода с консоли или 2 для ввода из файла:")) == 1:
            if int(input("Введите 1 для решения уравнения или 2 для решения системы уравнений:")) == 1:
                print("Доступные уравнения:")
                for key, value in functions.items():
                    print("№" + str(key) + ":\n" + value.present)
                fun = functions[int(input("Введите номер уравнения:"))]
                term_left = float(input("Введите левый край отрезка для рассмотрения:"))
                term_right = float(input("Введите правый край отрезка для рассмотрения:"))
                paint(Single_request(fun, {}, term_left, term_right, {}))
                fun.approx_left = float(input("Введите левый край приближения:"))
                fun.approx_right = float(input("Введите правый край приближения:"))
                accuracy = float(input("Введите точность:"))
                if int(input("Выберите метод: 1 - половинного деления, 2 - простой итерации")) == 1:
                    method = half_division_method
                else:
                    method = iterations_method
                return Single_request(fun, method, term_left, term_right, accuracy)
            else:
                print("Доступные системы:")
                for key, value in systems.items():
                    print("№" + str(key) + ":\n" + value["first"].present + "\n" + value["second"].present)
                system = systems[int(input("Введите номер системы:"))]
                paint(Sys_request(system, {}, 0, 0, {}))
                system["first"].approx_left = float(input("Введите левый край приближения x:"))
                system["first"].approx_right = float(input("Введите правый край приближения x:"))
                system["second"].approx_left = float(input("Введите левый край приближения y:"))
                system["second"].approx_right = float(input("Введите правый край приближения y:"))
                accuracy = float(input("Введите точность:"))
                return Sys_request(system, iterations_method_system, 0, 0, accuracy)
        else:
            with open('file') as f:
                lines = f.readlines()
                if int(lines[0]) == 1:
                    fun = functions[int(lines[1])]
                    term_left = float(lines[2])
                    term_right = float(lines[3])
                    paint(Single_request(fun, {}, term_left, term_right, {}))
                    fun.approx_left = float(lines[4])
                    fun.approx_right = float(lines[5])
                    accuracy = float(lines[6])
                    if int(lines[7]) == 1:
                        method = half_division_method
                    else:
                        method = iterations_method
                    return Single_request(fun, method, term_left, term_right, accuracy)
                else:
                    system = systems[int(lines[1])]
                    paint(Sys_request(system, {}, 0, 0, {}))
                    system["first"].approx_left = float(lines[2])
                    system["first"].approx_right = float(lines[3])
                    system["second"].approx_left = float(lines[4])
                    system["second"].approx_right = float(lines[5])
                    accuracy = float(lines[6])
                    return Sys_request(system, iterations_method_system, 0, 0, accuracy)
    except ValueError:
        print("\033[31mНеправильный формат ввода")
        exit(1)


def write(response: Response):
    print("Корень = " + str(response.root))
    print("Значение функции в корне = " + str(response.fun_in_root))
    print("Количество итерраций  = " + str(response.i_count))


def write_sys(response: Response):
    print("Корни = " + str(response.root))
    # print("Значение функций в точке = " + str(response.fun_in_root))
    print("Количество итерраций  = " + str(response.i_count))
    print("Вектор погрешностей:")
    for key, value in response.error_vector.items():
        print(str(key) + ": " + str(value))


def write_err(response: Response):
    print("ОШИБКА!: " + response.message)
