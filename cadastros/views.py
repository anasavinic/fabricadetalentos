from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from cadastros.form import AlunoForm
from cadastros.models import Aluno


class AlunoList(View):

    def get(self, request):

        qs = Aluno.objects.all().order_by('nome')

        context = {
            'aluno': qs,
            'titulo': 'Aluno'
        }

        return render(request, 'cadastros/lista_aluno.html', context)

    def post(self, request):
        pass


def aluno_detail(request, id):

    aluno = get_object_or_404(Aluno, pk=id)


    context = {
        'aluno': aluno,
    }

    return render(request, 'cadastros/detalhe_aluno.html', context)


def aluno_create(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('aluno-list')
    else:
        form = AlunoForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastros/cadastro_aluno.html', context)


def aluno_remove(request, id):

    aluno = get_object_or_404(Aluno, pk=id)

    aluno.delete()

    return redirect('aluno-list')


def aluno_edit(request, id):

    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForm(request.POST or None)

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluno-list')

    context = {
        'form': form,
        'obj': aluno
    }

    return render(request, 'cadastros/edita_aluno.html', context)
