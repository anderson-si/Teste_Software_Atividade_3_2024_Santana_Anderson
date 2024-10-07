## DISCIPLINA TESTE DE SOFTWARE
## **ANDERSON COSTA MOREIRA SANTANA**
### ATIVIDADE 3 - 2ª AVALIAÇÃO

## **TUTORIAL**

Para esta atividade foi selecionado o artigo "A Comparative Performance Analysis of Autogeneration Tools" disponível em https://arxiv.org/pdf/2312.10622, este por sua vez servirá de base para aplicar o conhecimento desenvolvido na disciplina Teste de Software.
Este artigo tem o objetivo de investigar experimentalmente a eficácia dos LLMs para a geração de scripts de casos de testes especificamente utilizando o Chat-GPT na versão 3.5 para programas escritos em Python e como os casos de testes se comportam com aqueles gerados por um gerador de testes unitários existentes o Pynguin. Pynguin:
O Pynguin é uma ferramenta de geração automática de testes para código Python e não utiliza diretamente uma arquitetura baseada em Transformers, como as arquiteturas "encoder-only", "decoder-only" ou "encoder-decoder". Ele se concentra em analisar o código-fonte e gerar testes baseados nisso, sem empregar modelos de aprendizado profundo como Transformers.
O ChatGPT utiliza uma arquitetura decoder-only. Ele é baseado no modelo GPT (Generative Pre-trained Transformer), que usa apenas a parte decoder de um Transformer. Nessa arquitetura, o foco está em gerar texto de forma autoregressiva, onde o modelo prevê a próxima palavra ou token com base nos tokens anteriores, sem a necessidade de um encoder para processar a entrada.
Segundo o autor para os experimentos foram utilizados 3 três tipos de códigos, 1º Scripts procedurais, 2º Código modular baseado em função e 3º Código baseado em classe. Os casos de teste gerados são avaliados com base em critérios como cobertura, correção e legibilidade, em resumo este artigo busca explorar as vantagens e desvantagens de suítes de testes produzidas por Large Language Models com foco no ChatGPT e as gerados pelo Pynguin representante dos SBST (Search-Based Software Testing) em que utilizam algoritmos de otimização e técnicas de busca para gerar testes automaticamente. 
O conjunto de dados utilizado foram 60 projetos buscados em repositórios aleatórios em Python compreendendo 20 por categoria, depois foram adicionados 49 projetos Python dos dados de benchmark usados por Lukasczyk et al. [21]. No total, foram utilizados 109 projetos Python. Mas baseando-se em alguns critérios como número de linhas de código, baixa complexidade e único módulo. 
O estudo foi focado em um modulo principal de cada projeto variando entre 100 e 300 linhas de códigos cujo objetivo é abordar as seguintes questões RQ1 Desempenho Comparativo, RQ2 Saturação de Desempenho e Melhoria Iterativa, RQ3 Avaliação de Qualidade e RQ4 Combinação de Ferramentas para desempenho Aprimorado. 
O autor descreve sua metodologia informando que o designer do prompt para o GPT foram compostos por 2 componentes, Primeiro o programa Python, segundo o texto descritivo em linguagem natural descrevendo a tarefa que pretendia realizar.


<p align="center">
  <img src="img\01.png" alt="Texto Alternativo">
</p>

O autor não descreve como foi descrito o designer do prompt para geração dos casos de teste com Pynguin. Mas, apresenta uma imagem demostrando o fluxo de seus experimentos.

<p align="center">
  <img src="img\02.png" alt="Texto Alternativo">
</p>

Prosseguindo a atividade solicitada pelo professor, busquei seguir a ideia do artigo escolhido, mas precisei diminuir o escopo em relação ao que foi feito pelo autor do artigo, pois, reunir diversos projeto, pesquisar e colher métricas de um a um, demanda bastante tempo. 
Em minha atividade será utilizado apenas um único repositório, disponível em https://github.com/M4DM4N56/small-python-projects/blob/main/TTT_old.py, busquei por um repositório que contivesse um programa com as características descrita no artigo. Além, disso utilizaremos apenas o modulo TTT.py em que se trata de um jogo com aproximadamente 300 linhas de código chamado “Jogo da Velha” em que pode ser jogado por 1 ou 2 jogadores.
Inicialmente instalei todas as ferramentas necessária em um ambiente virtual venv para proceder com os experimentos inclusive o gerador de casos de teste pynguin.

<p align="center">
  <img src="img\03.png" alt="Texto Alternativo">
</p>

Após configurando o ambiente de experimento, no terminal rodei o seguinte comando: 

```
pynguin --project-path . --module-name TTT --output-path .
```

Esse comando gerou um arquivo chamado test_pynguin_TTT.py contendo todos os casos testes.

<p align="center">
  <img src="img\04.png" alt="Texto Alternativo">
</p>

Em seguida gerei o prompt para o ChatGPT da seguindo forma. 

<p align="center">
  <img src="img\05.png" alt="Texto Alternativo">
</p>

Após passado o programa para o Chat-GPT gerar os casos de testes ele me retornou além do código sugestão de melhorias no programa principal e o passo a passo para instalação e execução das ferramentas usadas nos casos de testes diferentemente do Pynguin que apenas gera o código. 

<p align="center">
  <img src="img\06.png" alt="Texto Alternativo">
</p>

No vscode prosseguir para execução dos casos de teste usando o Pytest e o Pytest-cov para verificar a percentagem de cobertura de ambos os testes gerados visualmente é possível notar que o Chat-GPT gerou algumas linhas de códigos a mais em relação ao Pynguin, então rodei o seguinte comando.

```
pytest -vv test_pynguin_TTT.py
```

Obtendo o seguinte resultado: 

<p align="center">
  <img src="img\07.png" alt="Texto Alternativo">
</p>

O pynguin gerou 6 casos de testes, sendo que dos 6 apenas 1 falou. Para avaliar a cobertura do caso dos casos de testes gerados pelo Pynguin rodeio o seguinte comando. 

```
pytest -vv test_pynguin_TTT.py --cov=TTT
```
<p align="center">
  <img src="img\08.png" alt="Texto Alternativo">
</p>

Pela imagem que vemos acima o código gerado pelo Pynguin consegue ter uma cobertura de 28% do Código. 

Passemos agora aos testes com o código gerado com o Chat-GPT.

<p align="center">
  <img src="img\09.png" alt="Texto Alternativo">
</p>

Dos testes gerados pelo Chat-GPT 10 passaram e 7 Falharam. Como meu interesse e estudar o desempenho das ferramentas geradores de casos testes não corrigirei o código fonte do programa para os casos de testes que falharam, passemos agora a investigar a percentagem de cobertura dos casos de testes gerado pelo Chat-GPT.

```
pytest -vv test_chatgpt_TTT.py --cov=TTT
```

<p align="center">
  <img src="img\10.png" alt="Texto Alternativo">
</p>

Após, gerei um novo prompt para Chat-GPT para que melhorasse a cobertura.

<p align="center">
  <img src="img\11.png" alt="Texto Alternativo">
</p>

A quantidade de casos de testes aumentou para 60 caso de testes dos quais 43 falharam e 17 passaram.

<p align="center">
  <img src="img\12.png" alt="Texto Alternativo">
</p>

Após executado o comando para verificar a percentagem de cobertura tivemos um aumento significativo em relação aos casos de testes gerados anteriormente. 

<p align="center">
  <img src="img\13.png" alt="Texto Alternativo">
</p>

Após isso, solicitei ao Chat-GPT que melhorasse a cobertura de testes produzidas pelo Pynguin, então, ele aumento para 44 o número de casos de testes sendo que desse 11 falharam e 33 passaram. 

<p align="center">
  <img src="img\14.png" alt="Texto Alternativo">
</p>

Passemos a investigar qual a percentagem de cobertura gerada do código gerado pelo Pynguin e ajustado pelo Chat-GPT.

<p align="center">
  <img src="img\15.png" alt="Texto Alternativo">
</p>

Abaixo segue tabela demostrando todos os resultados obtidos: 


| FERRAMENTA / IA | CASO DE TESTE 1º INTERAÇÃO | CASO DE TESTE 2º INTERAÇÃO	| COBERTURA EM % 1º INTERAÇÃO |	COBERTURA EM % 2º INTERAÇÃO |
|-----------------|----------------------------|----------------------------|-----------------------------|-----------------------------|
| Pynguin	      |            06	           |             X	            |              28 %	          |               X             |
| Chat-GPT	      |            17	           |             60	            |              36 %	          |               87 %          |
| Pynguin combinada com Chat-GPT | 	 X	       |             44	            |               X	          |               91 %          |


O estudo descrito no artigo poderia ser utilizado para resolução de vários desafios enfrentados por programadores um deles é o descrito no site StackOverflow com o título “How to Unit Test a Nested Function Using PyTest Without Modifying the Outer Function” disponível no link https://stackoverflow.com/questions/78836464/how-to-unit-test-a-nested-function-using-pytest-without-modifying-the-outer-func, pois, a autor da pergunta deseja gerar caso de testes com algumas características especificas assim o seria muito mais fácil fazendo uso de ferramentas como o Pyguin ou o Chat-GPT.  
Assim, é possível concluir que em nossos experimentos o Chat-GPT conseguiu melhor desempenho a partir da segunda interação, com o Pynguin não foi possível realizar um aprimoramento dos casos de testes, mas combinados a Ferramenta Pynguin e a IA Chat-GPT foi possível observar que a percentagem de cobertura de código superou a utilização apenas do Chat-GPT.
