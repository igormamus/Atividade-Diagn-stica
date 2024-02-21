import numpy as np
import matplotlib.pyplot as plt
#Felipe Ribas, igor Mamus, Leonardo Marques e João Manfrim


# Solicitar ao usuário para inserir um ângulo em graus
angle_degrees = float(input("Insira um ângulo em graus (0 < ângulo < 180): "))

# Converter o ângulo para radianos
angle_radians = np.radians(angle_degrees)

# Coordenadas do círculo trigonométrico
x = np.cos(angle_radians)
y = np.sin(angle_radians)

# Linha para o seno
plt.plot([0, x], [0, y], label='Seno', color='blue', linewidth=2)

# Linha para o cosseno
plt.plot([x, x], [0, y], label='Cosseno', color='green', linewidth=2)

# Linha para a tangente
tan_length = 1.5  # comprimento da linha para a tangente
tan_end_x = x + tan_length * np.cos(angle_radians)
tan_end_y = y + tan_length * np.sin(angle_radians)
plt.plot([x, tan_end_x], [y, tan_end_y], label='Tangente', color='red', linewidth=2)

# Círculo trigonométrico
circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='dotted', linewidth=1)
plt.gca().add_patch(circle)

# Configurações adicionais
plt.title('Círculo Trigonométrico para um Ângulo Específico')
plt.xlabel('Cos(theta)')
plt.ylabel('Sin(theta)')
plt.axis('equal')  # Garante que os eixos x e y tenham a mesma escala
plt.grid(True)
plt.legend()

# Exibir o gráfico
plt.show()
