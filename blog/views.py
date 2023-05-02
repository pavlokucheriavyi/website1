from django.shortcuts import render, get_object_or_404
from .models import News
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class NewsView(ListView):
    model = News
    template_name = "blog/home.html"
    context_object_name = 'news'
    ordering = ["-date"]
    paginate_by = 4

    def get_context_data(self, **kwards):
        ctx = super(NewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница сайта'
        return ctx


class UserAllView(ListView):
    model = News
    template_name = "blog/user_news.html"
    context_object_name = 'news'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return News.objects.filter(avtor=user).order_by("-date")

    def get_context_data(self, **kwards):
        ctx = super(UserAllView, self).get_context_data(**kwards)

        ctx['title'] = f'Статьи от {self.kwargs.get("username")}' #логин вытягивает
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    context_object_name = 'i'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/update.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/' #после удаления будет переходить на главную страницу
    template_name = 'blog/delete.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False


def contacti(request):
    data = {
        "title" : "Eto kontakti"
    }
    return render(request, "blog/contacti.html", data)
