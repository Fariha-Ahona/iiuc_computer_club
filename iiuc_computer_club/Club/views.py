from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContactMessage
from .models import Notice, Notification,Announcement,Event



def main(request):
    return render(request, 'main.html')


def signin(request):
    if request.method == 'POST':
        if 'signup' in request.POST:  # Signup form submitted
            username = request.POST.get('txt')
            email = request.POST.get('email')
            password = request.POST.get('pswd')

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('signin')

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('signin')

        elif 'login' in request.POST:  # Login form submitted
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')  # Redirect to dashboard
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
                return redirect('signin')

    return render(request, 'signin.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been LOGGED OUT!")
    return redirect(reverse('main'))


def dashboard(request):
    return render(request, 'ex dash.html')
@login_required
def dashboard(request):
    user = request.user
    return render(request, 'ex dash.html', {'user': user})
def about(request):
    return render(request, 'about.html')
# def event(request):
    return render(request, 'dashboard/event.html')

def notice(request):
    return render(request, 'dashboard/notice.html')

def notice(request):
    notices = Notice.objects.all().order_by('-date_posted')  # Display the latest notices first
    notifications = Notification.objects.filter(is_read=False).count()  # Unread notifications count

    return render(request, 'notice.html', {
        'notices': notices,
        'notifications': notifications,
    })
def announcement(request):
    # Fetch announcements and order by the latest
    announcements = Announcement.objects.all().order_by('-date_posted')
    # Fetch unread notifications count
    notifications = Notification.objects.filter(is_read=False).count()

    return render(request, 'notice.html', {
        'announces': announcements,
        'notifications': notifications,
    })
    
from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})

def save_enquiry(request):
    return render(request,'main.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact message to the database
        ContactMessage.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )

        # Add a success message
        messages.success(request, "Your message has been sent successfully!")
        return redirect('main')

    return render(request, 'main.html')
def save_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('main')  # Replace 'contact' with the name of you

from .models import BlogPost
from .forms import BlogPostForm
def Blog(request):
    return render(request, 'Blog.html')
    
#blog's fucion
def blog_page(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.approved = False 
            post.save()
            return redirect('blog_page')
    else:
        form = BlogPostForm()

    featured_posts = {
        'academic': BlogPost.objects.filter(approved=True, feature='academic').order_by('-created_at'),
        'taskmanagement': BlogPost.objects.filter(approved=True, feature='taskmanagement').order_by('-created_at'),
        'suggestions': BlogPost.objects.filter(approved=True, feature='suggestions').order_by('-created_at'),
        'special': BlogPost.objects.filter(approved=True, feature='special').order_by('-created_at'),
    }

    context = {
        'form': form,
        'featured_posts': featured_posts
    }
    return render(request, 'Blog.html', context)