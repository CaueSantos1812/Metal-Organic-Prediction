# Metal-Organic-Prediction
## Autores: Cauê Santos, Izaque Junior, Karla Pascoalini

## Introdução:

Este é o read-me do nosso trabalho de redes neurais e algorítimo genético!

Neste trabalho iremos trabalhar com o data set _Metal-Organic Frame Materials Prediction_ 

Nosso objetivo com esse trabalho é desenvolver uma rede neural que preveja propriedades como temperatura (T) e tempo (t) de síntese de alguns materias específicos que são do nosso interesse estudar. Os nossos materiais de interesse são MOFs, ou Metal-Organic Frameworks. Os MOFs tem como principal característica serem compostos de íons metálicos (Ou aglomerados coordenados) que são ligados a ligantes orgânicos, formando estruturas que podem ser uni, bi ou tridimensionais! Uma observação é que MOFs são muito porosos, e similares a polímeros de coordenação.

Esse tipo de previsão de síntese de MOFs se constitui a partir de um projeto de rotas sintéticas (E condições sintéticas) de novos materiais que são MOF, isso aconteceria por meio da simulação de modelos computacionais preditivos.

Os inputs que utilizaremos são de um dataset chamado FingerPrint, cujo as features são: 1s - 5f [Configuração eletrônica]; metal [Tipo de metal do MOF]; linker1smi [Formula estrutural para o linker1, é uma expressão estrutural do MOF]; e oxidation_state [Estados de oxidação do metal nodal].

Os outputs desejados são: Temperatura [Temperatura de síntese de MOFs]; e Tempo [Tempo de síntese de MOFs].

## Motivação

##  Estrutura do Repositório
A estrutura desse repositório é em partes complexa, visto que o dataset utilizado, que até então seria de configuração eletrônica foi ampliado com outros atributos e, no próprio kaggle do dataset original, os df de treino e teste já estavam separados. 

## Requisitos para rodar o código

- **pandas:** Biblioteca para tratamento e anBálise de dados
- **optuna:** Biblioteca usada para otimização de hiperparâmetros
- **numpy:** Biblioteca usada para criar arrays
- **cod_izaque:** Import de funções para tratamento de dados
- **rdkit:** Biblioteca usada para retirar informações e propriedades dos MOFs
- **sklearn:** Biblioteca usada para tratamento de dados, como split de dados e normalização
- **torch:** Biblioteca utilizada para criação do modelo de NN
- **matplotlib:** Biblioteca usada para plotar gráficos
- **lightning:** Biblioteca usada para treinamentos de modelos flexíveis do Pytorch 
- **pickle:** 

## Conclusão



## Referências
[1] MOLSimplify Documentation. Available at: https://molsimplify.readthedocs.io/en/latest/Informatics.html. Accessed on: 20 May 2024. <br>
[2] KAGGLE. Rac predicts time using RF. Available at: https://www.kaggle.com/code/marquis03/rac-predicts-time-using-rf. Accessed on: 19 May 2024. <br>
[3]OYERINDE, Akinyemi B.; RICHARDS, Graham J. Supramolecular chemistry in two-dimensional organic materials: the role of intermolecular interactions. Coordination Chemistry Reviews, v. 474, p. 214781, 2023. Available at: https://www.sciencedirect.com/science/article/pii/S0010854523001017#b0095. Accessed on: 20 May 2024. <br>
[4] CLAY, Rachael; ANDERSON, Perry A.; KELLY, Scott. Thermodynamic properties of ionic liquids: A critical review. Journal of Chemical & Engineering Data, v. 64, n. 12, p. 5211-5231, 2019. Available at: https://pubs.acs.org/doi/epdf/10.1021/acs.jced.9b00835. Accessed on: 20 May 2024. <br>
[5] Computation-Ready, Experimental Metal–Organic Framework (CORE-MOF) 2.0. Northwestern Scholars. Available at: https://www.scholars.northwestern.edu/en/datasets/computation-ready-experimental-metal-organic-framework-core-mof-2. Accessed on: 25 May 2024. <br>
[6] LI, Hui; XU, Bo; ZHOU, Wei. Rational design of metal–organic frameworks for heterogeneous catalysis. Angewandte Chemie International Edition, v. 61, n. 15, p. e202200242, 2022. Available at: https://onlinelibrary.wiley.com/doi/epdf/10.1002/anie.202200242. Accessed on: 19 May 2024. <br>
[7] ZHANG, Q.; YANG, X.; CHEN, Y. Exploring the electronic structures of covalent organic frameworks. Chemical Science, v. 11, p. 10579-10586, 2020. Available at: https://www.rsc.org/suppdata/d0/sc/d0sc05337f/d0sc05337f1.pdf. Accessed on: 20 May 2024. <br>
[8] OPTUNA Documentation. Available at: https://optuna.readthedocs.io/en/stable/. Accessed on: 27 May 2024. <br>
[9] OPTUNA GitHub Repository. Available at: https://github.com/optuna/optuna. Accessed on: 27 May 2024. <br>
[10] Cassar, Daniel Roberto. Notebook 2.1: Tipos de Dados. <br>
[11] Cassar, Daniel Roberto. Notebook 5.3: PyThorch Lightning. <br>
[12] Cassar, Daniel Roberto. Notebook 8: Seleção de Atributos e redução de dimensionalidade. <br>
[13] KAGGLE. Rac predicts temperature using LSTM. Available at: https://www.kaggle.com/code/marquis03/rac-predicts-temperature-using-lstm. Accessed on: 19 May 2024. <br>
