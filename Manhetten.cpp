#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <sstream>

struct Point {
    int x;
    int y;
    int class_num;
};

// Функция для вычисления Манхэттенского расстояния
double manhattanDistance(const Point& p1, const Point& p2) {
    return std::abs(p1.x - p2.x) + std::abs(p1.y - p2.y);
}

int main() {
    std::ifstream file("result.txt");
    if (!file.is_open()) {
        std::cerr << "Не удалось открыть файл result.txt" << std::endl;
        return 1;
    }

    std::vector<Point> points;
    std::string line;

    // Считываем данные из файла
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        Point point;
        if (iss >> point.x >> point.y >> point.class_num) {
            points.push_back(point);
        } else {
            std::cerr << "Ошибка при чтении строки: " << line << std::endl;
        }
    }

    file.close();

    // Вычисляем Манхэттенское расстояние между всеми точками и выводим результаты
    for (size_t i = 0; i < points.size(); ++i) {
        for (size_t j = i + 1; j < points.size(); ++j) {
            double dist = manhattanDistance(points[i], points[j]);
            std::cout << "Расстояние между точками " << i << " и " << j << ": " << dist << std::endl;
        }
    }

    return 0;
}