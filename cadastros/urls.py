from django.urls import include, path

from cadastros.views import AlunoList, aluno_create, aluno_detail, aluno_remove, aluno_edit

urlpatterns = [
    path('', AlunoList.as_view(), name='aluno-list'),
    path('create/', aluno_create, name='aluno-create'),
    path('detail/<int:id>/', aluno_detail, name='aluno-detail'),
    path('remove/<int:id>/', aluno_remove, name='aluno-remove'),
    path('edit/<int:id>/', aluno_edit, name='aluno-edit'),
]

