# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import Question, Choice


# Create your views here.


"""
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
"""


"""
def index(request):
	 #Uses templates; avoids hardcoding in view
	 latest_question_list = Question.objects.order_by('-pub_date')[:5]
	 template = loader.get_template('polls/index.html')
	 context = {
	 	'latest_question_list' : latest_question_list
	 }
	 return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    template = loader.get_template("polls/details.html")
    
    return render(request, "polls/details.html", {'question':question})



def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question' : question})
"""

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
    	selected_choice = question.choice_set.get(id=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
    	#Redisplay question voting form
    	template = loader.get_template('polls/details.html')
    	context = {
    		'question' : question,
    		'error_message' : "You didnt select a choice"
    	}
    	return HttpResponse(template.render(context, request))
    #increment vote count	
    selected_choice.votes += 1
    #call save explicitly
    selected_choice.save()	
    #Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#Switch to using django's generic views
class IndexView(generic.ListView):
	#overide automatically generated context variable and template names
	template_name = 'polls/index.html'
	context_object_name = "latest_question_list"

	def get_queryset(self):
		#Last five published questions
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = "polls/details.html"

class ResultsView(generic.DetailView):
	model = Question
	template_name = "polls/results.html"