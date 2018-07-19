from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404

from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from schedule.filters import SchedulePostFilter
from schedule.forms import ScheduleForm
from schedule.models import SchedulePost
from comments.forms import CommentForm
from comments.models import Comment

class ScheduleView(TemplateView):
    template_name = 'schedule/schedule.html'

    def get(self,request): #Requires HttpResponse 
        schedule_posts = SchedulePost.objects.all().order_by('-created')
        
        args = {'schedule_posts': schedule_posts,}
        return render(request, self.template_name, args)

class ScheduleFormView(TemplateView):
    template_name = 'schedule/schedule_submit.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            form = ScheduleForm()
        else:
            messages.error(request, "You are not logged in!")
            return redirect('schedule')
        args = {'form':form,}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            schedule_post = form.save(commit=False)
            schedule_post.title = form.cleaned_data['title']
            schedule_post.image = form.cleaned_data['image']
            schedule_post.faculty = form.cleaned_data['faculty']
            schedule_post.year = form.cleaned_data['year']
            schedule_post.semester = form.cleaned_data['semester']
            schedule_post.course_name = form.cleaned_data['course_name']
            schedule_post.modules_taken = form.cleaned_data['modules_taken']
            schedule_post.desc = form.cleaned_data['desc']
            schedule_post.user = request.user
            schedule_post.save()
            form = ScheduleForm()
            return redirect('schedule')
        args = {'form': form}
        return render(request, self.template_name, args)

def schedule_detail(request,pk):
    template = 'schedule/schedule_post.html'
    schedule_post = get_object_or_404(SchedulePost, pk=pk)
    
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        content_data = comment_form.cleaned_data['content']
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None
        
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
                    user=request.user,
                    schedule_post=schedule_post,
                    content=content_data,
                    parent = parent_obj,
                )
        
        
        return redirect('view_schedule', pk)

    comments = Comment.objects.filter(schedule_post=schedule_post).filter(parent=None)

    args = {
        'schedulepost': schedule_post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, template, args)

@login_required
def edit_schedule_post(request, pk):
    template = 'schedule/schedule_submit.html'
    schedule_post = get_object_or_404(SchedulePost, pk=pk) # getting the object
    if schedule_post.user == request.user:
        if request.method == 'POST':
            form = ScheduleForm(request.POST, request.FILES, instance=schedule_post)
            if schedule_post.user == request.user:
                if form.is_valid():
                    schedule_post = form.save(commit=False)
                    schedule_post.title = form.cleaned_data['title']
                    schedule_post.image = form.cleaned_data['image']
                    schedule_post.faculty = form.cleaned_data['faculty']
                    schedule_post.course_name = form.cleaned_data['course_name']
                    schedule_post.modules_taken = form.cleaned_data['modules_taken']
                    schedule_post.desc = form.cleaned_data['desc']
                    schedule_post.user = request.user
                    schedule_post.save()
                    messages.success(request, "Post Saved!")
                    form = ScheduleForm()
                    return redirect('view_schedule', pk)
        else:
            form = ScheduleForm(instance=schedule_post)
    else:
        raise messages.error(request, "You are not authorized to do that!")
        return redirect('view_schedule', pk)
    
    args = {'form': form, 'schedule_post':schedule_post}
    return render(request, template, args)

@login_required
def delete_schedule_post(request, pk):
    schedule_post = get_object_or_404(SchedulePost, pk=pk)
    if schedule_post.user == request.user:
        schedule_post.delete()
        messages.success(request, "Post Successfully Deleted!")
        return redirect('schedule')
    else:
        messages.error(request, "You are not authorized to do that!")
        return redirect('view_schedule', pk)



def schedule_search(request):
    schedule_list = SchedulePost.objects.all().order_by('-created')
    schedule_filter = SchedulePostFilter(request.GET, queryset=schedule_list)
    return render(request, 'schedule/schedule_search.html', {'filter':schedule_filter })
