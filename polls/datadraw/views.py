from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO


# Create your views here.

def TestView(request):

  x = np.arange(0,np.pi*3,.1)
  y = np.sin(x)

  fig = plt.figure()
  plt.plot(x,y)

  imgdata = StringIO()
  fig.savefig(imgdata, format='svg')
  imgdata.seek(0)

  data = imgdata.getvalue()

  context = { 'fig' : data } 
  return render(request, 'index.html', context)
