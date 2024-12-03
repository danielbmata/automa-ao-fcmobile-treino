import pyautogui

# Exibe a posição do mouse enquanto você o move pela tela
print("Posicione o mouse onde deseja capturar a coordenada.")
input("Pressione Enter quando o mouse estiver no local correto...")

# Exibe as coordenadas
print(f"As coordenadas são: {pyautogui.position()}")


