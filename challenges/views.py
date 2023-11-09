from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.
monthlychallenges = {
    "january": "Eat no meat entire month !",
    "february": "walk for atleast 20 min",
    "march": "learn django for atleast 20 min ",
    "april": "Eat no meat entire month !",
    "may": "walk for atleast 20 min",
    "june": "learn django for atleast 20 min ",
    "july": "Eat no meat entire month !",
    "august": "walk for atleast 20 min",
    "september": "learn django for atleast 20 min ",
    "october": "Eat no meat entire month !",
    "november": "walk for atleast 20 min",
    "december": "learn django for atleast 20 min "
}
def monthly_challenges_by_number(request, month):
    months = list(monthlychallenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/"+redirect_month)

def monthly_challenges(request, month):
    try:
        challengetext=monthlychallenges[month]
        return HttpResponse(challengetext)
       
    except:
        return HttpResponseNotFound("Invalid month")