from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(TemplateView, DetailView,
                                ListView, FormView, CreateView, 
                                UpdateView, DeleteView)
from .models import Lesson, Standard, Subject, save_lesson_files
from .forms import LessonForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/class_list.html'

class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/class_subjects.html'


class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/course_list.html'


class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/course_details.html'



class LessonCreateView(CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug, 'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ('name', 'position', 'video', 'ppt', 'Notes', 'comment')
    model = Lesson
    template_name = 'curriculum/lesson_update_view.html'
    context_object_name = 'lessons'
    
    #function to check if user is the login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


class LessonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'curriculum/lesson_delete.html'

    def get_success_url(self):
        standard = self.object.standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_list', kwargs={'standard':standard.slug, 'slug':subject.slug})

#preventing other users from update other people's post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


