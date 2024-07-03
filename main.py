# Imports.
import pyautogui
from time import sleep


# Funções
def ralizarTarefa():
    #     Acessando o site em favoritos e indo a parte necessária
    pyautogui.doubleClick(77, 97, duration=1)

    # DailyTasks Page
    pyautogui.doubleClick(519, 330, duration=1)

    # ColetandoNome
    pyautogui.doubleClick(265, 601, duration=1)
    pyautogui.scroll(-500)

    # ColetandoImagem
    pyautogui.doubleClick(264, 539, duration=1)



# Abrindo Navegador no Desktop
pyautogui.hotkey('winleft', 'd')
pyautogui.doubleClick(1556,792,duration=1)

# Acessando e executando no primeiro Usuario
#     Acessando o usuario na homeScreen
pyautogui.doubleClick(526,528,duration=1)

ralizarTarefa()
# -----------------------------------------------------------------------------------------
#Primeira Conta (OK)
# AlterandoConta Navegador

pyautogui.click( 1546,58,duration=1)
pyautogui.click( 1330,261,duration=1)
ralizarTarefa()



