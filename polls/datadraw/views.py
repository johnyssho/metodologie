from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import random
from .models import Question
from django.http import HttpResponse


# Create your views here.
def IndexView(request):

  questions = Question.objects.all()
  context = { 'questions' : questions }

  if request.method == 'POST':
      choice = request.POST['choice']
      context = { 'questions' : questions, 'choice' : choice }
  return render(request, 'index.html', context)

def ResultsView(request):

  x = [random.randint(1, 100) for _ in range(200)]

  fig = plt.figure(figsize=[10, 6])
  plt.hist(x, bins=35)

  imgdata = StringIO()
  fig.savefig(imgdata, format='svg')
  imgdata.seek(0)

  data = imgdata.getvalue()

  context = { 'fig' : data } 
  return render(request, 'results.html', context)
