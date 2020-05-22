from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from cjudge.forms import SubmissionForm
from cjudge.models import Submission


def submission_list(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Submission(docfile=request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('submission_list'))
    else:
        form = SubmissionForm()
    submissions = Submission.objects.all().order_by("-id")[:1]

    return render(request, 'cjudge/list.html', {'submissions': submissions, 'form': form})
