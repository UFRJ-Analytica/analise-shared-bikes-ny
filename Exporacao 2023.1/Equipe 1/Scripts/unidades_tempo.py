#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def separa_ut(df):
    df['dia_inicio'] = df['inicio_viagem'].dt.day
    df['mes_inicio'] = df['inicio_viagem'].dt.month
    df['ano_inicio'] = df['inicio_viagem'].dt.year
    df['dia_fim'] = df['fim_viagem'].dt.day
    df['mes_fim'] = df['fim_viagem'].dt.month
    df['ano_fim'] = df['fim_viagem'].dt.year
    df['hora_inicio'] = df['inicio_viagem'].dt.hour
    df['minuto_inicio'] = df['inicio_viagem'].dt.minute
    df['segundo_inicio'] = df['inicio_viagem'].dt.second
    df['hora_fim'] = df['fim_viagem'].dt.hour
    df['minuto_fim'] = df['fim_viagem'].dt.minute
    df['segundo_fim'] = df['fim_viagem'].dt.second
    df['idade'] = df['ano_inicio'] - df['ano_nascimento']

    return df
