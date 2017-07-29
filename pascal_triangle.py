# функция по расчету треугольника паскаля, на вход принимает число строк
def pascal_triangle(rows):
    triangle = []
    # для нулевого ряда задаем значение вручную
    triangle.append([1])
    for n in range(1, rows+1):
        last_row = triangle[n-1]
        new_row = []
        #первый элемент совпадает с первым предыдущей строки, можно просто вставлять 1
        new_row.append(last_row[0])
        if n > 1:
            for z in range(1, len(last_row)):
                new_row.append((last_row[z-1]+last_row[z]))
        #тоже, наверное, можно просто последним элементом ставить 1
        new_row.append(last_row[-1])
        triangle.append(new_row)
    return triangle


# выводим в консоль модным треугольником
def centered(massiv):
    max_length = len(str(massiv[-1])) - 2    #нижняя строка без знаков []
    for n in massiv:
        stroka = str(n)[1:-1]
        print (str(len(n) - 1), stroka.center(max_length))




centered(pascal_triangle(17))


