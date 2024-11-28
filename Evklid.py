import matplotlib.pyplot as plt
import numpy as np

# Считываем данные из файла
x_coords = []
y_coords = []
classes = []

# Определяем цвета для каждого класса
colors = {
    1: 'blue',
    2: 'red',
    3: 'green',
    # Добавьте больше классов и их цветов по мере необходимости
}

with open('result.txt', 'r') as file:
    for line in file:
        # Разделяем строку на значения и преобразуем их в целые числа
        x, y, class_num = map(int, line.split())
        x_coords.append(x)
        y_coords.append(y)
        classes.append(class_num)

# Преобразуем списки в массивы NumPy для удобства
x_coords = np.array(x_coords)
y_coords = np.array(y_coords)

# Вычисляем Евклидово расстояние между всеми точками и выводим результаты
for i in range(len(x_coords)):
    for j in range(i + 1, len(x_coords)):
        dist = np.sqrt((x_coords[i] - x_coords[j]) **
                       2 + (y_coords[i] - y_coords[j])**2)
        print(f'Расстояние между точками {i} и {j}: {dist}')

# Создаем график
plt.figure(figsize=(8, 6))

# Отображаем точки с учетом класса
for class_num in set(classes):  # Уникальные номера классов
    indices = [i for i, c in enumerate(classes) if c == class_num]
    plt.scatter([x_coords[i] for i in indices], [y_coords[i] for i in indices],
                color=colors.get(class_num, 'black'),
                marker='o', label=f'Класс {class_num}')

# Настраиваем график
plt.title('Двумерный график точек')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)
plt.legend()  # Добавляем легенду

# Показываем график
plt.show()
