from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Asset
from .forms import AssetForm
from django.urls import reverse_lazy

# Create your views here.
def asset_list(request):
    query = request.GET.get('q', '')
    assets = Asset.search_fields(query)
    return render(request, '', {'assets': assets}) #Finish updating with html file

def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, '', {'form': form}) #Fininsh updating with html file

def asset_update(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, '', {'form': form}) #Fininsh updating with html file

def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, '', {'asset': asset})

class AssetListView(ListView):
    model = Asset
    context_object_name = 'assets'
    template_name = '' #html file here

class AssetDetailView(DetailView):
    model = Asset
    template_name = '' #html file here

class AssetCreateView(CreateView):
    model = Asset
    template_name = '' #html file goes here
    fields = [
        'serial_no',
        'asset_category',
        'asset_type',
        'owner',
        'department',
        'status',
        'notes',
    ]
    success_url = reverse_lazy('asset_list')

class AssetUpdateView(UpdateView):
    model = Asset
    template_name = ''#html file here
    fields = [
        'serial_no',
        'asset_category',
        'asset_type',
        'owner',
        'department',
        'status',
        'notes',
    ]
    success_url = reverse_lazy('asset_list')
    
class AssetDeleteView(DeleteView):
    model = Asset
    template_name = '' #html file goes here
    success_url = reverse_lazy('asset_list')    
