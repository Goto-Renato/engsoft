from django.shortcuts import render_to_response
from sancamobapp.models import Rep

def reps(request):
    return render_to_response('reps.html',
                              {'reps':Rep.objects.all()})
def rep(request, rep_id=1):
    return render_to_response('rep.html',
                              {'rep': Rep.objects.get(id=rep_id)})


