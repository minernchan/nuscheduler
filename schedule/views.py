from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from schedule.forms import ScheduleForm
from schedule.models import SchedulePost
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            schedule_post.course_name = form.cleaned_data['course_name']
            schedule_post.modules_taken = form.cleaned_data['modules_taken']
            schedule_post.desc = form.cleaned_data['desc']
            schedule_post.user = request.user
            schedule_post.save()
            form = ScheduleForm()
            return redirect('schedule')
        args = {'form': form}
        return render(request, self.template_name, args)

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

def filter_schedule_faculty(request, faculty_name):
    schedule_posts = SchedulePost.objects.filter(faculty=faculty_name).order_by('-created')
    return render(request, 'schedule/schedule.html', {'schedule_posts':schedule_posts})


