from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from home.models import Posts
from accounts.models import Profile
from django.core.paginator import Paginator



def tweets(request):

    tweet = Posts.objects.all().order_by('-id')
    page_number = request.GET.get('page')
    paginator = Paginator(tweet, 8)
    object_list = paginator.get_page(page_number)


    if request.method == 'POST':
        username = request.session['username']
        # profile = Profile.objects.get('image')
        author = User.objects.get(username=username)

        description = request.POST.get('description')
        Posts.objects.create(description=description, user_id=author.id)

    return render(request, 'home/tweeter.html', {'tweet': object_list})

