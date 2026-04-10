# =========================
# Variáveis globais
# =========================
player_name = ""
player_health = 0
inventory = []
current_location = ""

# =========================
# Mapa do jogo
# =========================
locations = {
    "Clareira Tranquila": {
        "description": "Você está em uma clareira ensolarada. Há caminhos para Leste e Sul.",
        "east": "Caminho da Floresta",
        "south": "Pântano Misterioso",
        "items": ["poção pequena"]
    },
    "Caminho da Floresta": {
        "description": "Uma trilha estreita serpenteia pela floresta. Você pode ir para Oeste ou Norte.",
        "west": "Clareira Tranquila",
        "north": "Caverna Sombria"
    },
    "Caverna Sombria": {
        "description": "Uma caverna escura e úmida. Há um brilho fraco no fundo. Você pode voltar para Sul.",
        "south": "Caminho da Floresta",
        "items": ["amuleto mágico"]
    },
    "Pântano Misterioso": {
        "description": "Um pântano denso e perigoso. Você sente um arrepio. Há um caminho para Norte.",
        "north": "Clareira Tranquila",
        "challenge": True
    }
}

# =========================
# Função de status
# =========================
def display_status():
    print("\n--- Status do Jogador ---")
    print(f"Nome: {player_name}")
    print(f"Vida: {player_health}")
    print(f"Inventário: {', '.join(inventory) if inventory else 'Vazio'}")
    print("------------------------")

# =========================
# Loop principal
# =========================
def main_game_loop():
    global player_name, player_health, current_location, inventory

    # Inicialização
    player_name = input("Qual o seu nome, aventureiro? ")
    player_health = 100
    current_location = "Clareira Tranquila"
    inventory = []

    direcoes = {
        "norte": "north",
        "sul": "south",
        "leste": "east",
        "oeste": "west"
    }

    game_active = True

    while game_active:
        display_status()

        print(f"\nVocê está em: {current_location}")
        print(locations[current_location]["description"])

        # Saídas disponíveis
        exits = []
        for direction in ["north", "south", "east", "west"]:
            if direction in locations[current_location]:
                exits.append(direction.capitalize())

        print(f"Saídas disponíveis: {', '.join(exits)}")

        # Itens no local
        if "items" in locations[current_location] and locations[current_location]["items"]:
            print(f"Itens neste local: {', '.join(locations[current_location]['items'])}")

        # Desafio
        if locations[current_location].get("challenge", False):
            print("Um monstro do pântano te ataca!")
            player_health -= 30
            print(f"Você perdeu 30 de vida. Vida atual: {player_health}")
            locations[current_location]["challenge"] = False

        # Entrada do jogador
        action = input("\nO que você quer fazer? (andar, pegar, usar, sair): ").lower().strip()

        # =========================
        # ANDAR
        # =========================
        if action.startswith("andar"):
            direction_input = action.replace("andar ", "")

            if direction_input in direcoes:
                direcao_ingles = direcoes[direction_input]

                if direcao_ingles in locations[current_location]:
                    current_location = locations[current_location][direcao_ingles]
                else:
                    print("Você não pode ir nessa direção.")
            else:
                print("Direção inválida.")

        # =========================
        # PEGAR ITEM
        # =========================
        elif action.startswith("pegar"):
            item_to_pick = action.replace("pegar ", "")

            if "items" in locations[current_location] and item_to_pick in locations[current_location]["items"]:
                inventory.append(item_to_pick)
                locations[current_location]["items"].remove(item_to_pick)
                print(f"Você pegou: {item_to_pick}")
            else:
                print("Este item não está aqui.")

        # =========================
        # USAR ITEM
        # =========================
        elif action.startswith("usar"):
            item_to_use = action.replace("usar ", "")

            if item_to_use in inventory:
                if item_to_use == "poção pequena":
                    player_health = min(100, player_health + 20)
                    inventory.remove(item_to_use)
                    print("Você usou a poção e recuperou 20 de vida.")

                elif item_to_use == "amuleto mágico":
                    print("Você usou o Amuleto Mágico! 🎉 PARABÉNS, você venceu o jogo!")
                    game_active = False

                else:
                    print("Você não sabe como usar este item.")
            else:
                print("Você não tem este item.")

        # =========================
        # SAIR
        # =========================
        elif action == "sair":
            print("Você saiu do jogo.")
            game_active = False

        else:
            print("Comando inválido.")

        # =========================
        # FIM DE JOGO
        # =========================
        if player_health <= 0:
            print("\n💀 Sua vida chegou a zero. Fim de jogo!")
            game_active = False

        if current_location == "Caverna Sombria" and "amuleto mágico" in inventory and game_active:
            print("\n🏆 Você encontrou o Amuleto Mágico e venceu o jogo!")
            game_active = False


# =========================
# Iniciar jogo
# =========================
main_game_loop()