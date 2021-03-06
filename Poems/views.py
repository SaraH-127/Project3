from django.shortcuts import render, redirect

from django.contrib import messages

from .models import *

def index(request):
    return render(request, 'index.html')


def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'wall_messages': Wall_Message.objects.all()
    }
    return render(request, 'success.html', context)

def register(request):
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['pw'])
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/success')

def login(request):
    print(request.POST)
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pw']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')

def post_mess(request):
    Wall_Message.objects.create(message=request.POST['mess'], poster=User.objects.get(id=request.session['id']))
    return redirect('/success')

def post_comment(request, id):
    poster = User.objects.get(id=request.session['id'])
    message = Wall_Message.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/success')

def profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'profile.html', context)

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/success')

def delete_comment(request, id):
    destroyed = Comment.objects.get(id=id)
    destroyed.delete()
    return redirect('/success')

def delete_post(request, id):
    destroyed = Wall_Message.objects.get(id=id)
    destroyed.delete()
    return redirect('/success')

def edit(request, id):
    edit_user = User.objects.get(id=id)
    edit_user.first_name = request.POST['fname']
    edit_user.last_name = request.POST['lname']
    edit_user.email = request.POST['email']
    edit_user.save()
    return redirect('/success')

def story(request):
    context = {
        'writings': Writing.objects.all()
    }
    return render(request, 'writings.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Writing.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/writings/new')

    Writing.objects.create(
        title = request.POST['title'],
        writing = request.POST['writing'],
    )
    return redirect('/writings')

def editor(request, writing_id):
    one_writing = Writing.objects.get(id=writing_id)
    context = {
        'writing': one_writing
    }
    return render(request, 'edit.html', context)

def update(request, writing_id):
    errors = Writing.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/writings/{writing_id}/edit')
    to_update = Writing.objects.get(id=writing_id)
    to_update.title = request.POST['title']
    to_update.writing = request.POST['writing']
    to_update.save()
    return redirect('/writings/')

def writing(request, writing_id):
    one_writing = Writing.objects.get(id=writing_id)
    context = {
        'writing': one_writing
    }
    return render(request, 'writing.html', context)

def to_delete(request, writing_id):
    to_delete = Writing.objects.get(id=writing_id)
    to_delete.delete()
    return redirect('/writings')

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')