from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html')

class NewPollView(generic.FormView):
    template_name = 'new.html'

class ListPollsView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question':question,
            'error_message': "No seleccionaste ninguna opcion"
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))