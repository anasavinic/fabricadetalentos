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


class AlunoDetail(View):

    def aluno_detail(request, id):
        aluno = get_object_or_404(Aluno, pk=id)

        context = {
            'aluno': aluno,
        }

        return render(request, 'cadastros/detalhe_aluno.html', context)


class AlunoCreate(View):

    def aluno_create(request):

        if request.method == 'POST':

            form = AlunoForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('aluno-list')

        else:
            form = AlunoForm()

        context = {
            'form': form
        }

        return render(request, 'cadastros/cadastro_aluno.html', context)


class AlunoRemove(View):

    def aluno_remove(request, id):
        aluno = get_object_or_404(Aluno, pk=id)

        aluno.delete()
        messages.success('Registro removido com sucesso!')

        return redirect('aluno-list')


class AlunoEdit(View):

    def aluno_edit(request, id):

        aluno_obj = get_object_or_404(Aluno, pk=id)
        form = AlunoForm(request.POST or None, instance=aluno_obj)

        if request.method == 'POST':
            form = AlunoForm(request.POST, instance=aluno_obj)
            if form.is_valid():
                form.save()
                return redirect('aluno-list')

        context = {
            'form': form,
            'obj': aluno_obj
        }

        return render(request, 'cadastros/edita_aluno.html', context)
