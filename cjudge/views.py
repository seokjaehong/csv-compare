from django.shortcuts import render

from cjudge.forms import SubmissionForm
from cjudge.models import Submission
from cjudge.utils import calculate_csv


def submission_list(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            doc_file = request.FILES['docfile']
            submission = Submission.objects.create(
                docfile=doc_file
            )

            form = SubmissionForm()
            _state, result = calculate_csv(submission)
            if _state:
                submission.score = result['score']
                submission.save()

            return render(request, 'cjudge/list.html', {
                'submission': submission,
                'form': form,
                'result': result,
            })
    else:
        form = SubmissionForm()
        return render(request, 'cjudge/list.html', {'form': form})
