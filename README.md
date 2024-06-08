# Projeto de Geração de Orçamento em PDF

Este projeto é uma aplicação Python que gera um PDF contendo informações de orçamento para um projeto. A aplicação coleta dados do usuário, calcula o valor total do projeto e insere essas informações em um template de PDF.

## Funcionalidades

- Entrada de dados do usuário (descrição do projeto, horas estimadas, valor da hora, prazo estimado).
- Cálculo do valor total do projeto.
- Geração de um PDF com os dados fornecidos.

## Tecnologias Utilizadas

- Python 3
- Biblioteca [FPDF](http://www.fpdf.org/) para a criação de PDFs.

## Como Usar

1. **Instalação das Dependências:**

   Certifique-se de ter o Python instalado. Você pode instalar a biblioteca `FPDF` usando pip:
   ```sh
   pip install fpdf
   ```

2. **Execução do Script:**

   Salve o código fornecido em um arquivo, por exemplo, `gerar_orcamento.py`, e execute-o:
   ```sh
   python gerar_orcamento.py
   ```

3. **Entrar com os Dados:**

   O script solicitará a entrada de:
   - Descrição do projeto
   - Total de horas estimadas
   - Valor da hora trabalhada
   - Prazo estimado para conclusão

4. **Geração do PDF:**

   Após a entrada dos dados, o script gerará um arquivo PDF nomeado `Orçamento.pdf` contendo as informações fornecidas.

## Estrutura do Código

```python
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
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias. Para isso, faça um fork do repositório, crie uma branch para sua funcionalidade, faça o commit e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para obter mais informações.

## Contato

Para dúvidas ou sugestões, entre em contato com wiliswasunb@gmail.com.

---

Este arquivo README fornece uma visão geral do projeto, instruções de uso, e detalhes sobre as tecnologias utilizadas. Sinta-se à vontade para adaptá-lo conforme necessário para melhor atender às suas necessidades.
