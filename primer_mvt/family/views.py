from django.shortcuts import render
from family.models import Family

def new_member(request):
    new_member = Family.objects.create(
        name= 'Pedro Bermúdez', age = 40, year_birth = '1982-05-09'
    )
    context = {
        'new_member':new_member
    }
    return render(request, 'new_member.html', context=context)

def list_members(request):
    members = Family.objects.all()
    context = {
        'members':members
    }
    return render(request, 'members.html', context=context)