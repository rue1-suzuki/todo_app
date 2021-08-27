from django.urls import path

from app.views import auth, todo, user

app_name = 'app'

urlpatterns = [
    path('user/add/', user.Create.as_view(), name='user_create'),
    path('user/', user.List.as_view(), name='user_list'),
    path('user/<int:pk>/', user.Detail.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', user.Update.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', user.Delete.as_view(), name='user_delete'),

    # Todo CRUD
    path('add/', todo.Create.as_view(), name='todo_create'),
    path('', todo.List.as_view(), name='todo_list'),
    path('<int:pk>/', todo.Detail.as_view(), name='todo_detail'),
    path('<int:pk>/update/', todo.Update.as_view(), name='todo_update'),
    path('<int:pk>/delete/', todo.Delete.as_view(), name='todo_delete'),

    # Todoのstatus切り替え
    path('switch/status/', todo.SwitchStatus.as_view(), name='todo_switch_status'),

    # ログイン・ログアウト
    path('login/', auth.MyLogin.as_view(), name='login'),
    path('logout/,', auth.MyLogout.as_view(), name='logout'),

    # パスワード変更
    path('pw/change/', auth.MyPasswordChange.as_view(), name='password_change'),
    path('pw/change/done/', auth.MyPasswordChangeDone.as_view(),
         name='password_change_done'),

    # パスワードリセット
    path('pw/reset/', auth.MyPasswordReset.as_view(), name='password_reset'),
    path('pw/reset/done/', auth.MyPasswordResetDone.as_view(),
         name='password_reset_done'),
    path('pw/reset/confirm/', auth.MyPasswordResetConfirm.as_view(),
         name='password_reset_confirm'),
    path('pw/reset/complete/', auth.MyPasswordResetComplete.as_view(),
         name='password_reset_complete'),

]
