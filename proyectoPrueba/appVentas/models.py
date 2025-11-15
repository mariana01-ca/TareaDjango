from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) #igual que en la tabla, Cahrfield una cadena abierta
    email = models.EmailField(max_length=100)
    
    class Meta:
        managed = False #no permite alterar las tablas el framwork django no modifique
        db_table =  'clientes'
    def __str__(self):
        return self.nombre     
        
class Tienda(models.Model):
    id_tienda=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=150)
    
    class Meta:
        managed = False #no permite alterar las tablas el framwork django no modifique
        db_table =  'tiendas'
    def __str__(self):
        return self.nombre     
        
class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete= models.CASCADE,
        db_column='id_cliente'
    )
    
    tienda = models.ForeignKey(
        Tienda,
        on_delete=models.CASCADE,
        db_column='id_tienda'
    )
    
    class Meta:
        managed=False
        db_table='compras'
    def __str__(self):
        return f"{self.id_compra} - {self.cliente} - {self.fecha}"
        
               