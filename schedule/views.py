from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from schedule.forms import ScheduleForm
from schedule.models import SchedulePost

class ScheduleView(TemplateView):
    template_name = 'schedule/schedule.html'

    def get(self,request): #Requires HttpResponse 
        schedule_posts = SchedulePost.objects.all().order_by('-created')
        
        args = {'schedule_posts': schedule_posts,}
        return render(request, self.template_name, args)



class ScheduleFormView(TemplateView):
    template_name = 'schedule/schedule_submit.html'

    def get(self, request):
        form = ScheduleForm()
        
        args = {'form':form,}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            schedule_post = form.save(commit=False)
            schedule_post.title = form.cleaned_data['title']
            schedule_post.image = form.cleaned_data['image']
            schedule_post.course_name = form.cleaned_data['course_name']
            schedule_post.modules_taken = form.cleaned_data['modules_taken']
            schedule_post.desc = form.cleaned_data['desc']
            schedule_post.user = request.user
            schedule_post.save()
            form = ScheduleForm()
            return redirect('/schedule')
        args = {'form': form}
        return render(request, self.template_name, args)

