from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from .models import  Projects,Profile
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


class PostListView(ListView):
    model = Projects
    template_name = 'index.html'
    context_object_name = 'projects'
    ordering = ['-created_date']

class PostDetailView(DetailView):
    model = Projects
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    success_url = '/'
    fields =['author','image','description', 'title' ,'link']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView):
    model = Projects
    success_url = '/'
    fields =['author','image','description', 'title' ,'link']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author_profile:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Projects
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author_profile:
            return True
        return False
   

@login_required
def Projectsproject(request):
    current_user = request.user
    if request.method == 'Projects':
        form = ProjectForm(request.Projects, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('/')
    else:
        form = ProjectForm()
    context = {
        'form':form,
    }
    return render(request, 'create-project.html', context)

def get_project(request, id):
    project = Projects.objects.get(pk=id)

    return render(request, 'project.html', {'project':project})

class ProjectsDetailView(DetailView):
    model = Projects

class ProjectsCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    fields =['author','image','description', 'title' ,'link']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)


class ProjectsUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView):
    model = Projects
    fields =['author','image','description', 'title' ,'link']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)

    def test_func(self):
        Projects = self.get_object()
        if self.request.user.profile == Projects.profile:
            return True
        return False
    
class ReviewCreateView(LoginRequiredMixin,CreateView):
    model = Review
    fields = ['design', 'usability', 'creativity', 'content']

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Project` instance exists
        before going any further.
        """
        self.project = get_object_or_404(Projects, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = self.project
        return super().form_valid(form)