from django.shortcuts import render
from .models import Profile
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user_id=request.user.id)
        except:
            profile = Profile(user=request.user)
        try:
            profile.avatar = request.user.socialaccount_set.filter(provider='google')[0].extra_data['picture']
        except:
            profile.avatar = "{% static img/avatar.png%}"
        profile.save()
    return render(request, 'index.html')


def gig_detail_page(request, pk):
    return render(request, 'gig_detail.html')
