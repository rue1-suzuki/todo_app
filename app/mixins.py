from django.contrib.auth.mixins import UserPassesTestMixin

from app.models import Todo


class OnlyMyTodoMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        todo = Todo.objects.get(pk=self.kwargs['pk'])
        return self.request.user == todo.user
