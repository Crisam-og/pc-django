from django.contrib import admin
from .models import Empresa, Sucursales, GruposProveedor, LineasArticulos, UnidadesMedida, Marcas, Articulos, Tipo_documento, Personal, Usuarios, Inventarios, SublineasArticulos, ItemsInventario

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('empresa_Id', 'nro_documento', 'razon_social', 'direccion')

@admin.register(Sucursales)
class SucursalesAdmin(admin.ModelAdmin):
    list_display = ('sucursal_id', 'empresa_Id', 'nombre_comercial', 'direccion')

@admin.register(GruposProveedor)
class GruposProveedorAdmin(admin.ModelAdmin):
    list_display = ('grupo_id', 'codigo_grupo', 'grupo_descripcion', 'empresa_Id', 'activo', 'responsable_grupo')

@admin.register(LineasArticulos)
class LineasArticulosAdmin(admin.ModelAdmin):
    list_display = ('linea_id', 'codigo_linea', 'linea_descripcion', 'grupo_id', 'activo', 'responsable_linea')

@admin.register(UnidadesMedida)
class UnidadesMedidaAdmin(admin.ModelAdmin):
    list_display = ('unidad_medida_id', 'unidad_nombre')

@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    list_display = ('marca_id', 'codigo_marca', 'marca_nombre')

@admin.register(Articulos)
class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('articulo_id', 'codigo_sku', 'descripcion', 'unidad_medida_id', 'grupo_id', 'linea_id', 'sublinea_id', 'empresa_Id', 'factor_compra', 'factor_reparto', 'marca_id')

@admin.register(Tipo_documento)
class Tipo_documentoAdmin(admin.ModelAdmin):
    list_display = ('tipo_documento_id', 'nombre')

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('personal_id', 'nombre_personal', 'direccion_personal', 'tipo_documento', 'nro_documento', 'empresa_Id')

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email')

@admin.register(Inventarios)
class InventariosAdmin(admin.ModelAdmin):
    list_display = ('inventario_id', 'empresa_Id', 'sucursal_id', 'fecha_inventario', 'nro_inventario', 'responsable', 'hora_inicio', 'hora_fin', 'total_inventario', 'estado', 'creado_por')

@admin.register(SublineasArticulos)
class SublineasArticulosAdmin(admin.ModelAdmin):
    list_display = ('sublinea_id', 'codigo_sublinea', 'sublinea_descripcion', 'linea_id', 'estado')

@admin.register(ItemsInventario)
class ItemsInventarioAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'inventario_id', 'nro_item', 'articulo_id', 'stock_fisico', 'devoluciones_pendientes', 'total_unidades_stock', 'precio_costo', 'total_item')
