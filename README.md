# Metal-Organic-Prediction
## Autores: Cauê Santos, Izaque Junior, Karla Pascoalini

Este é o read-me (PROVISÓRIO) do nosso trabalho de redes neurais e algorítimo genético!

Neste trabalho iremos trabalhar com o data set _Metal-Organic Frame Materials Prediction_ 

Nosso objetivo com esse trabalho é desenvolver uma rede neural que preveja grandezas físicas de temperatura (T) e tempo (t) de síntese de alguns materias específicos que são do nosso interesse estudar. Os nossos materiais de interesse são MOFs, ou Metal-Organic Frameworks. Os MOFs tem como principal característica serem compostos de íons metálicos (Ou aglomerados coordenados) que são ligados a ligantes orgânicos, formando estruturas que podem ser uni, bi ou tridimensionais! Uma observação é que MOFs são muito porosos, e similares a polímeros de coordenação.

Esse tipo de previsão de síntese de MOFs se constitui a partir de um projeto de rotas sintéticas (E condições sintéticas) de novos materiais que são MOF, isso aconteceria por meio da simulação de modelos computacionais preditivos.

Os inputs que utilizaremos são de um dataset chamado FingerPrint, cujo as features são: 1s - 5f [Configuração eletrônica]; metal [Tipo de metal do MOF]; linker1smi [Formula estrutural para o linker1, é uma expressão estrutural do MOF]; e oxidation_state [Estados de oxidação do metal nodal].

Os outputs desejados são: Temperatura [Temperatura de síntese de MOFs]; e Tempo [Tempo de síntese de MOFs].
