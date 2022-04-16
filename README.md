# TEXTCOLOR
É um arquivo Python com multiplas funções para colorir o terminal alterar as caracteristicas das palavras no terminal

## INSTALAÇÃO

1. Baixe o arquivo e o copie para a raiz do seu projeto Python.
2. Em seguida adicione  `import TextColor` no arquivo Python para importar as funções.


## FUNÇÃO DEMONSTRAÇÃO

A função  `TextColor.demonstracao()` Mostrará todas as funções e seus resultados no terminal

## MANEIRAS DE USAR

Exemplo 1
```
print("Destacamos em " + TextColor.negrito("negrito") + " o problema.")

```

##### Retorno
Destacamos em **negrito** o problema.

Exemplo 2
```
print("Para termos em ingles usamos " + TextColor.italico("textos em itálico") + " para representá-los.")

```

##### Retorno
Para termos em ingles usamos *textos em itálico* para representá-los.


## FUNÇÕES SIMPLES:                                                                                                              
```
 TextColor.normal("Texto Normal")
 TextColor.negrito("Texto Normal")
 TextColor.leve("Texto Normal")
 TextColor.italico("Texto Normal")
 TextColor.sublinhado("Texto Normal")
 TextColor.negativo("Texto Normal")
 TextColor.riscado("Texto Normal")
 TextColor.invisivel("Texto Normal")
```

## FUNÇÕES DE FONTE COLORIDAS:                                                                                                    
```
 TextColor.azul("Texto Normal")
 TextColor.negrito_amarelo("Texto Normal")
 TextColor.negrito_vermelho("Texto Normal")
 TextColor.leve_verde("Texto Normal")
 TextColor.italico_preto("Texto Normal")
 TextColor.sublinhado_branco("Texto Normal")
 TextColor.negativo_ciano("Texto Normal")
 TextColor.riscado_magenta("Texto Normal")
 TextColor.riscado_ciano("Texto Normal")                                  
```

Variações: NEGRITO, LEVE, ITÁLICO, SUBLINHADO, NEGATIVO e RISCADO                                                              

Cores: AZUL, AMARELO, VERMELHO, VERDE, PRETO, CIANO, MAGENTA e BRANCO                                                          

## FUNÇÕES DE CONTORNO:                                                                                                           
```
 TextColor.contorno_preto("Texto Normal", TextColor.AZUL, TextColor.NEGRITO)
 TextColor.contorno_azul("Texto Normal", TextColor.CIANO, TextColor.NEGRITO)
 TextColor.contorno_verde("Texto Normal", TextColor.BRANCO, TextColor.NEGRITO)
 TextColor.contorno_amarelo("Texto Normal", TextColor.AZUL, TextColor.NEGRITO)
 TextColor.contorno_vermelho("Texto Normal", TextColor.BRANCO, TextColor.NEGRITO)
 TextColor.contorno_ciano("Texto Normal", TextColor.PRETO, TextColor.NEGRITO)
 TextColor.contorno_magenta("Texto Normal", TextColor.BRANCO, TextColor.NEGRITO)
 TextColor.contorno_branco("Texto Normal", TextColor.AZUL, TextColor.NEGRITO)
```
Variações: NEGRITO, LEVE, ITÁLICO, SUBLINHADO, NEGATIVO e RISCADO                                                              

Cores: AZUL, AMARELO, VERMELHO, VERDE, PRETO, CIANO, MAGENTA e BRANCO                                                          

## FUNÇÕES DE ESPECIFICAS:                                                                                                        
```
 TextColor.colorido("Texto Normal", TextColor.AZUL, TextColor.NEGRITO)                                         

 TextColor.contorno_colorido("Texto Normal", TextColor.VERMELHO, TextColor.SUBLINHADO, TextColor.FUNDO_AMARELO)

 TextColor.fonte("Texto Normal", TextColor.RISCADO)                                                             
```

Variações: NEGRITO, LEVE, ITÁLICO, SUBLINHADO, NEGATIVO e RISCADO                                                              

Cores: AZUL, AMARELO, VERMELHO, VERDE, PRETO, CIANO, MAGENTA e BRANCO                                                          

Contornos: FUNDO_PRETO, FUNDO_AZUL, FUNDO_VERDE, FUNDO_AMARELO, FUNDO_VERMELHO, FUNDO_CIANO, FUNDO_MAGENTA e FUNDO_BRANCO

## OUTRAS FUNÇÕES:
Para escrever diretamente no terminal basta adicionar ` escrever_ ` no ínicio da função
```
 TextColor.escrever_negrito_azul("Texto Normal")

```

Em breve versão com funções em inglês
