from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import random
from .models import Question, Choice
from django.http import HttpResponse


# Create your views here.
def IndexView(request):

  questions = Question.objects.all()
  context = { 'questions' : questions }

  if request.method == 'POST':
      choice = request.POST['choice']
      question = request.POST['question']
      context = { 'questions' : questions, 'choice' : choice, 'question' : question }
      
      q = Question.objects.filter(pk = question).first()
      ch = Choice(question = q, choice = choice)
      ch.save()     

  return render(request, 'index.html', context)

def AddRandView(request, pk):

  choice = request.POST['choice']
  q = Question.objects.filter(pk = pk).first()
  random_nums = [random.randint(1, 100) for _ in range(int(choice))] 
  added = []
  for x in random_nums:
    ch = Choice(question = q, choice = x)
    ch.save() 
    added.append('Added number ' + str(x) + ' to question: ' + q.question_text)

  return render(request, 'random.html', { 'added' : added })

def ResultsView(request, pk):

  type_of_graph = request.POST['choice']

  choices = Choice.objects.all().filter(question=Question.objects.all().filter(pk=pk).first())
  array = []
  for x in choices:
    array.append(x.choice)

  fig = plt.figure(figsize=[10, 6])
  if type_of_graph == 'hist':
    plt.hist(array, bins=35)
  elif type_of_graph == 'boxplot':
    plt.boxplot(array)

  imgdata = StringIO()
  fig.savefig(imgdata, format='svg')
  imgdata.seek(0)

  data = imgdata.getvalue()

  context = { 'fig' : data } 
  return render(request, 'results.html', context)

def DeleteChoicesView(request):   
  Choice.objects.all().delete()
  return HttpResponse("Deleted all choices")
