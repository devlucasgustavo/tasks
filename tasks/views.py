from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class TasksListView(ListView):
    model = models.Task
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(title__icontains=name)

        return models.Task.objects.filter(is_completed__in=['aberta', 'em andamento'])


class TasksCreateView(CreateView):
    model = models.Task
    template_name = 'task_create.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')


class TasksDetailView(DetailView):
    model = models.Task
    template_name = 'task_detail.html'


class TasksUpdateView(UpdateView):
    model = models.Task
    template_name = 'task_update.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('task_list')


class TasksDeleteView(DeleteView):
    model = models.Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')


class CategoryCreateView(CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('task_list')


def update_status(request, pk):
    task = get_object_or_404(models.Task, id=pk)

    if request.method == 'POST':
        new_status = request.POST.get('is_completed')

        if new_status in ['aberta', 'em andamento', 'concluido', 'cancelado']:
            task.is_completed = new_status
            task.save()

            if new_status in ['concluido', 'cancelado']:
                return redirect('historic_list')

        return redirect('task_list')


class HistoricListView(ListView):
    model = models.Task
    template_name = 'historic_list.html'
    context_object_name = 'historic'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_completed__in=['concluido', 'cancelado'])

        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(title__icontains=name)

        return queryset
