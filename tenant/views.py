from django.shortcuts import render
from .utilities import get_tenant
from .models import Member

# Create your views here.
def get_members(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant).all()
    return render(request, 'members.html', {'tenant':tenant,'members': members})
    