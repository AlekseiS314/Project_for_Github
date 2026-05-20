import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку на комплексной плоскости
x_real = np.linspace(-np.pi, np.pi, 150)
y_imag = np.linspace(-np.pi, np.pi, 150)
X, Y = np.meshgrid(x_real, y_imag)
Z = X + 1j * Y

# Вычисляем косинус
W = np.cos(Z)

# ПЕРВЫЙ СЛАЙД: ДЕЙСТВИТЕЛЬНАЯ ЧАСТЬ
fig1 = plt.figure(figsize=(14, 6))
fig1.suptitle('Функция f(z) = cos(z): Действительная часть',
             fontsize=18, fontweight='bold', y=0.98)

# 3D поверхность действительной части
ax1 = fig1.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, W.real, cmap='viridis',
                        alpha=0.95, linewidth=0,
                        antialiased=True, rstride=3, cstride=3,
                        edgecolor='black')

ax1.set_title('3D поверхность: Re(cos z)', fontsize=16, pad=15)
ax1.set_xlabel('Re(z)', fontsize=12, labelpad=10)
ax1.set_ylabel('Im(z)', fontsize=12, labelpad=10)
ax1.set_zlabel('Re(f(z))', fontsize=12, labelpad=10)
ax1.view_init(elev=35, azim=45)
fig1.colorbar(surf1, ax=ax1, shrink=0.7, pad=0.1, label='Re(cos z)')

# Срез вдоль действительной оси
ax2 = fig1.add_subplot(122)
x_real_line = np.linspace(-3*np.pi/2, 3*np.pi/2, 400)
z_real_line = x_real_line + 0j
w_real_line = np.cos(z_real_line)

ax2.plot(x_real_line, w_real_line.real, 'b-', linewidth=3, label='Re(cos z), Im(z)=0')
ax2.plot(x_real_line, w_real_line.imag, 'r-', linewidth=3, label='Im(cos z), Im(z)=0')

ax2.set_title('Срез вдоль действительной оси (Im(z) = 0)  → cos(x)', fontsize=16, pad=15)
ax2.set_xlabel('Re(z)', fontsize=14)
ax2.set_ylabel('f(z)', fontsize=14)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(loc='best', fontsize=11)

# Отмечаем особые точки (нули косинуса)
for n in range(-2, 3):
    x_val = (2*n+1)*np.pi/2
    ax2.axvline(x=x_val, color='red', linestyle=':', alpha=0.3, linewidth=1)

plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()

# ВТОРОЙ СЛАЙД: МНИМАЯ ЧАСТЬ
fig2 = plt.figure(figsize=(14, 6))
fig2.suptitle('Функция f(z) = cos(z): Мнимая часть',
             fontsize=18, fontweight='bold', y=0.98)

# 3D поверхность мнимой части
ax1 = fig2.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, W.imag, cmap='plasma',
                        alpha=0.95, linewidth=0,
                        antialiased=True, rstride=3, cstride=3,
                        edgecolor='black')

ax1.set_title('3D поверхность: Im(cos z)', fontsize=16, pad=15)
ax1.set_xlabel('Re(z)', fontsize=12, labelpad=10)
ax1.set_ylabel('Im(z)', fontsize=12, labelpad=10)
ax1.set_zlabel('Im(f(z))', fontsize=12, labelpad=10)
ax1.view_init(elev=35, azim=45)
fig2.colorbar(surf1, ax=ax1, shrink=0.7, pad=0.1, label='Im(cos z)')

# Срез вдоль мнимой оси
ax2 = fig2.add_subplot(122)
y_imag_line = np.linspace(-3, 3, 400)
z_imag_line = 0 + 1j * y_imag_line
w_imag_line = np.cos(z_imag_line)

ax2.plot(y_imag_line, w_imag_line.real, 'b-', linewidth=3, label='Re(cos z), Re(z)=0')
ax2.plot(y_imag_line, w_imag_line.imag, 'r-', linewidth=3, label='Im(cos z), Re(z)=0')

ax2.set_title('Срез вдоль мнимой оси (Re(z) = 0)  → cosh(y)', fontsize=16, pad=15)
ax2.set_xlabel('Im(z)', fontsize=14)
ax2.set_ylabel('f(z)', fontsize=14)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(loc='best', fontsize=11)

plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()