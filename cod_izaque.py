from sklearn.linear_model import LinearRegression

def converte(df_com_coluna, tipo_convert):
    """Esta funcao converte o tipo de dado presente em uma coluna de um dataframe.
    
    Argumentos:
        df_com_coluna: dataframe identificado com a coluna a ser convertida.
        tipo_convert: string contendo o formato para o qual deseja converter os dados da coluna.
    """
    df_com_coluna = df_com_coluna.astype(tipo_convert)
    
    return df_com_coluna

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
        
        