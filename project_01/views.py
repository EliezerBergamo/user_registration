from django.http import Http404, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from project_01.forms import UserForm
from project_01.models import User


class HomeView(TemplateView):
    template_name = 'project_01/index.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'project_01/user/new.html'
    form_class = UserForm
    success_url = reverse_lazy('project_01:home')


class UserListView(ListView):
    model = User
    template_name = 'project_01/user/list.html'
    context_object_name = 'users'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'project_01/user/update.html'
    form_class = UserForm
    success_url = reverse_lazy('project_01:list_user')


def user_search_by_id(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            user = None

        return render(
            request,
            template_name='project_01/user/detail.html',
            context={'user': user}
        )


def user_delete_by_id(request: HttpRequest, pk: int):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        user = None

    if user is None:
        return render(
            request,
            template_name='project_01/user/delete.html',
            context={'user': user, 'not_found': True}
        )

    if request.method == 'POST':
        user.delete()
        return redirect('project_01:list_user')

    return render(
        request,
        template_name='project_01/user/delete.html',
        context={'user': user, 'not_found': False}
    )
