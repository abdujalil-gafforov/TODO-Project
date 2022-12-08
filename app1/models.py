from django.contrib.auth.models import User
from django.db.models import CharField, TextField, Model, ForeignKey, CASCADE, BooleanField, DateTimeField


class Task(Model):
    user = ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    complete = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

