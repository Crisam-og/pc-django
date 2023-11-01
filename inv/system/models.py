import uuid
from django.db import models
import random
import string

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        fila = self.username
        return fila


class Empresa(models.Model):
    empresa_Id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    nro_documento = models.CharField(max_length=11, verbose_name='Nro Documento')
    razon_social = models.CharField(max_length=150, verbose_name='Razon Social')
    direccion = models.CharField(max_length=150, verbose_name='Dirección')

    def __str__(self):
        fila = self.nro_documento
        return fila

class Sucursales(models.Model):
    sucursal_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    nombre_comercial = models.CharField(max_length=150, verbose_name='Nombre comercial')
    direccion = models.CharField(max_length=150,  verbose_name='Dirección')

    def __str__(self):
            fila = self.nombre_comercial
            return fila

class GruposProveedor(models.Model):
    grupo_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    codigo_grupo = models.CharField(max_length=15)
    grupo_descripcion = models.CharField(max_length=100)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    activo = models.BooleanField()
    responsable_grupo = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        fila = self.codigo_grupo
        return fila

class LineasArticulos(models.Model):
    linea_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    codigo_linea = models.CharField(max_length=15)
    linea_descripcion = models.CharField(max_length=100)
    grupo_id = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE)
    activo = models.BooleanField()
    responsable_linea = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        fila = self.codigo_linea
        return fila

class SublineasArticulos(models.Model):
    sublinea_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    codigo_sublinea = models.CharField(max_length=15)
    sublinea_descripcion = models.CharField(max_length=100)
    linea_id = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        fila = self.codigo_sublinea
        return fila
# class UnidadesMedida(models.Model):
#     unidad_medida_id = models.CharField(primary_key=True, max_length=10)
#     unidad_nombre = models.CharField(max_length=150)


class UnidadesMedida(models.Model):
    unidad_medida_id = models.CharField(primary_key=True, max_length=10)
    unidad_nombre = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.unidad_medida_id:
            self.unidad_medida_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        super(UnidadesMedida, self).save(*args, **kwargs)

    def __str__(self):
                fila = self.unidad_nombre
                return fila

class Marcas(models.Model):
    marca_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    codigo_marca = models.CharField(max_length=14)
    marca_nombre = models.CharField(max_length=150)

    def __str__(self):
            fila = self.marca_nombre
            return fila

class Articulos(models.Model):
    articulo_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    codigo_sku = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150)
    unidad_medida_id = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE)
    grupo_id = models.ForeignKey(GruposProveedor, on_delete=models.CASCADE)
    linea_id = models.ForeignKey(LineasArticulos, on_delete=models.CASCADE)
    sublinea_id = models.ForeignKey(SublineasArticulos, on_delete=models.CASCADE)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    factor_compra = models.IntegerField()
    factor_reparto = models.IntegerField()
    marca_id = models.ForeignKey(Marcas, on_delete=models.CASCADE)

    def __str__(self):
            fila = self.codigo_sku
            return fila

class Tipo_documento(models.Model):
    tipo_documento_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    nombre = models.CharField(max_length=14)

    def __str__(self):
        fila = self.nombre
        return fila

class Personal(models.Model):
    DOC = [
        ('DNI', 'DNI'),
        ('CARNET', 'CARNET'),
        ('PASSAPORT', 'PASAPORTE'),
    ]
    personal_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    nombre_personal = models.CharField(max_length=100, verbose_name='Nombre')
    direccion_personal = models.CharField(max_length=150, verbose_name='Direccion')
    # tipo_documento = models.CharField(Tipo_documento, on_delete=models.CASCADE, verbose_name='Tipo documento')
    tipo_documento = models.CharField(max_length=10, choices=DOC, verbose_name='Tipo documento')
    nro_documento = models.CharField(max_length=11, verbose_name='Documento')
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
            fila = self.nombre_personal
            return fila

class Usuarios(models.Model):
    username = models.CharField(primary_key=True, max_length=25)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)

class Inventarios(models.Model):
    ESTADOS_INVENTARIO = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    inventario_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    empresa_Id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal_id = models.ForeignKey(Sucursales, on_delete=models.CASCADE)
    fecha_inventario = models.DateField(auto_now_add=True)
    nro_inventario = models.IntegerField()
    responsable = models.ForeignKey(Personal, on_delete=models.CASCADE)
    hora_inicio = models.TimeField(auto_now_add=True)  # Se actualizará automáticamente al crear o modificar el inventario
    hora_fin = models.TimeField(auto_now=False)  # Se actualizará automáticamente al crear o modificar el inventario
    total_inventario = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS_INVENTARIO)
    creado_por = models.CharField(max_length=15, blank=True, null=True)
    #fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            fila = self.nro_inventario
            filaN = str(fila)
            return filaN
    
    class Meta:
        unique_together = ['fecha_inventario', 'empresa_Id', 'sucursal_id']

class ItemsInventario(models.Model):
    item_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    inventario_id = models.ForeignKey(Inventarios, on_delete=models.CASCADE)
    nro_item = models.IntegerField()
    articulo_id = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    stock_fisico = models.DecimalField(max_digits=12, decimal_places=2)
    devoluciones_pendientes = models.DecimalField(max_digits=12, decimal_places=2)
    total_unidades_stock = models.DecimalField(max_digits=12, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=2)
    total_item = models.DecimalField(max_digits=12, decimal_places=2)