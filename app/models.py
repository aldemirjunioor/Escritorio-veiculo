from django.db import models

STADO_CHOICES = (
    ('vencida', 'Vencida'),
    ('válida', 'Válida')
)

OP_CHOICES = (
    ('sim', 'Sim'),
    ('não', 'Não')
)

class Contrato(models.Model):
    num = models.DecimalField('Numero do Contrato', max_digits=8, decimal_places=0)
    num_escritorio = models.DecimalField('Numero do Escritório', max_digits=8, decimal_places=0)
    data = models.DateField('Data do Contrato')
    duracao = models.DecimalField('Duração do Contrato', max_digits=2, decimal_places=0)

    def __str__(self):
        return str(self.num)  

class Escritorio(models.Model):
    local = models.CharField(max_length=150)
    num_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.local
    
class Cliente(models.Model):
    num_hab = models.DecimalField('Número da Habilitação', max_digits=10, decimal_places=0)
    stado_hab = models.CharField('Estado da Habilitação', max_length=7, choices=STADO_CHOICES)
    nome_cliente = models.CharField('Nome do Cliente', max_length=150)
    end_cliente = models.CharField('Endereço do Cliente', max_length=200)
    tel_cliente = models.CharField('Telefone do Cliente', max_length=15)
    
    def __str__(self):
        return str(self.num_hab)
    
class Veiculo(models.Model):
    num_veiculo = models.DecimalField('Número do Veículo', max_digits=9, decimal_places=0)
    data_prox_manut = models.DateField('Data da Próxima Manutenção')
    placa = models.CharField('Número do Placa', max_length=10)

    def __str__(self):
        return str(self.num_veiculo)

class TipoVeiculo(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=2)
    nome_veiculo = models.CharField(max_length=90)
    ar_cond = models.CharField(max_length=3, choices=OP_CHOICES)
    
    def __str__(self):
        return str(self.codigo)
    
class Automovel(TipoVeiculo):
    num_portas = models.DecimalField(max_digits=2, decimal_places=0)
    dir_hidraulica = models.CharField(max_length=3, choices=OP_CHOICES)
    cambio_auto = models.CharField(max_length=3, choices=OP_CHOICES)
   
    def __str__(self):
        return str(self.num_portas)
    
class Onibus(TipoVeiculo):
    num_passag = models.DecimalField(max_digits=3, decimal_places=0)
    leito = models.CharField(max_length=30)
    sanitario = models.CharField(max_length=3, choices=OP_CHOICES)
    
    def __str__(self):
        return str(self.num_passag)
