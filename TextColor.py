#    TextColor
#    Personalizador de texto em terminal.
#    Copyright (C) 2022  Osvaldo Lucas da Silva Figueiredo
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA
#
#    Contact:
#    E-mail: osvaldo@gruponcgp.com.br


#Não mexa nos valores das variáveis
#Cores da fonte
PRETO = "30m"
VERMELHO = "31m"
VERDE = "32m"
AMARELO = "33m"
AZUL = "34m"
MAGENTA = "35m"
CIANO = "36m"
BRANCO = "37m"

#Cores de fundo:
FUNDO_PRETO = "40"
FUNDO_VERMELHO = "41"
FUNDO_VERDE = "42"
FUNDO_AMARELO = "43"
FUNDO_AZUL = "44"
FUNDO_MAGENTA = "45"
FUNDO_CIANO = "46"
FUNDO_BRANCO = "47"

#Modo ANSI:
NORMAL = "0"
NEGRITO = "1"
LEVE = "2"
ITALICO = "3"
SUBLINHADO = "4"
NEGATIVO = "7"
RISCADO = "9"
INVISIVEL = "8"

def demonstracao():
    print(negrito_amarelo("FUNÇÕES SIMPLES:"))
    print(" TextColor.normal(\"Texto Normal\") = " + normal("Texto Normal"))
    print(" TextColor.negrito(\"Texto Normal\") = " + negrito("Texto Normal"))
    print(" TextColor.leve(\"Texto Normal\") = " + leve("Texto Normal"))
    print(" TextColor.italico(\"Texto Normal\") = " + italico("Texto Normal"))
    print(" TextColor.sublinhado(\"Texto Normal\") = " + sublinhado("Texto Normal"))
    print(" TextColor.negativo(\"Texto Normal\") = " + negativo("Texto Normal"))
    print(" TextColor.riscado(\"Texto Normal\") = " + riscado("Texto Normal"))
    print(" TextColor.invisivel(\"Texto Normal\") = " + invisivel("Texto Normal"))
    
    print(negrito_amarelo("\nFUNÇÕES DE FONTE COLORIDAS:"))
    print(" TextColor.azul(\"Texto Normal\") = " + azul("Texto Normal"))
    print(" TextColor.negrito_amarelo(\"Texto Normal\") = " + negrito_amarelo("Texto Normal"))
    print(" TextColor.negrito_vermelho(\"Texto Normal\") = " + negrito_vermelho("Texto Normal"))
    print(" TextColor.leve_verde(\"Texto Normal\") = " + leve_verde("Texto Normal"))
    print(" TextColor.italico_preto(\"Texto Normal\") = " + italico_preto("Texto Normal"))
    print(" TextColor.sublinhado_branco(\"Texto Normal\") = " + sublinhado_branco("Texto Normal"))
    print(" TextColor.negativo_ciano(\"Texto Normal\") = " + negativo_ciano("Texto Normal"))
    print(" TextColor.riscado_magenta(\"Texto Normal\") = " + riscado_magenta("Texto Normal"))
    print(" TextColor.riscado_ciano(\"Texto Normal\") = " + riscado_ciano("Texto Normal"))
    print(negrito("Variações: ") + negrito_magenta("NEGRITO, ") + leve_magenta("LEVE, ") + italico_magenta("ITÁLICO, ") + sublinhado_magenta("SUBLINHADO") + ", " + negativo_magenta("NEGATIVO") + " e " + riscado_magenta("RISCADO"))
    print(negrito("Cores: ") + negrito_azul("AZUL, ") + negrito_amarelo("AMARELO, ") + negrito_vermelho("VERMELHO, ") + negrito_verde("VERDE, ") + negrito_preto("PRETO, ") + negrito_ciano("CIANO, ") + negrito_magenta("MAGENTA") + " e " + negrito_branco("BRANCO"))

    print(negrito_amarelo("\nFUNÇÕES DE CONTORNO:"))
    print(" TextColor.contorno_preto(\"Texto Normal\", TextColor.AZUL, TextColor.NEGRITO) = " + contorno_preto("Texto Normal", AZUL, NEGRITO))
    print(" TextColor.contorno_azul(\"Texto Normal\", TextColor.CIANO, TextColor.NEGRITO) = " + contorno_azul("Texto Normal", CIANO, NEGRITO))
    print(" TextColor.contorno_verde(\"Texto Normal\", TextColor.BRANCO, TextColor.NEGRITO) = " + contorno_verde("Texto Normal", BRANCO, NEGRITO))
    print(" TextColor.contorno_amarelo(\"Texto Normal\", TextColor.AZUL, TextColor.NEGRITO) = " + contorno_amarelo("Texto Normal", AZUL, NEGRITO))
    print(" TextColor.contorno_vermelho(\"Texto Normal\", TextColor.BRANCO, TextColor.NEGRITO) = " + contorno_vermelho("Texto Normal", BRANCO, NEGRITO))
    print(" TextColor.contorno_ciano(\"Texto Normal\", TextColor.PRETO, TextColor.NEGRITO) = " + contorno_ciano("Texto Normal", PRETO, NEGRITO))
    print(" TextColor.contorno_magenta(\"Texto Normal\", TextColor.BRANCO, TextColor.NEGRITO) = " + contorno_magenta("Texto Normal", BRANCO, NEGRITO))
    print(" TextColor.contorno_branco(\"Texto Normal\", TextColor.AZUL, TextColor.NEGRITO) = " + contorno_branco("Texto Normal", AZUL, NEGRITO))
    print(negrito("Variações: ") + negrito_magenta("NEGRITO, ") + leve_magenta("LEVE, ") + italico_magenta("ITÁLICO, ") + sublinhado_magenta("SUBLINHADO") + ", " + negativo_magenta("NEGATIVO") + " e " + riscado_magenta("RISCADO"))
    print(negrito("Cores: ") + negrito_azul("AZUL, ") + negrito_amarelo("AMARELO, ") + negrito_vermelho("VERMELHO, ") + negrito_verde("VERDE, ") + negrito_preto("PRETO, ") + negrito_ciano("CIANO, ") + negrito_magenta("MAGENTA") + " e " + negrito_branco("BRANCO"))

    print(negrito_amarelo("\nFUNÇÕES DE ESPECIFICAS:"))
    print(" TextColor.colorido(\"Texto Normal\", TextColor.AZUL, TextColor.NEGRITO) = " + colorido("Texto Normal", AZUL, NEGRITO))
    print(" TextColor.contorno_colorido(\"Texto Normal\", TextColor.VERMELHO, TextColor.SUBLINHADO, TextColor.FUNDO_AMARELO) = " + contorno_colorido("Texto Normal", VERMELHO, SUBLINHADO, FUNDO_AMARELO))
    print(" TextColor.fonte(\"Texto Normal\", TextColor.RISCADO) = " + fonte("Texto Normal", RISCADO))
    print(negrito("Variações: ") + negrito_magenta("NEGRITO, ") + leve_magenta("LEVE, ") + italico_magenta("ITÁLICO, ") + sublinhado_magenta("SUBLINHADO") + ", " + negativo_magenta("NEGATIVO") + " e " + riscado_magenta("RISCADO"))
    print(negrito("Cores: ") + negrito_azul("AZUL, ") + negrito_amarelo("AMARELO, ") + negrito_vermelho("VERMELHO, ") + negrito_verde("VERDE, ") + negrito_preto("PRETO, ") + negrito_ciano("CIANO, ") + negrito_magenta("MAGENTA") + " e " + negrito_branco("BRANCO"))
    print(negrito("Contornos: ") + contorno_preto("FUNDO_PRETO", AZUL, NEGRITO) + ", " + contorno_azul("FUNDO_AZUL", CIANO, NEGRITO) + ", " +  contorno_verde("FUNDO_VERDE", BRANCO, NEGRITO) + ", " +  contorno_amarelo("FUNDO_AMARELO", AZUL, NEGRITO) + ", " +  contorno_vermelho("FUNDO_VERMELHO", BRANCO, NEGRITO) + ", " +  contorno_ciano("FUNDO_CIANO", PRETO, NEGRITO) + ", " +  contorno_magenta("FUNDO_MAGENTA", BRANCO, NEGRITO) + " e " +  contorno_branco("FUNDO_BRANCO", AZUL, NEGRITO))
    
    print(negrito_amarelo("\nOUTRAS FUNÇÕES:"))
    print("Para escrever diretamente no terminal basta adicionar " + verde("\"escrever_\"") + " no ínicio da função")
    print(" TextColor.escrever_negrito_azul(\"Texto Normal\") = "+ negrito_azul("\nTexto Normal"))
    
    print("\n\nPressione " + sublinhado_vermelho("ENTER") + " para encerrar.")
    encerrar = input()


def colorido(texto, cor_texto, fonte):
    saida = ("\033["+ fonte +";"+ cor_texto+ texto+ "\033[0;0;0m")
    return saida

def contorno_colorido(texto, cor_texto, fonte, corfundo):
    saida = ("\033["+corfundo+ ";"+ fonte+";"+ cor_texto+ texto+ "\033[0;0;0m")
    return saida

def fonte(texto, fonte):
    saida = ("\033[" + fonte + "m" + texto + "\033[0;0;0m")
    return saida

#CONTORNOS MALEAVEIS
def contorno_preto(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_PRETO)
    return exibir

def contorno_vermelho(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_VERMELHO)
    return exibir

def contorno_verde(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_VERDE)
    return exibir
def contorno_amarelo(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_AMARELO)
    return exibir

def contorno_azul(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_AZUL)
    return exibir

def contorno_magenta(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_MAGENTA)
    return exibir

def contorno_ciano(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_CIANO)
    return exibir

def contorno_branco(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_BRANCO)
    return exibir

#CORES EM TOM NORMAL
def normal(texto):
    exibir = fonte(texto, NORMAL)
    return exibir

def invisivel(texto):
    exibir = fonte(texto, INVISIVEL)
    return exibir

def preto(texto):
    exibir = colorido(texto, PRETO, NORMAL)
    return exibir

def vermelho(texto):
    exibir = colorido(texto, VERMELHO, NORMAL)
    return exibir

def verde(texto):
    exibir = colorido(texto, VERDE, NORMAL)
    return exibir

def amarelo(texto):
    exibir = colorido(texto, AMARELO, NORMAL)
    return exibir

def azul(texto):
    exibir = colorido(texto, AZUL, NORMAL)
    return exibir

def magenta(texto):
    exibir = colorido(texto, MAGENTA, NORMAL)
    return exibir

def ciano(texto):
    exibir = colorido(texto, CIANO, NORMAL)
    return exibir

def branco(texto):
    exibir = colorido(texto, BRANCO, NORMAL)
    return exibir

#CORES EM NEGRITO
def negrito(texto):
    exibir = fonte(texto, NEGRITO)
    return exibir

def negrito_preto(texto):
    exibir = colorido(texto, PRETO, NEGRITO)
    return exibir

def negrito_vermelho(texto):
    exibir = colorido(texto, VERMELHO, NEGRITO)
    return exibir

def negrito_verde(texto):
    exibir = colorido(texto, VERDE, NEGRITO)
    return exibir

def negrito_amarelo(texto):
    exibir = colorido(texto, AMARELO, NEGRITO)
    return exibir

def negrito_azul(texto):
    exibir = colorido(texto, AZUL, NEGRITO)
    return exibir

def negrito_magenta(texto):
    exibir = colorido(texto, MAGENTA, NEGRITO)
    return exibir

def negrito_ciano(texto):
    exibir = colorido(texto, CIANO, NEGRITO)
    return exibir

def negrito_branco(texto):
    exibir = colorido(texto, BRANCO, NEGRITO)
    return exibir

#CORES EM BAIXA INTENSIDADE
def leve(texto):
    exibir = fonte(texto, LEVE)
    return exibir

def leve_preto(texto):
    exibir = colorido(texto, PRETO, LEVE)
    return exibir

def leve_vermelho(texto):
    exibir = colorido(texto, VERMELHO, LEVE)
    return exibir

def leve_verde(texto):
    exibir = colorido(texto, VERDE, LEVE)
    return exibir

def leve_amarelo(texto):
    exibir = colorido(texto, AMARELO, LEVE)
    return exibir

def leve_azul(texto):
    exibir = colorido(texto, AZUL, LEVE)
    return exibir

def leve_magenta(texto):
    exibir = colorido(texto, MAGENTA, LEVE)
    return exibir

def leve_ciano(texto):
    exibir = colorido(texto, CIANO, LEVE)
    return exibir

def leve_branco(texto):
    exibir = colorido(texto, BRANCO, LEVE)
    return exibir

#CORES EM ITÁLICO
def italico(texto):
    exibir = fonte(texto, ITALICO)
    return exibir

def italico_preto(texto):
    exibir = colorido(texto, PRETO, ITALICO)
    return exibir

def italico_vermelho(texto):
    exibir = colorido(texto, VERMELHO, ITALICO)
    return exibir

def italico_verde(texto):
    exibir = colorido(texto, VERDE, ITALICO)
    return exibir

def italico_amarelo(texto):
    exibir = colorido(texto, AMARELO, ITALICO)
    return exibir

def italico_azul(texto):
    exibir = colorido(texto, AZUL, ITALICO)
    return exibir

def italico_magenta(texto):
    exibir = colorido(texto, MAGENTA, ITALICO)
    return exibir

def italico_ciano(texto):
    exibir = colorido(texto, CIANO, ITALICO)
    return exibir

def italico_branco(texto):
    exibir = colorido(texto, BRANCO, ITALICO)
    return exibir

#CORES SUBLINHADO
def sublinhado(texto):
    exibir = fonte(texto, SUBLINHADO)
    return exibir

def sublinhado_preto(texto):
    exibir = colorido(texto, PRETO, SUBLINHADO)
    return exibir

def sublinhado_vermelho(texto):
    exibir = colorido(texto, VERMELHO, SUBLINHADO)
    return exibir

def sublinhado_verde(texto):
    exibir = colorido(texto, VERDE, SUBLINHADO)
    return exibir

def sublinhado_amarelo(texto):
    exibir = colorido(texto, AMARELO, SUBLINHADO)
    return exibir

def sublinhado_azul(texto):
    exibir = colorido(texto, AZUL, SUBLINHADO)
    return exibir

def sublinhado_magenta(texto):
    exibir = colorido(texto, MAGENTA, SUBLINHADO)
    return exibir

def sublinhado_ciano(texto):
    exibir = colorido(texto, CIANO, SUBLINHADO)
    return exibir

def sublinhado_branco(texto):
    exibir = colorido(texto, BRANCO, SUBLINHADO)
    return exibir

#CORES EM NEGATIVO
def negativo(texto):
    exibir = fonte(texto, NEGATIVO)
    return exibir

def negativo_preto(texto):
    exibir = colorido(texto, PRETO, NEGATIVO)
    return exibir

def negativo_vermelho(texto):
    exibir = colorido(texto, VERMELHO, NEGATIVO)
    return exibir

def negativo_verde(texto):
    exibir = colorido(texto, VERDE, NEGATIVO)
    return exibir

def negativo_amarelo(texto):
    exibir = colorido(texto, AMARELO, NEGATIVO)
    return exibir

def negativo_azul(texto):
    exibir = colorido(texto, AZUL, NEGATIVO)
    return exibir

def negativo_magenta(texto):
    exibir = colorido(texto, MAGENTA, NEGATIVO)
    return exibir

def negativo_ciano(texto):
    exibir = colorido(texto, CIANO, NEGATIVO)
    return exibir

def negativo_branco(texto):
    exibir = colorido(texto, BRANCO, NEGATIVO)
    return exibir

#CORES EM RISCADO
def riscado(texto):
    exibir = fonte(texto, RISCADO)
    return exibir

def riscado_preto(texto):
    exibir = colorido(texto, PRETO, RISCADO)
    return exibir

def riscado_vermelho(texto):
    exibir = colorido(texto, VERMELHO, RISCADO)
    return exibir

def riscado_verde(texto):
    exibir = colorido(texto, VERDE, RISCADO)
    return exibir

def riscado_amarelo(texto):
    exibir = colorido(texto, AMARELO, RISCADO)
    return exibir

def riscado_azul(texto):
    exibir = colorido(texto, AZUL, RISCADO)
    return exibir

def riscado_magenta(texto):
    exibir = colorido(texto, MAGENTA, RISCADO)
    return exibir

def riscado_ciano(texto):
    exibir = colorido(texto, CIANO, RISCADO)
    return exibir

def riscado_branco(texto):
    exibir = colorido(texto, BRANCO, RISCADO)
    return exibir

# FUNÇÕES DE SAÍDA EM TERMINAL

def escreva_colorido(texto, cor_texto, fonte):
    saida = ("\033["+ fonte +";"+ cor_texto+ texto+ "\033[0;0;0m")
    print(saida)

def escreva_contorno_colorido(texto, cor_texto, fonte, corfundo):
    saida = ("\033["+corfundo+ ";"+ fonte+";"+ cor_texto+ texto+ "\033[0;0;0m")
    print(saida)

def escreva_fonte(texto, fonte):
    saida = ("\033[" + fonte + "m" + texto + "\033[0;0;0m")
    print(saida)

#CONTORNOS MALEAVEIS
def escreva_contorno_preto(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_PRETO)
    print(exibir)

def escreva_contorno_vermelho(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_VERMELHO)
    print(exibir)

def escreva_contorno_verde(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_VERDE)
    print(exibir)

def escreva_contorno_amarelo(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_AMARELO)
    print(exibir)

def escreva_contorno_azul(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_AZUL)
    print(exibir)

def escreva_contorno_magenta(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_MAGENTA)
    print(exibir)

def escreva_contorno_ciano(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_CIANO)
    print(exibir)

def escreva_contorno_branco(texto, cor, ansi):
    exibir = contorno_colorido(texto, cor, ansi, FUNDO_BRANCO)
    print(exibir)

#CORES EM TOM NORMAL
def escreva_normal(texto):
    exibir = fonte(texto, NORMAL)
    print(exibir)

def escreva_invisivel(texto):
    exibir = fonte(texto, INVISIVEL)
    print(exibir)

def escreva_preto(texto):
    exibir = colorido(texto, PRETO, NORMAL)
    print(exibir)

def escreva_vermelho(texto):
    exibir = colorido(texto, VERMELHO, NORMAL)
    print(exibir)

def escreva_verde(texto):
    exibir = colorido(texto, VERDE, NORMAL)
    print(exibir)

def escreva_amarelo(texto):
    exibir = colorido(texto, AMARELO, NORMAL)
    print(exibir)

def escreva_azul(texto):
    exibir = colorido(texto, AZUL, NORMAL)
    print(exibir)

def escreva_magenta(texto):
    exibir = colorido(texto, MAGENTA, NORMAL)
    print(exibir)

def escreva_ciano(texto):
    exibir = colorido(texto, CIANO, NORMAL)
    print(exibir)

def escreva_branco(texto):
    exibir = colorido(texto, BRANCO, NORMAL)
    print(exibir)

#CORES EM NEGRITO
def escreva_negrito(texto):
    exibir = fonte(texto, NEGRITO)
    print(exibir)

def escreva_negrito_preto(texto):
    exibir = colorido(texto, PRETO, NEGRITO)
    print(exibir)

def escreva_negrito_vermelho(texto):
    exibir = colorido(texto, VERMELHO, NEGRITO)
    print(exibir)

def escreva_negrito_verde(texto):
    exibir = colorido(texto, VERDE, NEGRITO)
    print(exibir)

def escreva_negrito_amarelo(texto):
    exibir = colorido(texto, AMARELO, NEGRITO)
    print(exibir)

def escreva_negrito_azul(texto):
    exibir = colorido(texto, AZUL, NEGRITO)
    print(exibir)

def escreva_negrito_magenta(texto):
    exibir = colorido(texto, MAGENTA, NEGRITO)
    print(exibir)

def escreva_negrito_ciano(texto):
    exibir = colorido(texto, CIANO, NEGRITO)
    print(exibir)

def escreva_negrito_branco(texto):
    exibir = colorido(texto, BRANCO, NEGRITO)
    print(exibir)

#CORES EM BAIXA INTENSIDADE
def escreva_leve(texto):
    exibir = fonte(texto, LEVE)
    print(exibir)

def escreva_leve_preto(texto):
    exibir = colorido(texto, PRETO, LEVE)
    print(exibir)

def escreva_leve_vermelho(texto):
    exibir = colorido(texto, VERMELHO, LEVE)
    print(exibir)

def escreva_leve_verde(texto):
    exibir = colorido(texto, VERDE, LEVE)
    print(exibir)

def escreva_leve_amarelo(texto):
    exibir = colorido(texto, AMARELO, LEVE)
    print(exibir)

def escreva_leve_azul(texto):
    exibir = colorido(texto, AZUL, LEVE)
    print(exibir)

def escreva_leve_magenta(texto):
    exibir = colorido(texto, MAGENTA, LEVE)
    print(exibir)

def escreva_leve_ciano(texto):
    exibir = colorido(texto, CIANO, LEVE)
    print(exibir)

def escreva_leve_branco(texto):
    exibir = colorido(texto, BRANCO, LEVE)
    print(exibir)

#CORES EM ITÁLICO
def escreva_italico(texto):
    exibir = fonte(texto, ITALICO)
    print(exibir)

def escreva_italico_preto(texto):
    exibir = colorido(texto, PRETO, ITALICO)
    print(exibir)

def escreva_italico_vermelho(texto):
    exibir = colorido(texto, VERMELHO, ITALICO)
    print(exibir)

def escreva_italico_verde(texto):
    exibir = colorido(texto, VERDE, ITALICO)
    print(exibir)

def escreva_italico_amarelo(texto):
    exibir = colorido(texto, AMARELO, ITALICO)
    print(exibir)

def escreva_italico_azul(texto):
    exibir = colorido(texto, AZUL, ITALICO)
    print(exibir)

def escreva_italico_magenta(texto):
    exibir = colorido(texto, MAGENTA, ITALICO)
    print(exibir)

def escreva_italico_ciano(texto):
    exibir = colorido(texto, CIANO, ITALICO)
    print(exibir)

def escreva_italico_branco(texto):
    exibir = colorido(texto, BRANCO, ITALICO)
    print(exibir)

#CORES SUBLINHADO
def escreva_sublinhado(texto):
    exibir = fonte(texto, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_preto(texto):
    exibir = colorido(texto, PRETO, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_vermelho(texto):
    exibir = colorido(texto, VERMELHO, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_verde(texto):
    exibir = colorido(texto, VERDE, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_amarelo(texto):
    exibir = colorido(texto, AMARELO, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_azul(texto):
    exibir = colorido(texto, AZUL, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_magenta(texto):
    exibir = colorido(texto, MAGENTA, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_ciano(texto):
    exibir = colorido(texto, CIANO, SUBLINHADO)
    print(exibir)

def escreva_sublinhado_branco(texto):
    exibir = colorido(texto, BRANCO, SUBLINHADO)
    print(exibir)

#CORES EM NEGATIVO
def escreva_negativo(texto):
    exibir = fonte(texto, NEGATIVO)
    print(exibir)

def escreva_negativo_preto(texto):
    exibir = colorido(texto, PRETO, NEGATIVO)
    print(exibir)

def escreva_negativo_vermelho(texto):
    exibir = colorido(texto, VERMELHO, NEGATIVO)
    print(exibir)

def escreva_negativo_verde(texto):
    exibir = colorido(texto, VERDE, NEGATIVO)
    print(exibir)

def escreva_negativo_amarelo(texto):
    exibir = colorido(texto, AMARELO, NEGATIVO)
    print(exibir)

def escreva_negativo_azul(texto):
    exibir = colorido(texto, AZUL, NEGATIVO)
    print(exibir)

def escreva_negativo_magenta(texto):
    exibir = colorido(texto, MAGENTA, NEGATIVO)
    print(exibir)

def escreva_negativo_ciano(texto):
    exibir = colorido(texto, CIANO, NEGATIVO)
    print(exibir)

def escreva_negativo_branco(texto):
    exibir = colorido(texto, BRANCO, NEGATIVO)
    print(exibir)

#CORES EM RISCADO
def escreva_riscado(texto):
    exibir = fonte(texto, RISCADO)
    print(exibir)

def escreva_riscado_preto(texto):
    exibir = colorido(texto, PRETO, RISCADO)
    print(exibir)

def escreva_riscado_vermelho(texto):
    exibir = colorido(texto, VERMELHO, RISCADO)
    print(exibir)

def escreva_riscado_verde(texto):
    exibir = colorido(texto, VERDE, RISCADO)
    print(exibir)

def escreva_riscado_amarelo(texto):
    exibir = colorido(texto, AMARELO, RISCADO)
    print(exibir)

def escreva_riscado_azul(texto):
    exibir = colorido(texto, AZUL, RISCADO)
    print(exibir)

def escreva_riscado_magenta(texto):
    exibir = colorido(texto, MAGENTA, RISCADO)
    print(exibir)

def escreva_riscado_ciano(texto):
    exibir = colorido(texto, CIANO, RISCADO)
    print(exibir)

def escreva_riscado_branco(texto):
    exibir = colorido(texto, BRANCO, RISCADO)
    print(exibir)

