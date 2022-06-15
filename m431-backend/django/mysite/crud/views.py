from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, Form
from django.contrib import messages

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crud.models import MyObject
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, HTML


class MyObjectForm(ModelForm):

    class Meta:
        model = MyObject
        fields = '__all__'


# class MyObjectForm(ModelForm):
#     class Meta:
#         model = MyObject
#         fields = ['title',]


# @login_required
def object_list(request):

    object_list = MyObject.objects.all() #.order_by('-created_at')
    context = {
        'page_title': 'Objects list',
        'object_list': object_list
    }

    return render(request, 'crud/object_list.html', context)

# @login_required
def object_create(request):

    if request.method == 'POST':
        form = MyObjectForm(request.POST, files=request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            # object.user = request.user.profile
            object.save()
            messages.add_message(request, messages.INFO, 'You created succesfully your object.')
            return redirect('crud:object_list')
    else:
        form = MyObjectForm()

    context = {
        'page_title': 'Create a new object',
        'form': form,
    }
    return render(request, 'crud/object_form.html', context)

# @login_required
def object_update(request, pk):

    object = get_object_or_404(MyObject, pk=pk)
    # object = get_object_or_404(MyObject, pk=pk, creator=request.user.profile)

    if request.method == 'POST':
        form = MyObjectForm(request.POST, files=request.FILES, instance=object)

        if form.is_valid():
            object_update = form.save(commit=False)
            # object.user = request.user.profile
            object_update.save()
            messages.add_message(request, messages.INFO, 'You updated succesfully your object.')
            return redirect('crud:object_list')

    else:
        form = MyObjectForm(request.POST or None, instance=object)
    
    context = {
        'page_title': 'Edit an object',
        'form': form,
        'object': object,
    }
    return render(request, 'crud/object_form.html', context)

# @login_required
def object_delete(request, pk):

    object = get_object_or_404(MyObject, pk=pk)
    # object = get_object_or_404(MyObject, pk=pk, creator=request.user.profile)
    if request.method=='POST':
        object.delete()
        messages.add_message(request, messages.INFO, 'You deleted succesfully your object.')
        return redirect('crud:object_list')

    context = {
        'page_title': 'Delete a object',
        'object':object,
    }
    return render(request, 'crud/object_confirm_delete.html', context)
