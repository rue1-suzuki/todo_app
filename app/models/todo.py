from app.models import User
from django.db import models
from django.db.models.deletion import CASCADE


class Todo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name='作成ユーザ',
    )

    title = models.CharField(
        max_length=128,
        verbose_name='タイトル',
    )

    text = models.TextField(
        max_length=1024,
        blank=True,
        null=True,
        verbose_name='内容',
    )

    close_datetime = models.DateTimeField(
        verbose_name='期限',
    )

    status = models.IntegerField(
        choices=(
            (1, '未着手'),
            (2, '実施中'),
            (3, '完了'),
        ),
        default=1,
        verbose_name='状態',
    )

    priority = models.IntegerField(
        choices=(
            (1, '低'),
            (2, '中'),
            (3, '高'),
        ),
        default=1,
        verbose_name='優先度',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新日時',
    )
