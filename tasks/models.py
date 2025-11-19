from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


PRIORITY_CHOICES = (
    ('URGENTE', 'URGENTE'),
    ('NÃO URGENTE', 'NÃO URGENTE'),
)

STATUS_CHOICES = (
    ('aberta', 'ABERTA'),
    ('em andamento', 'EM ANDAMENTO'),
    ('cancelado', 'CANCELADO'),
    ('concluido', 'CONCLUIDO'),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='task_category')
    priority = models.CharField(
        max_length=100,
        choices=PRIORITY_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='aberta'
    )
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)

    def get_status_choices(self):
        return STATUS_CHOICES
