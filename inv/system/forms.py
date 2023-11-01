from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     is_superuser = forms.BooleanField(required=False)

#     class Meta:
#         model = User
#         fields = ("username", "first_name", "last_name", "email", "password1", "password2", "is_superuser")

# def save(self, commit=True):
#     user = super().save(commit=False)
#     user.email = self.cleaned_data['email']
#     user.first_name = self.cleaned_data['first_name']
#     user.last_name = self.cleaned_data['last_name']
#     user.is_superuser = self.cleaned_data['is_superuser']
#     user.is_staff = self.cleaned_data['is_superuser']  # los superusuarios también deben ser staff
#     if commit:
#         user.save()
#     return user

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    is_superuser = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email",
                  "password1", "password2", "is_active", "is_superuser")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = self.cleaned_data['is_active']
        user.is_superuser = self.cleaned_data['is_superuser']
        # los superusuarios también deben ser staff
        user.is_staff = self.cleaned_data['is_superuser']
        if commit:
            user.save()
        return user


class CustomUserEditForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', "is_active", 'is_superuser')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = self.cleaned_data['is_active']
        user.is_superuser = self.cleaned_data['is_superuser']
        # los superusuarios también deben ser staff
        user.is_staff = self.cleaned_data['is_superuser']
        if commit:
            user.save()
        return user


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nro_documento', 'razon_social', 'direccion')


class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursales
        fields = ('nombre_comercial', 'direccion', 'empresa_Id')
        widgets = {
            'empresa_Id': forms.Select(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('username', 'full_name', 'email', 'password')


class GroupProviderForm(forms.ModelForm):
    class Meta:
        model = GruposProveedor
        fields = ['codigo_grupo', 'grupo_descripcion',
                  'empresa_Id', 'responsable_grupo', 'activo']
        widgets = {
            'empresa_Id': forms.Select(attrs={'class': 'form-control'}),
            'responsable_grupo': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(GroupProviderForm, self).__init__(*args, **kwargs)

        # Filtrar usuarios activos en el queryset para el campo 'responsable_linea'
        self.fields['responsable_grupo'].queryset = CustomUser.objects.filter(
            is_active=True)


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('nombre_personal', 'direccion_personal',
                  'tipo_documento', 'nro_documento', 'empresa_Id')
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'empresa_Id': forms.Select(attrs={'class': 'form-control'}),
        }


class LineForm(forms.ModelForm):
    class Meta:
        model = LineasArticulos
        fields = ('codigo_linea', 'linea_descripcion',
                  'grupo_id', 'activo', 'responsable_linea')
        widgets = {
            'responsable_linea': forms.Select(attrs={'class': 'form-control'}),
            'grupo_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(LineForm, self).__init__(*args, **kwargs)

        # Filtrar usuarios activos en el queryset para el campo 'responsable_linea'
        self.fields['responsable_linea'].queryset = CustomUser.objects.filter(
            is_active=True)
        self.fields['grupo_id'].queryset = GruposProveedor.objects.filter(
            activo=True)


class SublineForm(forms.ModelForm):
    class Meta:
        model = SublineasArticulos
        fields = ('codigo_sublinea', 'sublinea_descripcion',
                  'linea_id', 'estado')
        widgets = {
            'linea_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SublineForm, self).__init__(*args, **kwargs)

        # Filtrar usuarios activos en el queryset para el campo 'responsable_linea'
        self.fields['linea_id'].queryset = LineasArticulos.objects.filter(
            activo=True)


class MarcasForm(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = ('codigo_marca', 'marca_nombre')


class UnidadesMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadesMedida
        fields = ('unidad_nombre',)


class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ('codigo_sku', 'descripcion', 'unidad_medida_id', 'marca_id', 'grupo_id',
                  'linea_id', 'sublinea_id', 'empresa_Id', 'factor_compra', 'factor_reparto')
        widgets = {
            'unidad_medida_id': forms.Select(attrs={'class': 'form-control'}),
            'marca_id': forms.Select(attrs={'class': 'form-control'}),
            'grupo_id': forms.Select(attrs={'class': 'form-control'}),
            'linea_id': forms.Select(attrs={'class': 'form-control'}),
            'sublinea_id': forms.Select(attrs={'class': 'form-control'}),
            'empresa_Id': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(ArticulosForm, self).__init__(*args, **kwargs)

        # Filtrar usuarios activos en el queryset para el campo 'responsable_linea'
        self.fields['grupo_id'].queryset = GruposProveedor.objects.filter(
            activo=True)
        self.fields['linea_id'].queryset = LineasArticulos.objects.filter(
            activo=True)
        self.fields['sublinea_id'].queryset = SublineasArticulos.objects.filter(
            estado=True)


class InventariosForm(forms.ModelForm):
    class Meta:
        model = Inventarios
        fields = ('empresa_Id', 'sucursal_id', 'fecha_inventario', 'nro_inventario', 'responsable',
                  'hora_inicio', 'hora_fin', 'total_inventario', 'estado', 'creado_por', 'fecha_creacion')
        widgets = {
            'empresa_Id': forms.Select(attrs={'class': 'form-control'}),
            'sucursal_id': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
        exclude = ['fecha_inventario', 'hora_inicio', 'hora_fin', 'fecha_creacion']  # Excluir los campos no editables
        unique_together = ('fecha_inventario', 'empresa_Id', 'sucursal_id',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(InventariosForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['creado_por'].initial = user.username

    def clean(self):
        cleaned_data = super().clean()
        # fecha_inventario = cleaned_data.get('fecha_inventario')
        empresa_Id = cleaned_data.get('empresa_Id')
        sucursal_id = cleaned_data.get('sucursal_id')

        # Verificar si ya existe un inventario con la misma fecha, empresa y sucursal
        if Inventarios.objects.filter(empresa_Id=empresa_Id, sucursal_id=sucursal_id).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                'Ya existe un inventario con la misma empresa y sucursal.')

        return cleaned_data

# class ItemsInventarioForm(forms.ModelForm):
#     class Meta:
#         model = ItemsInventario
#         fields = ('inventario_id', 'nro_item', 'articulo_id', 'stock_fisico',
#                   'devoluciones_pendientes', 'total_unidades_stock', 'precio_costo', 'total_item')
#         widgets = {
#             'inventario_id': forms.Select(attrs={'class': 'form-control'}),
#             'articulo_id': forms.Select(attrs={'class': 'form-control','label': 'Artículo a agregar'}),
#             'total_unidades_stock': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
#             'total_item': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
#         }

#     def clean_nro_item(self):
#         nro_item = self.cleaned_data['nro_item']
#         inventario_id = self.cleaned_data['inventario_id']

#         # Verificar la unicidad del nro_item en el inventario
#         if ItemsInventario.objects.filter(inventario_id=inventario_id, nro_item=nro_item).exists():
#             raise ValidationError('Este número de item ya está registrado en el inventario.')

#         return nro_item


class ItemsInventarioForm(forms.ModelForm):
    class Meta:
        model = ItemsInventario
        fields = ('inventario_id', 'nro_item', 'articulo_id', 'stock_fisico',
                  'devoluciones_pendientes', 'total_unidades_stock', 'precio_costo', 'total_item')
        widgets = {
            'inventario_id': forms.Select(attrs={'class': 'form-control'}),
            'articulo_id': forms.Select(attrs={'class': 'form-control'}),
            'total_unidades_stock': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'total_item': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        stock_fisico = cleaned_data.get('stock_fisico')
        devoluciones_pendientes = cleaned_data.get('devoluciones_pendientes')
        precio_costo = cleaned_data.get('precio_costo')

        if stock_fisico and devoluciones_pendientes:
            cleaned_data['total_unidades_stock'] = stock_fisico + devoluciones_pendientes

        if cleaned_data.get('total_unidades_stock') and precio_costo:
            cleaned_data['total_item'] = cleaned_data['total_unidades_stock'] * precio_costo

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        existing_item = ItemsInventario.objects.filter(nro_item=instance.nro_item).first()

        if existing_item:
            existing_item.stock_fisico += instance.stock_fisico
            existing_item.devoluciones_pendientes += instance.devoluciones_pendientes
            existing_item.total_unidades_stock += instance.total_unidades_stock
            existing_item.total_item += instance.total_item
            existing_item.save()
            return existing_item
        else:
            instance.save()
            return instance