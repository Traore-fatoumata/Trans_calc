from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Marchandise, Cargaison
from .forms import MarchandiseForm, CargaisonForm


@login_required
def dashboard(request):
    return render(request, 'transport/dashboard.html')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username}! Vous pouvez maintenant vous connecter')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'transport/home.html')

class MarchandiseListView(ListView):
    model = Marchandise
    template_name = 'transport/marchandise_list.html'
    context_object_name = 'marchandises'

class MarchandiseCreateView(CreateView):
    model = Marchandise
    form_class = MarchandiseForm
    template_name = 'transport/marchandise_form.html'
    success_url = reverse_lazy('marchandise_list')

class MarchandiseUpdateView(UpdateView):
    model = Marchandise
    form_class = MarchandiseForm
    template_name = 'transport/marchandise_form.html'
    success_url = reverse_lazy('marchandise_list')

class MarchandiseDeleteView(DeleteView):
    model = Marchandise
    template_name = 'transport/marchandise_confirm_delete.html'
    success_url = reverse_lazy('marchandise_list')

class CargaisonListView(ListView):
    model = Cargaison
    template_name = 'transport/cargaison_list.html'
    context_object_name = 'cargaisons'

class CargaisonCreateView(CreateView):
    model = Cargaison
    form_class = CargaisonForm
    template_name = 'transport/cargaison_form.html'
    success_url = reverse_lazy('cargaison_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        marchandises_ids = self.request.POST.getlist('marchandises')
        self.object.marchandises.set(marchandises_ids)
        return response

class CargaisonDeleteView(DeleteView):
    model = Cargaison
    template_name = 'transport/cargaison_confirm_delete.html'
    success_url = reverse_lazy('cargaison_list')

def calculer_cout(request, pk):
    cargaison = get_object_or_404(Cargaison, pk=pk)
    cout = cargaison.calculer_cout()
    stats = {
        'poids_total': cargaison.poids_total(),
        'volume_total': cargaison.volume_total(),
        'nombre_marchandises': cargaison.marchandises.count(),
    }
    return render(request, 'transport/calcul_result.html', {
        'cargaison': cargaison,
        'cout': cout,
        'stats': stats
    })