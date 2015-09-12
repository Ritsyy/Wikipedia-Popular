from django.conf import settings
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .wikipop import *
from .forms import WikiTitleForm
from .models import *

# Create your views here.
def home(request):
	form = WikiTitleForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		title = save_it.title
		save_it.save()
		print title
		ans = wikipop(title)
		myans = dict(ans)
		print "this is response", myans
		return render_to_response("result.html", locals(), context_instance=RequestContext(request))
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))