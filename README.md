# Automação de Tarefas com PyAutoGUI

Este projeto utiliza a biblioteca PyAutoGUI para automatizar a navegação em um site e a execução de tarefas diárias. O script foi desenvolvido para abrir o navegador, acessar uma página específica e coletar informações clicando em coordenadas específicas na tela. Em seguida, ele alterna entre diferentes contas de usuário para realizar a mesma tarefa.

## Pré-requisitos

- Python 3.x
- Biblioteca PyAutoGUI
  - Para instalar, execute: `pip install pyautogui`

## Descrição do Script

O script realiza as seguintes operações:

1. Abre o navegador no desktop.
2. Acessa um usuário específico na tela inicial.
3. Executa a função `ralizarTarefa` que:
   - Acessa um site específico a partir dos favoritos.
   - Navega até a página de tarefas diárias.
   - Coleta o nome e a imagem necessários.
4. Alterna entre diferentes contas de usuário no navegador e repete a tarefa.

   ## Instruções e Avisos
   - Este script depende das coordenadas específicas da tela. Certifique-se de que a resolução da tela **(1600x900)** e a disposição dos elementos estejam corretas.
   - A automação pode falhar se houver mudanças na interface do usuário do site ou do navegador.
   
  - Certifique-se de que o navegador e os elementos a serem clicados estão na mesma posição que as coordenadas especificadas no script.
  -  Para adicionar novos usuários, adicione as coordenadas de troca no navegador e chame a função ralizarTarefa() conforme necessário.

