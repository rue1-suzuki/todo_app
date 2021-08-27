from app.mixins import OnlyMyTodoMixin
from app.models import Todo
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseForbidden
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic


class Create(LoginRequiredMixin, generic.CreateView):
    template_name = 'todo/create.html'
    model = Todo
    success_url = reverse_lazy('app:todo_list')
    fields = ['title', 'text', 'close_datetime', 'priority', ]

    def get_form(self):
        datetime_widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'value': timezone.now().strftime('%Y-%m-%dT00:00'),
            }
        )

        form = super().get_form()
        form.fields['close_datetime'].widget = datetime_widget
        form.fields['close_datetime'].input_formats = ['%Y-%m-%dT%H:%M']
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'todo/list.html'
    model = Todo

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user=self.request.user)
        query = query.order_by('close_datetime', '-priority')

        filter = self.request.GET.get(key='filter')
        if filter == 'today':
            dt = timezone.now()
            query = query.filter(
                close_datetime__year=dt.year,
                close_datetime__month=dt.month,
                close_datetime__day=dt.day,
            )

        title = self.request.GET.get(key='title')
        prriority = self.request.GET.get(key='priority')
        status = self.request.GET.get(key='status')
        if title:
            query = query.filter(title=title)
        if prriority:
            query = query.filter(priority=prriority)
        if status:
            query = query.filter(status=status)

        return query


class Detail(OnlyMyTodoMixin, generic.DetailView):
    template_name = 'todo/detail.html'
    model = Todo


class Update(OnlyMyTodoMixin, generic.UpdateView):
    template_name = 'todo/update.html'
    model = Todo
    success_url = reverse_lazy('app:todo_list')
    fields = ['title', 'text', 'close_datetime', 'priority', 'status', ]


class Delete(OnlyMyTodoMixin, generic.DeleteView):
    template_name = 'todo/delete.html'
    model = Todo
    success_url = reverse_lazy('app:todo_list')


class SwitchStatus(LoginRequiredMixin, generic.RedirectView):
    def post(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.request.POST['pk'])

        if not todo.user == self.request.user:
            return HttpResponseForbidden()

        todo.status += 1
        if 3 < todo.status:
            todo.status -= 3
        todo.save()

        return super().post(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        todo = Todo.objects.get(pk=self.request.POST['pk'])

        url = self.request.META['HTTP_REFERER']
        return f'{url}#todo{todo.pk}_{todo.title}'
