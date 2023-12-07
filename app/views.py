from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from app.forms import CadUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_func
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    def handle_no_permission(self):
        return render(self.request, 'error.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class CadUsuarioView(CreateView):
    template_name = 'cadastro.html'
    form_class = CadUsuarioForm
    success_url = reverse_lazy('loginuser')
    
    def form_valid(self, form, *args, **kwargs):
        form.cleaned_data
        form.save()
        
        return super(CadUsuarioView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        return super(CadUsuarioView, self).form_invalid(form, *args, **kwargs)

class LoginView(FormView):
    template_name = 'login.html'
    model = User
    form_class = AuthenticationForm
    success_url = ('home')
    
    def form_valid(self, form):
        nome = form.cleaned_data['username']
        senha = form.cleaned_data['password']
        usuario = authenticate(self.request, username=nome, password=senha)        
        if usuario is not None:
            login_func(self.request, usuario)
            return redirect('home')
        return redirect('loginuser')
                
    def form_invalid(self, form):
        return redirect('home')

class LogoutUsuarioView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    
    def get(self, request):
        logout(request)
        return redirect('logoutuser')

class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'veiculo/veiculo_list.html'
    
class VeiculoCreateView(SuperUserRequiredMixin, CreateView):
    model = Veiculo
    template_name = 'veiculo/veiculo_form.html'
    fields = ['num_veiculo', 'data_prox_manut', 'placa']
    success_url = reverse_lazy('veiculo_list')
    
class VeiculoUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Veiculo
    template_name = 'veiculo/veiculo_form.html'
    fields = ['num_veiculo', 'data_prox_manut', 'placa' ]
    
    success_url = reverse_lazy('veiculo_list')
    
class VeiculoDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo/veiculo_confirm_delete.html'
    success_url = reverse_lazy('veiculo_list')
    
# ----------------------------
    
class ContratoListView(ListView):
    model = Contrato
    template_name = 'contrato/contrato_list.html'

class ContratoCreateView(SuperUserRequiredMixin, CreateView):
    model = Contrato
    template_name = 'contrato/contrato_form.html'
    fields = ['num', 'num_escritorio', 'data', 'duracao']
    success_url = reverse_lazy('contrato_list')
    
class ContratoUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Contrato
    template_name = 'contrato/contrato_form.html'
    fields = ['num', 'num_escritorio', 'data', 'duracao']
    success_url = reverse_lazy('contrato_list')

class ContratoDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Contrato
    template_name = 'contrato/contrato_confirm_delete.html'
    success_url = reverse_lazy('contrato_list')
    
# ----------------------------
    
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

class ClienteCreateView(SuperUserRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    fields = ['num_hab', 'stado_hab', 'nome_cliente', 'end_cliente', 'tel_cliente']
    success_url = reverse_lazy('cliente_list')
    
class ClienteUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    fields = ['num_hab', 'stado_hab', 'nome_cliente', 'end_cliente', 'tel_cliente']
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')