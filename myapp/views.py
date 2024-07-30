from django.shortcuts import render, redirect
from .models import Post, Message
from .forms import MessageForm, Message_editForm
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, page):
    posts = Post.objects.get(id=page)
    messages = Message.objects.filter(room=page)
    if request.method == 'POST':
        msg_form = MessageForm(request.POST)
        if msg_form.is_valid():
            new_username = msg_form.cleaned_data['username']
            new_msg_content = msg_form.cleaned_data['msg_content']
    
            new_message = Message(
                username = new_username,
                msg_content = new_msg_content,
                room = page
            )
            new_message.save()

    return render(request, 'post.html', {'post': posts , 'messages' : messages, 'form': MessageForm(),'formedit': Message_editForm(),})


def edit(request, id):
    message = Message.objects.get(pk=id)
    msg = message.room
    
    if request.method == 'POST':
        msg_form = Message_editForm(request.POST, instance=message)
        if msg_form.is_valid():
            msg_form.save()
    
    return redirect('post', msg)


def delete(request, id):
    message = Message.objects.get(pk=id)
    msg = message.room
    
    if request.method == 'POST':
        message.delete()

    return redirect('post', msg)
