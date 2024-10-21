# -*- coding: UTF-8 -*-
"""
	JOGO DA FORCA v1.0
	Criado por Luiz R. Dererita – 2024
"""

from colorama import Fore
import os
import shutil
import random


class JogoDaForca():
	""" Classe principal do jogo """
	def __init__(self, palavras_dicas):
		# Variáveis para armazenar a palavra e a dica atuais
		self.palavras_dicas = palavras_dicas
		self.palavra, self.dica = random.choice(palavras_dicas)
		# Lista para armazenar as respostas do jogador
		self.letras = []
		# Armazena a palavra escondida
		self.palavra_secreta = ""
		# Número de erros cometidos (máximo 6 erros)
		self.erros = 0
		# Pontuação do jogador
		self.pontos = 0
		# Flag para ligar/desligar as dicas
		self.dicas = False
		
	def exibir_titulo(self, titulo):
		""" Exibe o título do jogo """
		# Obtém largura e altura da tela
		colunas, linhas = shutil.get_terminal_size()
		print("—"* colunas)
		print(" "*9+f"{Fore.YELLOW}{titulo}{Fore.RESET}")
		print("—"* colunas)
		
	def exibir_layout(self):
		""" Exibe o layout do jogo na tela """
		# Edita a palavra secreta para serem exibidas apenas as letras descobertas
		self.palavra_secreta = ""
		
		for letra in self.palavra:
			if letra in self.letras:
				self.palavra_secreta += letra.upper()
			else:
				self.palavra_secreta += "_"
		
		# Exibe as informações sobre o jogo
		print(f"{Fore.CYAN}Digite \"?\" para exibir a dica{Fore.RESET}")
		# Exibe os pontos do jogador
		print(f"PONTOS: {self.pontos}\n")
		
		if self.erros == 0:		
			# Exibe a forca na tela
			print(" "* len(self.palavra) + "|—" + "—  ")
			print(" "* len(self.palavra) + "|" + "    ")
			print(self.palavra_secreta + "| " + "   ")
			
		elif self.erros == 1:		
			# Exibe a forca na tela
			print(" "* len(self.palavra) + "|—" + "—o ")
			print(" "* len(self.palavra) + "|" + "    ")
			print(self.palavra_secreta + "| " + "   ")
			
		elif self.erros == 2:		
			# Exibe a forca na tela
			print(" "* len(self.palavra) + "|—" + "—o ")
			print(" "* len(self.palavra) + "|" + "  | ")
			print(self.palavra_secreta + "| " + "   ")
			
		elif self.erros == 3:		
			# Exibe a forca na tela
			print(" "* len(self.palavra) + "|—" + "—o ")
			print(" "* len(self.palavra) + "|" + " /| ")
			print(self.palavra_secreta + "| " + "   ")
			
		elif self.erros == 4:		
			# Exibe a forca na tela
			print(" "* len(self.palavra) + "|—" + "—o ")
			print(" "* len(self.palavra) + "|" + " /|\\")
			print(self.palavra_secreta + "| " + "   ")
			
		elif self.erros == 5:		
			# Exibe a forca na tela
			print(" "* len(self.palavra) + "|—" + "—o ")
			print(" "* len(self.palavra) + "|" + " /|\\")
			print(self.palavra_secreta + "| " + "/  ")
			
		elif self.erros >= 6:		
			# Exibe a forca na tela
			print(" "* len(self.palavra) + "|—" + f"—{Fore.RED}o{Fore.RESET} ")
			print(" "* len(self.palavra) + "|" + f" {Fore.RED}/|\\{Fore.RESET}")
			print(self.palavra_secreta + "| " + f"{Fore.RED}/ \\{Fore.RESET}")
		
		print()
		
		print(f"A palavra contém {Fore.YELLOW}{len(self.palavra)}{Fore.RESET} letras")
		if self.dicas:
			print(f"Dica: {Fore.YELLOW}{self.dica}{Fore.RESET}")
		else:
			print("Dica: --")
		
	def exibir_palavra_dica(self):
		""" Exibe a palavra e a dica """
		if self.palavra and self.dica:
			print(f"Palavra: {self.palavra}\nDica: {self.dica}")
		else:
			print("Nenhuma palavra encontrada.")
	
	def exibir_cursor(self):
		""" Exibe o cursor na tela """
		return input(f"{Fore.YELLOW}>>>{Fore.RESET} ")
	
	def proxima_palavra(self):
		""" Inicia a próxima fase """
		# Remove a última palavra descoberta da lista
		self.palavras_dicas.remove((self.palavra, self.dica))
		# Variáveis para armazenar a palavra e a dica atuais
		self.palavra, self.dica = random.choice(self.palavras_dicas)
		# Lista para armazenar as respostas do jogador
		self.letras = []
		# Número de erros cometidos (máximo 6 erros)
		self.erros = 0
		# Pontuação do jogador
		if self.dicas:
			self.pontos += 5
		else:
			self.pontos += 10
		# Flag para ligar/desligar as dicas
		self.dicas = False
		
		
	def fim_de_jogo(self):
		""" Encerra a partida """
		print(f"{Fore.LIGHTRED_EX}FIM DE JOGO! :({Fore.RESET}")
		
	def executar(self):
		""" Inicia a execução do jogo """
		while True:
			os.system('clear') or None
			# Exibe o título do jogo na tela
			jogo.exibir_titulo("JOGO DA FORCA")
			# Exibe o layout do jogo a cada jogada
			jogo.exibir_layout()
			# Checa se o jogador adivinhou a palavra e inicia a próxima fase
			if jogo.palavra_secreta.lower() == jogo.palavra:
				print(f"{Fore.GREEN}ACERTOU! ;D{Fore.RESET}")
				jogo.proxima_palavra()
			# Checa se o jogador cometeu 7 erros
			elif jogo.erros >= 7:
				jogo.fim_de_jogo()
				break
			# Exibe o cursor na tela
			resposta = jogo.exibir_cursor()
			# Checa se a letra informada está na palavra secreta e a adiciona á lista de acertos
			if resposta in jogo.palavra:
				jogo.letras.append(resposta)
			# Checa se a resposta do jogador é um pedido para exibir a dica
			elif resposta == "?":
				jogo.dicas = True
			# Se a resposta do jogador for inválida ele perde uma vida
			else:
				jogo.erros += 1
			print("".join(jogo.letras))


# Lista de palavras e dicas
palavras_dicas = [
    ("abacaxi", "Fruta tropical com coroa"),
    ("elefante", "Maior mamífero terrestre"),
    ("astronauta", "Profissional que viaja ao espaço"),
    ("biblioteca", "Lugar com muitos livros"),
    ("computador", "Máquina para processar dados"),
    ("girassol", "Flor que segue o sol"),
    ("oceano", "Grande massa de água salgada"),
    ("montanha", "Elevação natural do terreno"),
    ("pinguim", "Ave que não voa e vive na Antártida"),
    ("vulcão", "Montanha que expele lava"),
    ("cachorro", "Melhor amigo do homem"),
    ("guitarra", "Instrumento musical de cordas"),
    ("avião", "Meio de transporte aéreo"),
    ("bicicleta", "Veículo de duas rodas"),
    ("chocolate", "Doce feito de cacau"),
    ("diamante", "Pedra preciosa"),
    ("escola", "Lugar de aprendizado"),
    ("futebol", "Esporte popular no Brasil"),
    ("gelo", "Água em estado sólido"),
    ("hipopótamo", "Animal grande que vive na água"),
    ("igreja", "Lugar de culto religioso"),
    ("jardim", "Área com plantas e flores"),
    ("kiwi", "Fruta verde e peluda"),
    ("leão", "Rei da selva"),
    ("macaco", "Animal que gosta de bananas"),
    ("navio", "Grande embarcação"),
    ("orquestra", "Grupo de músicos"),
    ("piano", "Instrumento musical de teclas"),
    ("quadro", "Objeto para pendurar na parede"),
    ("relógio", "Objeto para ver as horas"),
    ("sorvete", "Sobremesa gelada"),
    ("tartaruga", "Animal com casco"),
    ("urso", "Animal grande e peludo"),
    ("violino", "Instrumento musical de cordas"),
    ("xadrez", "Jogo de tabuleiro"),
    ("zoológico", "Lugar com muitos animais"),
    ("abelha", "Inseto que produz mel"),
    ("banana", "Fruta amarela e curva"),
    ("cavalo", "Animal usado para montaria"),
    ("dente", "Parte da boca usada para mastigar"),
    ("eleição", "Processo de escolha de representantes"),
    ("fada", "Ser mágico com asas"),
    ("gato", "Animal doméstico que mia"),
    ("hotel", "Lugar para se hospedar"),
    ("ilha", "Terreno cercado de água"),
    ("jornal", "Publicação diária de notícias"),
    ("ketchup", "Condimento feito de tomate"),
    ("lua", "Satélite natural da Terra"),
    ("museu", "Lugar com exposições de arte e história"),
    ("noite", "Período do dia sem luz solar"),
    ("ovo", "Alimento oval produzido por aves"),
    ("praia", "Faixa de areia junto ao mar"),
    ("quintal", "Área externa de uma casa"),
    ("rio", "Curso de água natural"),
    ("sol", "Estrela que ilumina a Terra"),
    ("tigre", "Grande felino listrado"),
    ("urso-polar", "Urso que vive no Ártico"),
    ("vaca", "Animal que produz leite"),
    ("xícara", "Recipiente para beber chá ou café"),
    ("zebra", "Animal com listras"),
    ("abóbora", "Fruta usada no Halloween"),
    ("baleia", "Maior animal marinho"),
    ("cacto", "Planta que vive no deserto"),
    ("dromedário", "Animal com uma corcova"),
    ("esquilo", "Animal que coleta nozes"),
    ("foca", "Animal que vive no gelo"),
    ("girafa", "Animal com pescoço longo"),
    ("hiena", "Animal que ri"),
    ("iguana", "Réptil que muda de cor"),
    ("jacaré", "Réptil com dentes afiados"),
    ("koala", "Animal que vive na Austrália"),
    ("lobo", "Animal que uiva"),
    ("morcego", "Único mamífero que voa"),
    ("nuvem", "Formação de vapor de água no céu"),
    ("ostra", "Molusco que produz pérolas"),
    ("panda", "Urso preto e branco"),
    ("quati", "Animal com focinho longo"),
    ("raposa", "Animal astuto e veloz"),
    ("sapo", "Anfíbio que pula"),
    ("tucano", "Ave com bico grande"),
    ("urso-panda", "Urso preto e branco que come bambu"),
    ("vagalume", "Inseto que brilha no escuro"),
    ("xilofone", "Instrumento musical de teclas")
]

# Cria uma instancia da classe principal do jogo
jogo = JogoDaForca(palavras_dicas)
# Inicia o loop de execução do jogo
jogo.executar()
