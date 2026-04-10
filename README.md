Aventura na Floresta Encantada
Este projeto consiste em um protótipo de jogo de aventura textual (RPG) em Python. O sistema foi desenvolvido como um exercício de refatoração, focado em corrigir erros de lógica, implementar funcionalidades de exploração e garantir as melhores práticas de programação.

Funcionalidades
Inicialização Dinâmica: O jogador define seu nome e inicia com 100 pontos de vida e inventário vazio.

Sistema de Exploração: Navegação entre áreas (Clareira, Caminho, Caverna e Pântano) usando comandos de direção em português.

Gestão de Itens: Mecânicas para listar, coletar (pegar) e utilizar (usar) itens do cenário.

Eventos de Sobrevivência: Desafios automáticos em locais perigosos que reduzem a vida do jogador.

Condições de Vitória: O jogo monitora o inventário e a localização para determinar o sucesso na busca pelo Amuleto Mágico.

Conceitos Aplicados
Estruturas de Dados: Uso de Dicionários Aninhados para representar o mapa e suas propriedades.

Manipulação de Variáveis Globais: Controle de estado do jogador (global) entre as funções.

Tratamento de Strings: Uso de .lower(), .strip() e .replace() para garantir que os comandos do usuário sejam interpretados corretamente.

Lógica de Controle: Implementação de while loops para o ciclo principal e estruturas condicionais para as ações do jogo.

Estrutura do Projeto
Variáveis de Estado: player_name, player_health, inventory e current_location.

Mapa (locations): Contém as descrições, saídas disponíveis, itens presentes e desafios de cada local.

Funções Principais:

display_status(): Renderiza a interface de status do jogador.

main_game_loop(): Gerencia a lógica de entrada, movimentação e condições de fim de jogo.

Como Executar
Certifique-se de ter o Python 3.x instalado em sua máquina.

Salve o código em um arquivo (ex: floresta.py).

Abra o terminal ou prompt de comando na pasta do arquivo.

Execute o jogo com o comando:
python floresta.py
