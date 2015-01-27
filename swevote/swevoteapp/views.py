from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from swevoteapp.models import Election, Candidate, User

# Create your views here.
def index(request):
    return render(request, 'swevoteapp/index.html')

def detail(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    current_election = get_object_or_404(Election, pk=Election.objects.get(is_current=True).id)
    candidates_list = current_election.candidate_set.all()
    return render(request, 'swevoteapp/detail.html', {'current_election': current_election, 'candidates_list': candidates_list})

def vote(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    current_election = get_object_or_404(Election, pk=Election.objects.get(is_current=True).id.first())
    candidates_list = current_election.candidate_set.all()
    try:
        selected_candidate =candidates_list.get(pk=request.POST['candidate'])
    except (KeyError, Candidate.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'swevoteapp/detail.html', {
            'current_election':current_election,
            'candidates_list': candidates_list,
            'error_message': "You didn't select a candidate.",
        })
    else:
        if not Election.objects.filter(users_have_voted_list=request.user.id).exists(): 
            selected_candidate.num_votes += 1
            selected_candidate.save()
            current_election.users_have_voted_list.add(request.user)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
            return HttpResponseRedirect(reverse('swevoteapp:thanks'))
        else:
            return render(request, 'swevoteapp/detail.html', {
            'current_election':current_election,
            'candidates_list': candidates_list,
            'error_message': "You have already voted in this election.",
        })

def thanks(request): #shows thanks for voting page after person votes
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    return render(request, 'swevoteapp/thanks_for_voting.html')
