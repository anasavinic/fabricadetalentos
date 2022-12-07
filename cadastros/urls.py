from django.urls import include, path

from cadastros.views import AlunoList, AlunoDetail, AlunoCreate, AlunoRemove, AlunoEdit

urlpatterns = [
    path('', AlunoList.as_view(), name='aluno-list'),
    path('create/', AlunoCreate.as_view(), name='aluno-create'),
    path('detail/<int:id>/', AlunoDetail.as_view(), name='aluno-detail'),
    path('remove/<int:id>/', AlunoRemove.as_view(), name='aluno-remove'),
    path('edit/<int:id>/', AlunoEdit.as_view(), name='aluno-edit'),
]

