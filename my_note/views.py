from django.shortcuts import render, redirect
from my_note.models import *


def index(request):
    contact_list = Contact.objects.all()
    context_dic = {}
    context_dic['contacts'] = contact_list
    return render(request, 'index.html', context_dic)


def add_contact(request):
    name = request.POST['name']
    last_name = request.POST['last_name']
    new_contact = Contact.objects.create(name=name, last_name=last_name, profile_photo='')
    new_contact.save()
    return redirect('index-url')


def view_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    numbers = PhoneNumber.objects.filter(contact=contact)
    context_dic = {}
    context_dic['contact'] = contact
    context_dic['numbers'] = numbers
    return render(request, 'contact-info.html', context_dic)


def add_phone_number(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    new_number = PhoneNumber.objects.create(contact=contact)
    new_number.name = request.POST['name']
    new_number.number = request.POST['number']
    new_number.save()
    return redirect('view-contact', contact_id)


def view_history(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    histories = CallHistory.objects.filter(contact=contact)
    context_dic = {}
    context_dic['contact'] = contact
    context_dic['histories'] = histories
    return render(request, 'history-info.html', context_dic)


def add_history(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    new_history = CallHistory.objects.create(contact=contact)
    new_history.number = request.POST['number']
    new_history.history_time = request.POST['time']
    new_history.history_type = request.POST['type']
    new_history.save()
    return redirect('view-history', contact_id)
