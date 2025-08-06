import json
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vaga, Candidato
from .forms import VagaForm

def dashboard(request):
    vagas      = Vaga.objects.all()
    candidatos = Candidato.objects.all()

    abertas = vagas.filter(status='aberta').count()
    fechadas = vagas.filter(status='fechada').count()

    dados_vagas = [
        {'vaga': v.titulo, 'candidatos': v.candidatos.count()}
        for v in vagas
    ]
    labels = [d['vaga'] for d in dados_vagas]
    values = [d['candidatos'] for d in dados_vagas]

    idades = [c.idade() for c in candidatos]
    media_idade = round(sum(idades) / len(idades), 1) if idades else 0

    setor_df = pd.DataFrame(vagas.filter(status='aberta').values('setor'))
    setor_mais = (
        setor_df['setor'].value_counts().idxmax()
        if not setor_df.empty else 'Nenhum'
    )

    contexto = {
        'abertas': abertas,
        'fechadas': fechadas,
        'media_idade': media_idade,
        'setor_mais_vagas': setor_mais,
        'dados_vagas': dados_vagas,
        'chart_labels_json': json.dumps(labels),
        'chart_values_json': json.dumps(values),
    }
    return render(request, 'core/dashboard.html', contexto)

def vaga_list(request):
    vagas = Vaga.objects.all()
    return render(request, 'core/vaga_list.html', {'vagas': vagas})

def vaga_create(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaga_list')
    else:
        form = VagaForm()
    return render(request, 'core/vaga_form.html', {
        'form': form,
        'titulo': 'Nova Vaga'
    })

def vaga_edit(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            return redirect('vaga_list')
    else:
        form = VagaForm(instance=vaga)
    return render(request, 'core/vaga_form.html', {
        'form': form,
        'titulo': 'Editar Vaga'
    })
