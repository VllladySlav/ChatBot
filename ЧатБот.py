import datetime
import re
from colorama import Fore, Back, Style, init
topic_history = []
topics_dictionary_1 = {
    "фізика": ["1 - Закон всесвітнього тяжіння Ньютона",
               "2 - Закон збереження енергії",
               "3 - Вивести сталу Планка"],
    "математика": ["1 - Розв'язати квадратне рівняння",
                   "2 - Обчислити довжину дуги кола",
                   "3 - Обчислити довжину відрізка між двома точками",
                   "4 - Вивести sin(x) та cos(x)",
                   "5 - Вивести число π"],
    "географія": ["1 - Яке найбільше озеро у світі за площею?",
                  "2 - Які дві держави мають найбільшу кількість кордонів з іншими державами?",
                  "3 - Яке місто має найбільшу кількість населення у світі?",
                  "4 - Знайти відстань між двома точками"],
    "філологія": ["1 - Яка різниця між present simple та present continuous?",
                  "2 - Як утворити passive voice в present simple?",
                  "3 - Як поставити іменник у давальному відмінку?",
                  "4 - Правильний наголос"],
    "астрономія": ["1 - Що таке космічне випромінювання?",
                   "2 - Що таке астероїди та комети?",
                   "3 - Які процеси відбуваються на сонці та як вони впливають на землю?"],
    "загальні": ["1 - Який зараз місяць?",
                 "2 - Котра година?",
                 "3 - Як тебе звати?",
                 "4 - Пограти у вгадай число між 1 та 10",
                 "5 - Пограти у камінь-ножиці-папір",
                 "6 - Сказати надихаючу цитату"]
}

topics_dictionary = {
    "фізика": ["1 - закон всесвітнього тяжіння ньютона", "1", "закон всесвітнього тяжіння ньютона",
               "2 - закон збереження енергії", "2", "закон збереження енергії",
               "3 - вивести сталу планка", "3", "вивести сталу планка"],
    "математика": ["1 - розв'язати квадратне рівняння", "1", "розв'язати квадратне рівняння",
                   "2 - обчислити довжину дуги кола", "2", "обчислити довжину дуги кола",
                   "3 - обчислити довжину відрізка між двома точками", "3",
                   "обчислити довжину відрізка між двома точками",
                   "4 - вивести sin(x) та cos(x)", "4", "вивести sin(x) та cos(x)",
                   "5 - вивести число π", "5", "вивести число π"],
    "географія": ["1 - яке найбільше озеро у світі за площею?", "1", "яке найбільше озеро у світі за площею?",
                  "2 - які дві держави мають найбільшу кількість кордонів з іншими державами?", "2",
                  "які дві держави мають найбільшу кількість кордонів з іншими державами?",
                  "3 - яке місто має найбільшу кількість населення у світі?", "3",
                  "яке місто має найбільшу кількість населення у світі?",
                  "4 - знайти відстань між двома точками", "4", "знайти відстань між двома точками"],
    "філологія": [
        "1 - яка різниця між present simple та present continuous?", "1",
        "яка різниця між present simple та present continuous?",
        "2 - як утворити passive voice в present simple?", "2", "як утворити passive voice в present simple?",
        "3 - як поставити іменник у давальному відмінку?", "3", "як поставити іменник у давальному відмінку?",
        "4 - правильний наголос", "4", "правильний наголос"],
    "астрономія": ["1 - що таке космічне випромінювання?", "1", "що таке космічне випромінювання?",
                   "2 - що таке астероїди та комети?", "2", "що таке астероїди та комети?",
                   "3 - які процеси відбуваються на сонці та як вони впливають на землю?", "3",
                   "які процеси відбуваються на сонці та як вони впливають на землю?"],
    "загальні": ["1 - який зараз місяць?", "1", "який зараз місяць?",
                 "2 - котра година?", "2", "котра година?",
                 "3 - як тебе звати?", "3", "як тебе звати?",
                 "4 - пограти у вгадай число між 1 та 10", "4", "пограти у вгадай число між 1 та 10",
                 "5 - пограти у камінь-ножиці-папір", "5", "пограти у камінь-ножиці-папір",
                 "6 - сказати надихаючу цитату", "6", "сказати надихаючу цитату"]
}


class Physics:
    def calculate_energy(self):

        init()

        answer = "так"
        while answer == "так":
            print_response("Введіть значення двох параметрів і константи.\n(відсутнє значення позначте нулем).")

            print_response(Fore.RED + "Кінетична енергія (Дж): " + Fore.RESET)

            while True:
                try:
                    e_kin = float(get_user_input())
                    break
                except ValueError:
                    print_response("Значення енергії має бути дійсним числом! Повторіть спробу ще.")

            print_response(Fore.GREEN + "Потенціальна енергія (Дж): " + Fore.RESET)

            while True:
                try:
                    e_pot = float(get_user_input())
                    break
                except ValueError:
                    print_response("Значення енергії має бути дійсним числом! Повторіть спробу ще.")

            print_response(Fore.BLUE + "Внутрішня енергія (Дж): " + Fore.RESET)

            while True:
                try:
                    e_int = float(get_user_input())
                    break
                except ValueError:
                    print_response("Значення енергії має бути дійсним числом! Повторіть спробу ще.")

            print_response(Fore.MAGENTA + "Константа (Дж): " + Fore.RESET)

            while True:
                try:
                    const = float(get_user_input())
                    break
                except ValueError:
                    print_response("Значення константи має бути дійсним числом! Повторіть спробу ще.")

            if e_kin == 0:
                e_kin = Style.BRIGHT + Fore.BLACK + str(const - e_pot - e_int) + " Дж." + Style.RESET_ALL + Fore.RESET
                result = Back.YELLOW + Fore.BLACK + f"Кінетична енергія дорівнює: {e_kin}" + Back.RESET + Fore.RESET
                print_response(result)
            elif e_pot == 0:
                e_pot = Style.BRIGHT + Fore.BLACK + str(const - e_kin - e_int) + " Дж." + Style.RESET_ALL + Fore.RESET
                result = Back.YELLOW + Fore.BLACK + f"Кінетична енергія дорівнює: {e_pot}" + Back.RESET + Fore.RESET
                print_response(result)
            elif e_int == 0:
                e_int = Style.BRIGHT + Fore.BLACK + str(const - e_kin - e_pot) + " Дж." + Style.RESET_ALL + Fore.RESET
                result = Back.YELLOW + Fore.BLACK + f"Кінетична енергія дорівнює: {e_int}" + Back.RESET + Fore.RESET
                print_response(result)
            else:
                print_response("Недостатньо даних для обчислення.")

            print_response("Чи бажаєте повторити спробу ще раз?")
            answer = get_user_input().lower().strip()

    def calculate_gravity(self):
        answer = "так"
        while answer == "так":
            g = 6.67430e-11  # гравітаційна стала

            print_response(Fore.RED + "Введіть масу першого тіла (в кілограмах): " + Fore.RESET)
            while True:
                try:
                    m_1 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Маса тіла повинна бути дійсним числом (наприклад, 5.56).")

            print_response(Fore.GREEN + "Введіть масу другого тіла (в кілограмах): " + Fore.RESET)
            while True:
                try:
                    m_2 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Маса тіла повинна бути дійсним числом (наприклад, 12.34).")

            print_response(Fore.BLUE + "Введіть відстань між центрами тіл (в метрах): " + Fore.RESET)
            while True:
                try:
                    r = float(get_user_input())
                    break
                except ValueError:
                    print_response("Відстань має бути дійсним числом (наприклад, 9.777).")

            gravity = g * ((m_1 * m_2) / (r ** 2))

            print_response(Back.YELLOW + Fore.BLACK + "Сила притягання між тілами дорівнює: " + Style.BRIGHT
                           + str(gravity) + " H." + Back.RESET + Fore.RESET + Style.RESET_ALL)

            print_response("Чи бажаєте повторити спробу?")
            answer = get_user_input().lower().strip()

    def derive_planck_constant(self):
        # Значення сталої Планка в метро-кілограм-секундних одиницях
        h = Style.BRIGHT + str(6.62607015e-34) + " м²·кг/с."

        print_response(Fore.BLACK + Back.YELLOW + "Значення сталої Планка: " + h
                       + Back.RESET + Fore.RESET + Style.RESET_ALL)


class Mathematics:
    def solve_quadratic_equation(self):
        answer = "так"
        while answer == "так":
            from math import sqrt

            print_response(Fore.RED + "Введіть коефіцієнт a: " + Fore.RESET)
            while True:
                try:
                    a = float(get_user_input())
                    break
                except ValueError:
                    print_response("Коефіцієнтом може бути лише дійсне число. Введіть коефіцієнт а ще раз.")

            print_response(Fore.GREEN + "Введіть коефіцієнт b: " + Fore.RESET)
            while True:
                try:
                    b = float(get_user_input())
                    break
                except ValueError:
                    print_response("Коефіцієнтом може бути лише дійсне число. Введіть коефіцієнт b ще раз.")

            print_response(Fore.BLUE + "Введіть коефіцієнт c: " + Fore.RESET)
            while True:
                try:
                    c = float(get_user_input())
                    break
                except ValueError:
                    print_response("Коефіцієнтом може бути лише дійсне число. Введіть коефіцієнт c ще раз.")

            d = b ** 2 - 4 * a * c
            if d < 0:
                print_response("Рівняння не має коренів.")
            else:
                x_1 = Fore.BLACK + Style.BRIGHT + str(round((-b + sqrt(d)) / (2 * a), 4))
                x_2 = Fore.BLACK + Style.BRIGHT + str(round((-b - sqrt(d)) / (2 * a), 4))
                print_response(Fore.GREEN + "Корені квадратного рівняння:" + Fore.RESET)
                print("             " + Fore.BLACK + Back.YELLOW + "x_1 = " + x_1
                      + Fore.RESET + Back.RESET + Style.RESET_ALL, end="")
                print(Fore.BLACK + Back.YELLOW + "," + Fore.RESET + Back.RESET)
                print("             " + Fore.BLACK + Back.YELLOW + "x_2 = " + x_2
                      + Fore.RESET + Back.RESET + Style.RESET_ALL, end="")
                print(Fore.BLACK + Back.YELLOW + "." + Fore.RESET + Back.RESET)

            print_response("Чи бажаєте повторити спробу ще раз?")
            answer = get_user_input().lower().strip()

    def calculate_length_circle(self):
        answer = "так"
        while answer == "так":
            print_response(Fore.RED + "Введіть радіус кола (см): " + Fore.RESET)
            while True:
                try:
                    r = float(get_user_input())
                    break
                except ValueError:
                    print_response("Радіус кола - це дійсне число (наприклад, 2.222).")

            print_response(Fore.GREEN + "Введіть кут у радіанах (число без pi): " + Fore.BLUE)
            while True:
                try:
                    theta = float(get_user_input())
                    break
                except ValueError:
                    print_response("Кут - це дійсне число (наприклад, 5.123).")

            length = Style.BRIGHT + str(r * theta)

            print_response(Back.YELLOW + Fore.BLACK + "Довжина дуги кола дорівнює: " + length + " см." +
                  Back.RESET + Fore.BLACK + Style.RESET_ALL)

            print_response("Чи бажаєте повторити спробу ще раз?")
            answer = get_user_input().lower().strip()

    def calculate_length_between_two_points(self):
        answer = "так"
        while answer == "так":
            from math import sqrt

            print_response(Fore.RED + "Введіть координату x першої точки: " + Fore.RESET)
            while True:
                try:
                    x_1 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть дійсне чило!")
            print_response(Fore.GREEN + "Введіть координату x другої точки: " + Fore.RESET)
            while True:
                try:
                    x_2 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть дійсне чило!")

            print_response(Fore.BLUE + "Введіть координату y першої точки: " + Fore.RESET)
            while True:
                try:
                    y_1 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть дійсне чило!")

            print_response(Fore.MAGENTA + "Введіть координату y другої точки: " + Fore.RESET)
            while True:
                try:
                    y_2 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть дійсне чило!")

            print_response("Скільки знаків після коми бажаєте залишити (до 16)?")
            while True:
                try:
                    figures_after_comma = int(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть ціле чило!")

            leng = (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2
            length = Style.BRIGHT + str(round(sqrt(leng), figures_after_comma))

            print_response(Fore.BLACK + Back.YELLOW + "Довжина відрізка між двома точками на площині становить: " +
                  length + "." + Fore.RESET + Back.RESET + Style.RESET_ALL)

            print_response("Чи бажаєте повторити спробу ще раз?")
            answer = get_user_input().lower().strip()

    def calculate_sin_cos(self):
        answer = "так"
        while answer == "так":
            import math

            print_response(Fore.MAGENTA + "Введіть значення кута в радіанах (без pi): " + Fore.RESET)
            while True:
                try:
                    radians = float(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть дійсне число!")

            print_response("Скільки знаків після коми бажаєте залишити (до 16)?")
            while True:
                try:
                    figures_after_comma = int(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть ціле число!")

            sin = Style.BRIGHT + str(round(math.sin(radians), figures_after_comma))
            cos = Style.BRIGHT + str(round(math.cos(radians), figures_after_comma))
            print_response(Fore.BLACK + Back.BLUE + "sin(" + str(radians) + ")" + " = " + sin + Fore.RESET + Back.RESET
                  + Style.RESET_ALL)
            print_response(Fore.BLACK + Back.YELLOW + "cos(" + str(radians) + ")" + " = " + cos
                           + Fore.RESET + Back.RESET + Style.RESET_ALL)

            print_response("Чи бажаєте повторити спробу ще раз?")
            answer = get_user_input().lower().strip()

    def print_value_pi(self):
        from math import pi

        print_response(Fore.BLACK + Back.YELLOW + "Число π становить: " + (Style.BRIGHT + str(pi)) + '.'
              + Fore.RESET + Back.RESET + Style.RESET_ALL)


class Geography:
    def the_largest_lake(self):
        print_response("""Найбільше озеро у світі - це """ + Fore.CYAN + "Каспійське море" + Fore.RESET
                       + """. Незважаючи на те, що воно 
називається морем, науковці класифікують його як озеро. Каспійське море розташоване
між Азією та Європою та має площу близько 143 000 км².""")

    def the_largest_number_of_borders(self):
        print_response("""Дві держави з найбільшою кількістю кордонів з іншими державами - це московія та китай.
московія має кордон з 16 державами, а саме: Азербайджан, Білорусь, Естонія, Фінляндія, Грузія, Казахстан, 
Латвія, Литва, Монголія, Норвегія, Польща, Північна Корея, Абхазія, Південна Осетія, Україна та 
Естонська Республіка. Китай має кордон з 14 державами, а саме: Афганістан, Бутан, М'янма, Камбоджа, 
Індія, Казахстан, Киргизстан, Лаос, Макао, Монголія, Непал, Корея Північна, Пакистан та Таджикистан.""")

    def the_largest_population(self):
        print_response("Найбільшу кількість населення у світі має місто " + Fore.CYAN + "Шанхай (КНР)" + Fore.RESET
                       + ": приблизно 24,150,000 людей.")

    def calculate_distance_between_two_points(self):
        answer = "так"
        while answer == "так":
            from math import sqrt

            print_response(Fore.RED + "Введіть координату x_1: " + Fore.RESET)
            while True:
                try:
                    x_1 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Координата - це дійсне число!")

            print_response(Fore.GREEN + "Введіть координату y_1: " + Fore.RESET)
            while True:
                try:
                    y_1 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Координата - це дійсне число!")

            print_response(Fore.MAGENTA + "Введіть координату x_2: " + Fore.RESET)
            while True:
                try:
                    x_2 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Координата - це дійсне число!")

            print_response(Fore.MAGENTA + "Введіть координату y_2: " + Fore.RESET)
            while True:
                try:
                    y_2 = float(get_user_input())
                    break
                except ValueError:
                    print_response("Координата - це дійсне число!")

            print_response("Скільки знаків після коми бажаєте залишити (до 16)?")
            while True:
                try:
                    figures_after_comma = int(get_user_input())
                    break
                except ValueError:
                    print_response("Введіть ціле число!")

            distance = Style.BRIGHT + str(round(sqrt(x_2 - x_1) ** 2 + (y_2 - y_1) ** 2, figures_after_comma))

            print_response(Fore.BLACK + Back.YELLOW + "Відстань між точками А і В: " + distance + "."
                  + Fore.RESET + Back.RESET + Style.RESET_ALL)

            print_response("Чи бажаєте повторити спробу ще раз?")
            answer = get_user_input().lower().strip()


class Philology:
    def the_difference_between_tenses(self):
        print_response("""Present Simple використовують для опису рутинних дій, загальних правд, розкладів, 
указівок тощо. Форму дієслова в Present Simple не змінюємо залежно від особи чи числа, крім третьої 
особи однини, де до дієсслова додаємо -s або -es. Наприклад: I always drink tea in the morning. 
(Я завжди п'ю чай вранці.)

Present Continuous використовується для опису дій, які відбуваються прямо зараз, у момент розмови, 
або в недалекому майбутньому. Форма Present Continuous складається з допоміжного дієслова "to be" у 
Present Simple й основи дієслова із закінченням -ing. Наприклад: I am drinking tea right now. 
(Я зараз п'ю чай.)""")

    def how_formate_passive(self):
        print_response("""Аби утворити Passive Voice в Present Simple використовуємо дієслово to be в Present Simple 
(am/is/are) + Participle II (Past Participle).

Наприклад:
Active Voice: My sister cleans the room.
Passive Voice: The room is cleaned by my sister.""")

    def how_formate_nouns_in_dative(self):
        print_response("""Якщо іменник належить до чоловічого роду, то можливі його закінчення в Д. в. такі:
-ові/-еві(-єві) (-у/-ю), -ам/-ям. Якщо іменник належить до твердої групи, то в Д. в. одн. матиме 
паралельні закінчення -ові/-у, а в множині -ам. Іменники мішаної групи у Д. в. одн. мають закінчення -еві, 
у множині -ам. Іменники м'якої групи матимуть закінчення -еві /-ю в однині, у множині - -ям.
Іменники м'якої групи, основа яких закінчується на -й, в однині матимуть закінчення -єві.

Якщо ж іменник належить до жіночого роду, то можливі його закінчення в Д. в. такі:
-і/-ії, -ам/-ям. Якщо іменник належить до твердої групи, то в Д. в. одн. матиме 
закінчення -і, а в множині -ам. Іменники м'якої групи матимуть закінчення -і в однині, у множині - -ям.
Іменники м'якої групи, основа яких закінчується на -й, в однині матимуть закінчення -ії.

Якщо ж іменник належить до середнього роду, то його можливі закінчення такі: 
-у/-ю, -ам/-ям. Якщо іменник належить до твердої групи, то в Д. в. одн. матиме 
закінчення -у, а в множині -ам. Іменники м'якої групи матимуть закінчення -ю в однині, у множині - -ям.""")

    def say_right_stress(self):
        words_with_stress = \
            ["агронОмія", "алфАвІт", "Аркушик", "асиметрІя", "багаторазОвий", "безпринцИпний", "бЕшкет", "блАговіст",
             "близькИй", "болотИстий", "борОдавка", "босОніж", "боЯзнь", "бурштинОвий", "бюлетЕнь", "вАги",
             "вантажІвка", "веснЯнИй", "видАння", "визвОльний", "вимОга", "вИпадок", "вирАзний", "вИсіти", "вИтрата",
             "вишИваний", "відвезтИ", "відвестИ", "вІдгомін", "віднестИ", "вІрші", "віршовИй", "вітчИм", "гальмО",
             "гАльма", "глядАч", "горошИна", "граблІ", "гуртОжиток", "данИна", "дАно", "децимЕтр", "дЕщиця",
             "де-Юре", "джерелО", "дИвлячись", "дичАвіти", "діалОг", "добовИй", "добУток", "довезтИ", "довестИ",
             "довІдник", "дОгмат", "донестИ", "дОнька", "дочкА", "дрОва", "експЕрт", "єретИк", "жалюзІ", "завдАння",
             "завезтИ", "завестИ", "зАвжди", "завчасУ", "зАгадка", "заіржАвілий", "заіржАвіти", "закінчИти",
             "зАкладка", "зАкрутка", "залишИти", "замІжня", "занестИ", "зАпонка", "заробІток", "зАставка",
             "зАстібка", "застОпорити", "звИсока", "здАлека", "зібрАння", "зобразИти", "зОзла", "зрАння", "зрУчний",
             "зубОжіння", "індУстрія", "кАмбала", "каталОг", "квартАл", "кИшка", "кіломЕтр", "кінчИти", "кОлесо",
             "кОлія", "корИсний", "кОсий", "котрИй", "крицЕвий", "крОїти", "кропивА",
             "кулінАрія", "кУрятина", "лАте", "листопАд", "літОпис", "лЮстро", "мАбУть", "магістЕрський",
             "мАркетинг", "мерЕжа", "металУргія", "мілімЕтр", "навчАння", "нанестИ", "напІй", "нАскрізний",
             "нАчинка", "ненАвидіти", "ненАвисний", "ненАвисть", "нестИ", "нІздря", "новИй", "обіцЯнка", "обрАння",
             "обрУч", "одинАдцять", "одноразОвий", "ознАка", "Олень", "оптОвий", "осетЕр", "отАман", "Оцет",
             "павИч", "партЕр", "пЕкарський", "перевезтИ", "перевестИ", "перЕкис", "перелЯк", "перенестИ",
             "перЕпад", "перЕпис", "піалА", "пІдлітковий", "пізнАння", "пітнИй", "піцЕрія", "пОдруга", "пОзначка",
             "пОмИлка", "помІщик", "помОвчати", "понЯття", "порядкОвий", "посерЕдині", "привезтИ", "привестИ",
             "прИморозок", "принестИ", "прИчіп", "прОділ", "промІжок", "псевдонІм", "рАзом", "рЕмінь", "рЕшето",
             "рИнковий", "рівнИна", "роздрібнИй", "рОзпірка", "рукОпис", "руслО", "сантимЕтр", "свЕрдло",
             "серЕдина", "сЕча", "симетрІя", "сільськогосподАрський", "сімдесЯт", "слИна", "соломИнка", "стАтуя",
             "стовідсОтковий", "стрибАти", "текстовИй", "течіЯ", "тИгровий", "тисОвий", "тім’янИй", "травестІя",
             "тризУб", "тУлуб", "украЇнський", "уподОбання", "урочИстий", "усерЕдині", "фартУх", "фаховИй",
             "фенОмен", "фОльга", "фОрзац", "цАрина", "цемЕнт", "цЕнтнер", "ціннИк", "чарівнИй", "черговИй",
             "читАння", "чорнОзем", "чорнОслив", "чотирнАдцять", "шляхопровІд", "шовкОвий", "шофЕр", "щЕлепа",
             "щИпці", "щодобовИй", "ярмаркОвий"]

        words_without_stress = [word.lower() for word in words_with_stress]

        answer = "так"
        while answer == "так":
            print_response(Fore.MAGENTA + """Введіть слово зі списку наголосів, яке передбачене програмою ЗНО (2018 р.), 
зауважте, що програма не містить слів із двома наголосами (наприклад, хАос, хаОс): """ + Fore.RESET)
            user_word = get_user_input().lower().strip()

            if user_word in words_without_stress:
                index = words_without_stress.index(user_word)
                print_response(Style.BRIGHT + Back.RED + Fore.BLACK + words_with_stress[index]
                      + Style.RESET_ALL + Back.RESET + Fore.RESET)
            else:
                print_response("Такого слова не знайдено.")

            print_response("Чи бажаєте продовжити? ")
            answer = get_user_input().lower().strip()


class Astronomy:
    def cosmic_radiation(self):
        print_response(Style.BRIGHT + Fore.RED + "Космічне випромінювання" + Style.RESET_ALL + Fore.RESET +
              """ - це потік заряджених частинок та електромагнітної радіації, які походять з космічного 
простору. Воно складається з різноманітних частинок, таких як протони, електрони, альфа-частинки, 
гамма-промені, космічні промені космічних сонячних вітрів та инших джерел.

Це випромінювання може мати великий вплив на життя на Землі та космічних місіях. Космічні астронавти, 
які перебувають на Міжнародній космічній станції, піддаються дії цього випромінювання, що може призвести 
до ризику для їхнього здоров'я. Крім того, космічне випромінювання може впливати на електроніку космічних 
апаратів, що може призвести до їхньої помилкової роботи або збоїв.""")

    def asteroids_and_comets(self):
        print_response(Style.BRIGHT + Fore.LIGHTRED_EX + "Астероїди" + Style.RESET_ALL + Fore.RESET +
              """ – небесні тіла, які рухаються навколо Сонця еліптичними орбітами і відрізняються 
від 9-ти великих планет малими розмірами (діаметр до 1000 км). Інша назва – малі планети.
Відомо близько 8 тис. астероїдів із точно визначеними орбітами, більшість із яких розташовані 
між орбітами Марса і Юпітера, із серед. відстанню до Сонця 2.75 астрономічних одиниць.""" +

Style.BRIGHT + Fore.LIGHTRED_EX + "\nКомети" + Style.RESET_ALL + Fore.RESET +
              """ — це тіла Сонячної системи, що рухаються по витягнутих орбітах. При наближенні до Сонця 
комети утворять хвіст із газу та пилу, що иноді досягає мільйонів кілометрів. 
Назва "Комета" походить від давньогрецького слова "kometes" – довговолосий.""")

    def processes_in_the_sun(self):
        print_response(Style.BRIGHT + Fore.LIGHTRED_EX + "Сонце" + Style.RESET_ALL + Fore.RESET +
              """ - це джерело енергії та світла для нашої планети, але воно також може мати 
негативний вплив на Землю через різноманітні процеси, що відбуваються на його 
поверхні. Розгляньмо деякі з них:""" +

Style.BRIGHT + Fore.RED + "\nСонячні вітри" + Style.RESET_ALL + Fore.RESET +
              """: Сонце випускає потік заряджених частинок, які називаються сонячним вітром. 
Цей потік може впливати на магнітне поле Землі та спричиняти збурення в його роботі. 
Це може призводити до змін у роботі супутників, а також впливати на роботу електропередач й инших 
систем, що залежать від магнітного поля.""" +

Style.BRIGHT + Fore.RED + "\nСонячні спалахи" + Style.RESET_ALL + Fore.RESET +
              """: Сонячні спалахи - це яскраві вибухи на поверхні Сонця, які супроводжуються викидом 
енергії, маси та заряджених частинок. Ці спалахи можуть впливати на Землю, спричинюючи магнітні бурі 
й инші різноманітні явища.""" +

Style.BRIGHT + Fore.RED + "\nСонячні промені" + Style.RESET_ALL + Fore.RESET +
              """: Сонце випромінює різні типи електромагнітної радіації, зокрема видиме світло, 
ультрафіолетове випромінювання та рентгенівські промені. Це випромінювання може бути шкідливим для 
здоров'я людей та тварин, а також може впливати на клімат Землі.""" +

Style.BRIGHT + Fore.RED + "\nЗміни сонячної активності" + Style.RESET_ALL + Fore.RESET +
              """: Сонце має циклічну активність, яка відображається у кількості та 
інтенсивності спалахів та сонячних вітрів. Ці зміни можуть впливати на клімат нашої планети та 
призводити до змін у різних екосистемах.""")


class General:
    def what_month_is_it(self):
        import datetime

        now = datetime.datetime.now()

        month = now.month

        months_dict = {1: 'січень', 2: 'лютий', 3: 'березень', 4: 'квітень', 5: 'травень', 6: 'червень', 7: 'липень',
                       8: 'серпень', 9: 'вересень', 10: 'жовтень', 11: 'листопад', 12: 'грудень'}

        print_response(Fore.BLACK + Back.YELLOW + "Зараз " + Style.BRIGHT + months_dict[month]
              + "." + Fore.RESET + Back.RESET + Style.RESET_ALL)

    def play_rock_paper_scissors(self):
        answer = "так"
        while answer == "так":
            import random

            print_response("Пограємо у камінь-ножиці-папір. Введіть свій вибір:")
            options = ["камінь", "ножиці", "папір"]

            user_choice = get_user_input().lower().strip()
            while user_choice not in options:
                print_response("Повторіть спробу ще раз.")
                user_choice = get_user_input().lower().strip()

            computer_choice = random.choice(options)

            if computer_choice == "камінь":
                print_response("Комп'ютер вибрав: камінь")
            elif computer_choice == "ножиці":
                print_response("Комп'ютер вибрав: ножиці")
            else:
                print_response("Комп'ютер вибрав: папір")

            if user_choice == computer_choice:
                print_response("Нічия!")
            elif user_choice == "камінь" and computer_choice == "ножиці":
                print_response("Ви перемогли! Камінь б'є ножиці.")
            elif user_choice == "ножиці" and computer_choice == "папір":
                print_response("Ви перемогли! Ножиці ріжуть папір.")
            elif user_choice == "папір" and computer_choice == "камінь":
                print_response("Ви перемогли! Папір накриває камінь.")
            else:
                print_response("Комп'ютер переміг!")

            print_response("Чи бажаєте продовжити?")
            answer = get_user_input().lower().strip()

    def say_inspirational_quote(self):
        import random
        quotes = ["Життя – це 10% того, що з тобою трапляється, і 90% твоєї реакції на це.",
                  "Ти можеш зробити все, що забажаєш, якщо віриш у себе.",
                  "Твої найбільші обмеження – це не те, що ти є, а те, що ти думаєш про себе.",
                  "Будьмо зміною, яку хочемо бачити у світі.",
                  "Найбільша перемога – це перемога над самим собою.",
                  "Успіх – це не ключ до щастя. Щастя – це ключ до успіху. Якщо ви любите те, що робите, "
                  "ви будете успішні.",
                  "Життя надається тільки раз, але якщо жити правильно, одного разу достатньо.",
                  "Багато людей не досягають успіху, оскільки вони бояться ризикувати. Але без ризику немає нагороди.",
                  "Твої можливості ніколи не будуть більшими, ніж твої мрії.",
                  "Великі речі робляться не за допомогою сили, а за допомогою наполегливості."]

        random_quote = random.choice(quotes)
        print_response(Fore.MAGENTA + random_quote + Fore.RESET)

    def what_time_is_it(self):
        import datetime

        now = datetime.datetime.now()
        time = Fore.LIGHTRED_EX + str(now.time()) + Fore.RESET

        print_response(f"Поточна година: {time}.")

    def what_is_your_name(self):
        import random

        print_response("Мене звати " + Fore.BLUE + "Розумаха" + Fore.RESET + ". А тебе як?")
        user_name = get_user_input()
        compliments = ["Цікаве ім'я:)",
                       f"Ще ніколи не розмовляв із {user_name}.",
                       "Красиве ім'я, так звали мого друга.",
                       "Це ім'я має гарні магічні властивості)",
                       "Прекрасне ім'я!"]
        rnd = random.choice(compliments)
        print_response(rnd)

    def guess_the_number(self):
        answer = "так"
        while answer == "так":
            import random

            print_response("Напиши число від 1 до 10.")
            user_number = get_user_input()
            if user_number.isdigit():
                while int(user_number) < 1 or int(user_number) > 10 or not user_number.isdigit():
                    print_response("Некоректні дані. Спробуйте ще.")
                    user_number = get_user_input()
                bot_number = random.randint(1, 10)
                if int(user_number) == bot_number:
                    print_response("Вітаю! Ви вгадали число.")
                else:
                    print_response(f"Ви не вгадали:( Моє число - {bot_number}.")
            else:
                print_response("Некоректні дані.")

            print_response("Чи бажаєте продовжити?")
            answer = get_user_input().lower().strip()


def print_greeting():
    global topics_dictionary
    greeting = f"""Вітаю, мене звати Розумаха. Ви можете поставити мені запитання з таких тем: 
{', '.join(topics_dictionary.keys())}."""
    print_response(greeting)


init()  # initialize colorama

def get_file_name():
    now = datetime.datetime.now()
    file_name = f'діялог-{now.strftime("%Y-%m-%d_%H-%M")}.txt'
    return file_name

file_name = get_file_name()
with open(file_name, 'a', encoding='utf-8') as f:
    pass

def print_response(text, file_output=True):
    colored = Fore.BLUE + "[Бот]:" + Fore.RESET
    plain = "[Бот]:"
    if file_output:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(plain + ' ' + re.sub('\033\[[^m]*m', '', text) + '\n')
    print(f"{colored} {text}")

def get_user_input():
    text = input(Fore.YELLOW + Style.BRIGHT + "[Користувач]: " + Fore.RESET + Style.RESET_ALL)
    plain = "[Користувач]:"
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(plain + ' ' + re.sub('\033\[[^m]*m', '', text) + '\n')
    return text

def print_help():
    global topic_history
    help_message = ""
    if len(topic_history) == 0:
        help_message += "Введіть назву операції. "
    else:
        help_message += "Ви обрали операцію " + Fore.RED + f"«{get_current_topic()}»" + Fore.RESET + ". "

    help_message += f"\nДля виходу напишіть «вихід».\nДля повернення до попереднього блоку напишіть «назад»."
    print_response(help_message)

def get_current_topic():
    global topic_history
    if len(topic_history) == 0:
        return "Нічого"
    else:
        return topic_history[-1]


print_greeting()
input_text = 0
while True:
    if input_text == "вихід":
        break

    try:
        input_text = get_user_input()
    except KeyboardInterrupt:
        break

    if input_text.lower().strip() == "допомога":
        print_help()
        continue

    if input_text.lower().strip() == "назад":
        if len(topic_history) > 0:
            topic_history.pop()
        else:
            print_greeting()
            continue

    if input_text.lower().strip() == "вихід":
        break

    else:
        if input_text.lower().strip() in topics_dictionary:
            topic_history.append(input_text)
            print_response(f"Ви обрали тему: " + Fore.RED + f"«{get_current_topic()}»" + Fore.RESET + ".")

            # ФІЗИКА

            if input_text.lower().strip() == "фізика":
                print_response("Ви можете поставити мені запитання з таких тем:\n" +
                               "\n".join(topics_dictionary_1["фізика"]))

                while True:
                    input_text_phy = get_user_input()

                    if input_text_phy.lower().strip() in topics_dictionary["фізика"]:
                        topic_history.append(input_text_phy)

                        physics = Physics()

                        if input_text_phy.lower().strip() == "закон всесвітнього тяжіння ньютона" \
                                or input_text_phy.lower().strip() == "1" \
                                or input_text_phy.lower().strip() == "1 - закон всесвітнього тяжіння ньютона":
                            physics.calculate_gravity()
                        elif input_text_phy.lower().strip() == "закон збереження енергії" \
                                or input_text_phy.lower().strip() == "2" \
                                or input_text_phy.lower().strip() == "2 - закон збереження енергії":
                            physics.calculate_energy()
                        else:
                            physics.derive_planck_constant()
                    elif input_text_phy == "вихід":
                        input_text = "вихід"
                        break
                    elif input_text_phy == "назад":
                        print_response(f"""Ви можете поставити мені запитання з таких тем:
{', '.join(topics_dictionary.keys())}.""")
                        break
                    elif input_text_phy == "допомога":
                        print_help()
                    else:
                        print_response(f"Не знайдено такої теми. Ви можете поставити мені запитання з таких тем:\n"
                                       + "\n".join(topics_dictionary_1["фізика"]))
                        print_response("Бажаєте вийти із блоку «фізика» - напишіть «назад».")

            # МАТЕМАТИКА

            if input_text.lower().strip() == "математика":
                print_response(f"Ви можете поставити мені запитання з таких тем:\n"
                               + "\n".join(topics_dictionary_1["математика"]))

                while True:
                    input_text_math = get_user_input()

                    if input_text_math.lower().strip() in topics_dictionary["математика"]:
                        topic_history.append(input_text_math)

                        mathmatics = Mathematics()

                        if input_text_math.lower().strip() == "розв'язати квадратне рівняння" \
                                or input_text_math.lower().strip() == "1" \
                                or input_text_math.lower().strip() == "1 - розв'язати квадратне рівняння":
                            mathmatics.solve_quadratic_equation()
                        elif input_text_math.lower().strip() == "обчислити довжину дуги кола" \
                                or input_text_math.lower().strip() == "2" \
                                or input_text_math.lower().strip() == "2 - обчислити довжину дуги кола":
                            mathmatics.calculate_length_circle()
                        elif input_text_math.lower().strip() == "обчислити довжину відрізка між двома точками" \
                                or input_text_math.lower().strip() == "3" \
                                or input_text_math.lower().strip() == \
                                "3 - обчислити довжину відрізка між двома точками":
                            mathmatics.calculate_length_between_two_points()
                        elif input_text_math.lower().strip() == "вивести число π" \
                                or input_text_math.lower().strip() == "5" \
                                or input_text_math.lower().strip() == "5 - вивести число π":
                            mathmatics.print_value_pi()
                        else:
                            mathmatics.calculate_sin_cos()
                    elif input_text_math == "вихід":
                        input_text = "вихід"
                        break
                    elif input_text_math == "назад":
                        print_response(f"""Ви можете поставити мені запитання з таких тем:
{', '.join(topics_dictionary.keys())}.""")
                        break
                    elif input_text_math == "допомога":
                        print_help()
                    else:
                        print_response(f"Не знайдено такої теми. Ви можете поставити мені запитання з таких тем:\n"
                                       + "\n".join(topics_dictionary_1["математика"]))
                        print_response("Бажаєте вийти із блоку «математика» - напишіть «назад».")

            # ГЕОГРАФІЯ

            if input_text.lower().strip() == "географія":
                print_response(f"Ви можете поставити мені запитання з таких тем:\n"
                               + "\n".join(topics_dictionary_1["географія"]))

                while True:
                    input_text_geo = get_user_input()

                    if input_text_geo.lower().strip() in topics_dictionary["географія"]:
                        topic_history.append(input_text_geo)

                        geography = Geography()

                        if input_text_geo.lower().strip() == "яке найбільше озеро у світі за площею?" \
                                or input_text_geo.lower().strip() == "1" \
                                or input_text_geo.lower().strip() == "1 - яке найбільше озеро у світі за площею?":
                            geography.the_largest_lake()
                        elif input_text_geo.lower().strip() == \
                                "які дві держави мають найбільшу кількість кордонів з іншими державами?" \
                                or input_text_geo.lower().strip() == "2" \
                                or input_text_geo.lower().strip() == "2 - які дві держави мають найбільшу " \
                                                                     "кількість кордонів з іншими державами?":
                            geography.the_largest_number_of_borders()
                        elif input_text_geo.lower().strip() == "яке місто має найбільшу кількість населення у світі?" \
                                or input_text_geo.lower().strip() == "3" \
                                or input_text_geo.lower().strip() == "3 - яке місто має найбільшу кількість " \
                                                                     "населення у світі?":
                            geography.the_largest_population()
                        else:
                            geography.calculate_distance_between_two_points()
                    elif input_text_geo == "вихід":
                        input_text = "вихід"
                        break
                    elif input_text_geo == "назад":
                        print_response(f"""Ви можете поставити мені запитання з таких тем:
{', '.join(topics_dictionary.keys())}.""")
                        break
                    elif input_text_geo == "допомога":
                        print_help()
                    else:
                        print_response(f"Не знайдено такої теми. Ви можете поставити мені запитання з таких тем:\n"
                                       + "\n".join(topics_dictionary_1["географія"]))
                        print_response("Бажаєте вийти із блоку «географія» - напишіть «назад».")

            # ФІЛОЛОГІЯ

            if input_text.lower().strip() == "філологія":
                print_response(f"Ви можете поставити мені запитання з таких тем:\n"
                               + "\n".join(topics_dictionary_1["філологія"]))

                while True:
                    input_text_phil = get_user_input()

                    if input_text_phil.lower().strip() in topics_dictionary["філологія"]:
                        topic_history.append(input_text_phil)

                        philology = Philology()

                        if input_text_phil.lower().strip() == "яка різниця між present simple та present continuous?" \
                                or input_text_phil.lower().strip() == "1" \
                                or input_text_phil.lower().strip() == "1 - яка різниця між present simple та " \
                                                                      "present continuous?":
                            philology.the_difference_between_tenses()
                        elif input_text_phil.lower().strip() == "як утворити passive voice в present simple?" \
                                or input_text_phil.lower().strip() == "2" \
                                or input_text_phil.lower().strip() == "2 - як утворити passive voice в present simple?":
                            philology.how_formate_passive()
                        elif input_text_phil.lower().strip() == "як поставити іменник у давальному відмінку?" \
                                or input_text_phil.lower().strip() == "3" \
                                or input_text_phil.lower().strip() == "3 - як поставити іменник у давальному відмінку?":
                            philology.how_formate_nouns_in_dative()
                        else:
                            philology.say_right_stress()
                    elif input_text_phil == "вихід":
                        input_text = "вихід"
                        break
                    elif input_text_phil == "назад":
                        print_response(f"""Ви можете поставити мені запитання з таких тем:
{', '.join(topics_dictionary.keys())}.""")
                        break
                    elif input_text_phil == "допомога":
                        print_help()
                    else:
                        print_response(f"Не знайдено такої теми. Ви можете поставити мені запитання з таких тем:\n"
                                       + "\n".join(topics_dictionary_1["філологія"]))
                        print_response("Бажаєте вийти із блоку «філологія» - напишіть «назад».")

            # АСТРОНОМІЯ

            if input_text.lower().strip() == "астрономія":
                print_response(f"Ви можете поставити мені запитання з таких тем:\n"
                               + "\n".join(topics_dictionary_1["астрономія"]))

                while True:
                    input_text_astro = get_user_input()

                    if input_text_astro.lower().strip() in topics_dictionary["астрономія"]:
                        topic_history.append(input_text_astro)

                        astronomy = Astronomy()

                        if input_text_astro.lower().strip() == "що таке космічне випромінювання?" \
                                or input_text_astro.lower().strip() == "1" \
                                or input_text_astro.lower().strip() == "1 - що таке космічне випромінювання?":
                            astronomy.cosmic_radiation()
                        elif input_text_astro.lower().strip() == "що таке астероїди та комети?" \
                                or input_text_astro.lower().strip() == "2" \
                                or input_text_astro.lower().strip() == "2 - що таке астероїди та комети?":
                            astronomy.asteroids_and_comets()
                        else:
                            astronomy.processes_in_the_sun()
                    elif input_text_astro == "вихід":
                        input_text = "вихід"
                        break
                    elif input_text_astro == "назад":
                        print_response(f"""Ви можете поставити мені запитання з таких тем:
{', '.join(topics_dictionary.keys())}.""")
                        break
                    elif input_text_astro == "допомога":
                        print_help()
                    else:
                        print_response(f"Не знайдено такої теми. Ви можете поставити мені запитання з таких тем:\n"
                                       + "\n".join(topics_dictionary_1["астрономія"]))
                        print_response("Бажаєте вийти із блоку «астрономія» - напишіть «назад».")

            # ЗАГАЛЬНІ

            if input_text.lower().strip() == "загальні":
                print_response(f"Ви можете поставити мені запитання з таких тем:\n"
                               + "\n".join(topics_dictionary_1["загальні"]))

                while True:
                    input_text_gen = get_user_input()

                    if input_text_gen.lower().strip() in topics_dictionary["загальні"]:
                        topic_history.append(input_text_gen)

                        general = General()

                        if input_text_gen.lower().strip() == "який зараз місяць?" \
                                or input_text_gen.lower().strip() == "1" \
                                or input_text_gen.lower().strip() == "1 - який зараз місяць?":
                            general.what_month_is_it()
                        elif input_text_gen.lower().strip() == "котра година?" \
                                or input_text_gen.lower().strip() == "2" \
                                or input_text_gen.lower().strip() == "2 - котра година?":
                            general.what_time_is_it()
                        elif input_text_gen.lower().strip() == "як тебе звати?" \
                                or input_text_gen.lower().strip() == "3" \
                                or input_text_gen.lower().strip() == "3 - як тебе звати?":
                            general.what_is_your_name()
                        elif input_text_gen.lower().strip() == "пограти у вгадай число між 1 та 10" \
                                or input_text_gen.lower().strip() == "4" \
                                or input_text_gen.lower().strip() == "4 - пограти у вгадай число між 1 та 10":
                            general.guess_the_number()
                        elif input_text_gen.lower().strip() == "пограти у камінь-ножиці-папір" \
                                or input_text_gen.lower().strip() == "5" \
                                or input_text_gen.lower().strip() == "5 - пограти у камінь-ножиці-папір":
                            general.play_rock_paper_scissors()
                        else:
                            general.say_inspirational_quote()
                    elif input_text_gen == "вихід":
                        input_text = "вихід"
                        break
                    elif input_text_gen == "назад":
                        print_response(f"""Ви можете поставити мені запитання з таких тем:
{', '.join(topics_dictionary.keys())}.""")
                        break
                    elif input_text_gen == "допомога":
                        print_help()
                    else:
                        print_response(f"Не знайдено такої теми. Ви можете поставити мені запитання з таких тем:\n"
                                       + "\n".join(topics_dictionary_1["загальні"]))
                        print_response("Бажаєте вийти із блоку «загальні» - напишіть «назад».")
        else:
            print_response(f"""Я не знаю цієї теми. Ви можете поставити мені запитання з таких тем: 
{", ".join(topics_dictionary.keys())}.""")
            continue

print_response("Радий був поспілкуватися, до зустрічі!")