from rdkit import Chem
from rdkit.Chem import AllChem as al
from rdkit.Chem import Draw, AllChem, Descriptors
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

def enc_intersection(dados1, dados2):
    """Encontra a intersecção entre dois conjuntos.
        Argumentos:
            dados1: conjunto de dados do tipo set
            dados2: conjunto de dados do tipo set
        returns:
            retorna a interceção entre os dois conjuntos.
    """
    a = set(list(dados1))
    b = set(list(dados2))
    
    c = a.intersection(b)
    
    return c

def converte_datatype(df, lista_com_colunas_covrt, type_converte):
    """Esta funcao converte o tipo do dado presente em uma coluna de um dataframe.
    
    Argumentos:
        df: dataframe que contém as colunas a serem modificadas
        lista_com_colunas_covrt: lista contendo o nome das colunas a serem convertidas
        type_convert: string contendo o formato para o qual deseja converter os dados da coluna.
    """
    for coluna in lista_com_colunas_covrt:
        df[coluna] = df[coluna].astype(type_converte)

def stri_to_mol(df, with_linker1smi=False):
    """Esta função converte do tipo string para objetos do tipo mol da biblioteca rdkit.
    
    Argumentos:
        df: dataframe com os dados
        with_linker1smi: argumento que realiza a adição de colunas fingerprint no df. Padrão: False.
    
    Returns:
        retorna o dataframe com as transformações solicitadas.
    """
    if with_linker1smi==False:
        #print('Estou no if false')
        molecula = df['linker1smi'].apply(Chem.MolFromSmiles)
        df = df.drop('linker1smi', axis=1)
        df = df.drop('metal', axis=1)
        
        parametros_novos(df, molecula)
        
    if with_linker1smi==True:
        
        molecula = df['linker1smi'].apply(Chem.MolFromSmiles)
        df =df.drop('metal', axis=1)
        fingerprint = lambda x: al.GetMorganFingerprintAsBitVect(x, 3)
        #baseado no código do Marquis03
        fingerprint1 = np.array(molecula.apply(fingerprint).tolist())             
        fingerprint1 = pd.DataFrame(fingerprint1).add_prefix("fp1_")
        fingerprint1.index = df.index
        df =df.drop('linker1smi', axis=1)
        df = pd.concat([df, fingerprint1], axis=1)
        #Fim
        parametros_novos(df, molecula)
    
    return df
    
def parametros_novos(df, molecula):
    """Esta função adiciona ao dataframe características presentes na formula molecular da coluna linker1smi.
       Argumentos:
           df: dataframe no qual serão adicionadas as novas colunas.
           molecula: objeto convertido do tipo mol para leitura da biblioteca rdkit.
    """
    df['Peso Molecula'] = molecula.apply(Descriptors.ExactMolWt)
    df['TPSA'] = molecula.apply(Chem.rdMolDescriptors.CalcTPSA) #Total Superficial Polar Area
    df['HBA'] = molecula.apply(Chem.rdMolDescriptors.CalcNumHBA) #Hidrogen bond acceptors
    df['HBD'] = molecula.apply(Chem.rdMolDescriptors.CalcNumHBD) #Hidrogen bond donnors
    df['LogP'] = molecula.apply(Descriptors.MolLogP) #calculus the hidrophobicity
    df['RotnBond'] = molecula.apply(Chem.rdMolDescriptors.CalcNumRotatableBonds) #calculus the number of rotation bonds
#Créditos: Daniel Roberto Cassar
def selecao_vif(df_atributos, limiar_vif):
    """Realiza a seleção de atributos por VIF.

    Args:
      df_atributos: DataFrame contendo os atributos.
      limiar_vf: valor do limiar do vif. Número positivo. Usualmente é 5 ou 10.

    Returns:
      DataFrame com os atributos selecionados.
    """

    df = df_atributos.copy()

    while True:
        VIFs = []

        for col in df.columns:
            X = df.drop(col, axis=1).values
            y = df[col].values

            r_quadrado = LinearRegression().fit(X, y).score(X, y)

            if r_quadrado != 1:
                VIF = 1 / (1 - r_quadrado)
            else:
                VIF = float("inf")

            VIFs.append(VIF)

        VIF_maximo = max(VIFs)

        if VIF_maximo > limiar_vif:
            indice = VIFs.index(VIF_maximo)
            coluna_remocao = df.columns[indice]
            df = df.drop(coluna_remocao, axis=1)
        else:
            break

    return df