from django.urls import path
from app.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('cadastro/', CadUsuarioView.as_view(), name='cadastrouser'),
    path('login/', LoginView.as_view(), name='loginuser'),
    path('logout/', LogoutView.as_view(), name='logoutuser'),
    
    #VEÍCULO
    
    path('veiculos/', VeiculoListView.as_view(), name='veiculo_list'),
    path('criarveiculos/', VeiculoCreateView.as_view(), name='veiculo_create'),
    path('editarveiculos/<int:pk>/', VeiculoUpdateView.as_view(), name='veiculo_update'),
    path('excluirveiculos/<int:pk>/', VeiculoDeleteView.as_view(), name='veiculo_delete'),
    
    #CONTRATO
    
    path('contratos/', ContratoListView.as_view(), name='contrato_list'),
    path('criarcontratos/', ContratoCreateView.as_view(), name='contrato_create'),
    path('editarcontratos/<int:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('excluircontratos/<int:pk>/', ContratoDeleteView.as_view(), name='contrato_delete'),
    
    #CLIENTE
    
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('criarclientes/', ClienteCreateView.as_view(), name='cliente_create'),
    path('editarclientes/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('excluirclientes/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
