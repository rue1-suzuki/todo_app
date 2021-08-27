from django.contrib.auth import views
from django.urls import reverse_lazy


class MyLogin(views.LoginView):
    redirect_authenticated_user = True


class MyLogout(views.LogoutView):
    pass


class MyPasswordReset(views.PasswordResetView):
    success_url = reverse_lazy('app:password_reset_done')


class MyPasswordResetDone(views.PasswordResetDoneView):
    pass


class MyPasswordResetConfirm(views.PasswordResetConfirmView):
    success_url = reverse_lazy('app:password_reset_complete')


class MyPasswordResetComplete(views.PasswordResetCompleteView):
    pass


class MyPasswordChange(views.PasswordChangeView):
    success_url = reverse_lazy('app:password_change_done')


class MyPasswordChangeDone(views.PasswordChangeDoneView):
    pass
