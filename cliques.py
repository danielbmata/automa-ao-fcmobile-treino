import pyautogui
import time

# Definindo as coordenadas de cada um dos 6 cliques
clicar_coords = [
    (223, 193),  # Clique 1
    (161, 266),  # Clique 2
    (515, 206),  # Clique 3
    (826, 593),  # Clique 4
    (779, 591),  # Clique 5
    (52, 70)     # Clique 6
]

# Espera um pouco para você preparar a tela do BlueStacks
time.sleep(3)

# Função para realizar os 6 cliques em posições diferentes
def realizar_cliques():
    for i, coord in enumerate(clicar_coords):
        pyautogui.click(coord[0], coord[1])
        time.sleep(2)  # Intervalo de 1 segundo entre os cliques

        # Se for o clique 4, adicionar um intervalo maior
        if i == 3:  # O clique 4 está no índice 3
            print("Esperando 6 segundos entre o clique 4 e o clique 5...")
            time.sleep(6)  # Aumenta o tempo de espera entre o clique 4 e o clique 5

# Loop infinito para repetir os 6 cliques
while True:
    realizar_cliques()
    time.sleep(3)  # Tempo de espera entre a repetição dos 6 cliques
