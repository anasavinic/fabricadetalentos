from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from cadastros.form import AlunoForm
from cadastros.models import Aluno


def listar_cidades(request):
    qs= Aluno.objects.all()

    pass