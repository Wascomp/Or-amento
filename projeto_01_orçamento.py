# -*- coding: utf-8 -*-
"""Projeto 01 - Orçamento

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z66-v0C3ZRStoms-b-xry0N_0NaDvvfT
"""

!pip install fpdf

from fpdf import FPDF

# Funções para obter os dados do usuário
projeto = input("Digite a descrição do projeto: ")
horas_estimadas = int(input("Digite o total de horas estimadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
prazo = input("Digite o prazo estimado para conclusão: ")

# Cálculo do valor total do projeto
valor_total = horas_estimadas * valor_hora

# Criação do PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.image("template.png", x=0, y=0, w=210)  # Ajuste a largura conforme necessário

# Adicionando textos ao PDF
pdf.text(115, 145, projeto)
pdf.text(115, 160, str(horas_estimadas))
pdf.text(115, 175, str(valor_hora))
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

# Salvando o PDF
pdf.output("Orçamento.pdf")

print("Orçamento gerado com sucesso!")