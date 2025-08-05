import json
from django.shortcuts import render
from core.models import Vaga, Candidato
import pandas as pd

def dashboard(request):
    vagas = Vaga.objects.all()
    candidatos = Candidato.objects.all()

    abertas = vagas.filter(status='aberta').count()
    fechadas = vagas.filter(status='fechada').count()

    dados_vagas = []
    for vaga in vagas:
        dados_vagas.append({
            'vaga': vaga.titulo,
            'candidatos': vaga.candidatos.count()
        })
    df_vagas = pd.DataFrame(dados_vagas)

    idades = [c.idade() for c in candidatos]
    media_idade = round(sum(idades)/len(idades), 1) if idades else 0

    setor_df = pd.DataFrame(vagas.filter(status='aberta').values('setor'))
    setor_mais_vagas = setor_df['setor'].value_counts().idxmax() if not setor_df.empty else 'Nenhum'

    contexto = {
        'abertas': abertas,
        'fechadas': fechadas,
        'media_idade': media_idade,
        'setor_mais_vagas': setor_mais_vagas,
        'tabela': df_vagas.to_html(index=False)
    }
    return render(request, 'core/dashboard.html', contexto)
