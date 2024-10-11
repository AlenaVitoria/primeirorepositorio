# Função para gerar o plano de treino personalizado
def gerar_plano_treino(biotipo, dias_treino, tipo_exercicio):
    # Estruturas de treino baseadas nos dias disponíveis
    planos = {
        "1": {
            "descricao": "Treino Full Body",
            "exercicios": [
                "Agachamento: 3 séries de 10-12 repetições",
                "Supino: 3 séries de 10-12 repetições",
                "Remada Unilateral: 3 séries de 10-12 repetições",
                "Flexão de Braços: 3 séries de 10-15 repetições",
                "Desenvolvimento com Halteres: 3 séries de 10-12 repetições"
            ]
        },
        "3": {
            "descricao": "Treino ABC",
            "exercicios": {
                "A": [
                    "Supino: 3 séries de 10-12 repetições",
                    "Flexão de Braços: 3 séries de 10-15 repetições",
                    "Tríceps na Máquina: 3 séries de 10-12 repetições"
                ],
                "B": [
                    "Remada Unilateral: 3 séries de 10-12 repetições",
                    "Pull-Ups ou Lat Pulldown: 3 séries de 8-10 repetições",
                    "Rosca Direta: 3 séries de 10-12 repetições"
                ],
                "C": [
                    "Agachamento: 3 séries de 10-12 repetições",
                    "Desenvolvimento com Halteres: 3 séries de 10-12 repetições",
                    "Avanço: 3 séries de 10-12 repetições"
                ]
            }
        },
        "5": {
            "descricao": "Treino ABCDE",
            "exercicios": {
                "A": [
                    "Supino: 3 séries de 10-12 repetições",
                    "Flexão de Braços: 3 séries de 10-15 repetições"
                ],
                "B": [
                    "Remada Unilateral: 3 séries de 10-12 repetições"
                ],
                "C": [
                    "Agachamento: 3 séries de 10-12 repetições"
                ],
                "D": [
                    "Desenvolvimento com Halteres: 3 séries de 10-12 repetições"
                ],
                "E": [
                    "Avanço: 3 séries de 10-12 repetições"
                ]
            }
        }
    }

    # Gerando o plano de treino com base nas informações do usuário
    if dias_treino in planos:
        plano = planos[dias_treino]
        print(f"\nPlano de Treino Personalizado:\n\n{plano['descricao']}:\n")
        
        if dias_treino == "3":
            for dia, exercicios in plano['exercicios'].items():
                print(f"**{dia}:**")
                for exercicio in exercicios:
                    print(f"  - {exercicio}")
                print()  # Linha em branco entre os dias
        else:
            for exercicio in plano['exercicios']:
                print(f"  - {exercicio}")
    else:
        print("Número de dias inválido.")

# Função principal para interagir com o usuário
def main():
    print("Bem-vindo ao Assistente de Personal Trainer!")
    
    # Coletando informações do usuário
    biotipo = input("Escolha seu biotipo corporal (Ectomorfo, Mesomorfo, Endomorfo): ")
    dias_treino = input("Quantos dias por semana você pode treinar? (1, 3 ou 5): ")
    tipo_exercicio = input("Escolha seu tipo de exercício preferido (Funcional, Maquinário, Peso Livre, Cardio, HIIT): ")

    # Gerando o plano de treino
    gerar_plano_treino(biotipo, dias_treino, tipo_exercicio)

# Executar a função principal
if __name__ == "__main__":
    main()
