from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Profile, Gig
from .forms import GigForm

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
            profile.avatar = ''
        profile.save()
    gigs = Gig.objects.filter(status=True)
    return render(request, 'index.html', {'gigs': gigs})


def gig_detail_page(request, pk):
    try:
        gig = Gig.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return redirect('/')
    return render(request, 'gig_detail.html', {'gig': gig})


@login_required(login_url='/')
def create_gig(request):
    error = ''
    if request.method == 'POST':
        gig_form = GigForm(request.POST, request.FILES)
        if gig_form.is_valid():
            gig = gig_form.save(commit=False)
            gig.photo = request.FILES['photo']
            gig.user = request.user
            gig.save()
            return redirect('my_gigs')
        else:
            error = 'Данные введены неверно'
    else:
        gig_form = GigForm()
    return render(request, 'create_gig.html', {"error": error})


@login_required(login_url='/')
def my_gigs(request):
    gigs = Gig.objects.filter(user=request.user)
    return render(request, 'my_gigs.html', {"gigs": gigs})


@login_required(login_url='/')
def edit_gig(request, pk):
    try:
        gig = Gig.objects.get(pk=pk, user=request.user)
        error = ''
        if request.method == 'POST':
            gig_form = GigForm(request.POST, request.FILES, instance=gig)
            if gig_form.is_valid():
                gig.save()
                return redirect('my_gigs')
            else:
                error = 'Данные введены неверно'
        return render(request, 'edit_gig.html', {'gig': gig, 'error':error })
    except:
        return redirect('/')
