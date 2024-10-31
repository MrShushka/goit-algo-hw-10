import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції для обчислення
def f(x):
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення площі під кривою
def monte_carlo_integration(f, a, b, num_points=10000):
    x_random = np.random.uniform(a, b, num_points)  # Генерація випадкових x в межах [a, b]
    y_random = f(x_random)  # Обчислення f(x) для кожного випадкового x
    avg_height = np.mean(y_random)  # Середнє значення f(x) (висоти)
    return (b - a) * avg_height  # Площа під кривою

# Обчислення значення інтеграла методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)
print("Інтеграл методом Монте-Карло:", monte_carlo_result)

# Аналітичне обчислення значення інтеграла за допомогою quad
analytical_result, error = spi.quad(f, a, b)
print("Інтеграл методом quad:", analytical_result)
print("Похибка:", abs(analytical_result - monte_carlo_result))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2, label="f(x) = x^2")

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label="Область інтеграції")

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()