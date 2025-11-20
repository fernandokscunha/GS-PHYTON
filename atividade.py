   import pandas as pd

# Base de Dados com Profissões e Futuro Possível
BASE_CONHECIMENTO = [
    {
        'Profissao_Atual': 'Contabilidade Manual',
        'Risco_Automacao': 'Alto',
        'Habilidades_Core': 'Excel, Contas',
        'Area_Foco_Futuro': 'Analise de Dados e IA',
        'Habilidades_Futuro_Necessarias': 'Python, Analise Critica, Ética em IA',
        'Inclusao_Status': 'Jovem Aprendiz'
    },
    {
        'Profissao_Atual': 'Atendimento ao Cliente (Call Center)',
        'Risco_Automacao': 'Alto',
        'Habilidades_Core': 'Comunicação, Rotinas',
        'Area_Foco_Futuro': 'UX (Experiência do Usuário)',
        'Habilidades_Futuro_Necessarias': 'Empatia, Pensamento Critico, Design Thinking',
        'Inclusao_Status': 'Mulher'
    },
    {
        'Profissao_Atual': 'Montagem de Peças Repetitiva',
        'Risco_Automacao': 'Alto',
        'Habilidades_Core': 'Mecânica Básica',
        'Area_Foco_Futuro': 'Economia Verde e Energia Renovável',
        'Habilidades_Futuro_Necessarias': 'Sustentabilidade, Tecnologias Verdes, Liderança',
        'Inclusao_Status': 'Maior de 50'
    },
    {
        'Profissao_Atual': 'Analista de RH Tradicional',
        'Risco_Automacao': 'Médio',
        'Habilidades_Core': 'Recrutamento, Rotinas de RH',
        'Area_Foco_Futuro': 'Saúde Mental Corporativa',
        'Habilidades_Futuro_Necessarias': 'Psicologia Positiva, Gestão de Ambientes Híbridos',
        'Inclusao_Status': 'PCD'
    }
]

#  Criando DataFrame para consulta estruturada
df_profissoes = pd.DataFrame(BASE_CONHECIMENTO)


#  Função inteligente de busca com aproximações
def buscar_trilha(profissao, inclusao, base):

    #  Função interna para normalização → (função dentro de função )
    def normalizar(texto):
        return texto.strip().lower()

    prof_normalizada = normalizar(profissao)
    inc_normalizada = normalizar(inclusao)

    melhor_match_prof = None
    melhor_match_inc = None

    for perfil in base:
        # Se encontrou profissão e inclusão exata 
        if normalizar(perfil['Profissao_Atual']) == prof_normalizada and \
           normalizar(perfil['Inclusao_Status']) == inc_normalizada:
            return perfil, "match_total"

        # Se encontrou profissão semelhante 
        if prof_normalizada in normalizar(perfil['Profissao_Atual']):
            melhor_match_prof = perfil

        # Se encontrou inclusão semelhante 
        if inc_normalizada in normalizar(perfil['Inclusao_Status']):
            melhor_match_inc = perfil

    # Retornos alternativos caso não ache tudo 
    if melhor_match_prof:
        return melhor_match_prof, "match_profissao"
    if melhor_match_inc:
        return melhor_match_inc, "match_inclusao"

    return None, "nenhum_match"


#  Simulação geral para relatório
def simular_base(base):
    print("\n--- Simulação com Perfis Cadastrados ---\n")
    resultados = []

    for item in base:
        match, _ = buscar_trilha(item['Profissao_Atual'], item['Inclusao_Status'], base)
        if match:
            print(f"✅ {item['Profissao_Atual']} → {match['Area_Foco_Futuro']}")
            resultados.append(match['Area_Foco_Futuro'])

    print("\n📌 Áreas mais recomendadas no futuro:")
    for area in sorted(set(resultados)):
        print(f"- {area}")


#  Menu principal com repetição
def iniciar_sistema():
    while True:
        print("\n====== Menu Principal ======")
        print("1 - Buscar trilha profissional")
        print("2 - Ver base de profissões")
        print("3 - Simular com dados existentes")
        print("4 - Sair")
        print("============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            profissao = input("\nDigite sua profissão atual: ")
            inclusao = input("Digite seu status de inclusão: ")

            resultado, tipo = buscar_trilha(profissao, inclusao, BASE_CONHECIMENTO)

            print("\n Resultado da Busca:\n")
            if tipo == "match_total":
                print(" Perfil encontrado com exatidão!")
            elif tipo == "match_profissao":
                print(" Sugestão baseada na PROFISSÃO semelhante:")
            elif tipo == "match_inclusao":
                print(" Sugestão baseada no seu grupo de INCLUSÃO:")
            else:
                print(" Nenhuma sugestão encontrada ainda para esse perfil.")
                continue

            print(f"→ Profissão base: {resultado['Profissao_Atual']}")
            print(f"→ Risco de Automação: {resultado['Risco_Automacao']}")
            print(f"→ Área sugerida: {resultado['Area_Foco_Futuro']}")
            print(f"→ Habilidades Futuras: {resultado['Habilidades_Futuro_Necessarias']}")

        elif opcao == "2":
            print("\n Base de Profissões Cadastradas:\n")
            print(df_profissoes)

        elif opcao == "3":
            simular_base(BASE_CONHECIMENTO)

        elif opcao == "4":
            print("\n Sistema encerrado. Até mais!")
            break

        else:
            print("\n Opção inválida. Tente novamente!")


# Executa o sistema
iniciar_sistema()
