from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from datetime import datetime
# Create your views here.


def is_superuser(user):
    return user.is_superuser


def home(request):
    users_count = Personal.objects.all().count()
    company_count = Empresa.objects.all().count()
    grupos = GruposProveedor.objects.all().count()
    sucursales = Sucursales.objects.all().count()
    current_datetime = datetime.now()
    articulos = Articulos.objects.all().count()
    formatted_datetime = current_datetime.strftime("%A %B / %d / %Y, %H:%M:%S")
    data = {
        'num_users': users_count,
        'num_empresas': company_count,
        'formatted_datetime': formatted_datetime,
        'num_prov': grupos,
        'sucursales':sucursales,
        'articulos':articulos
    }
    return render(request, 'index.html',data)
# Seccion Login


def signup(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('user_list2')
            except IntegrityError:
                return render(request, 'login/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'login/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'login/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')


def list_users(request):
    users = User.objects.all()
    return render(request, 'login/users.html', {'users': users})


def user_list2(request):
    User = get_user_model()
    data = {
        'title': 'Listado de Usuarios',
        'users': User.objects.all(),
        'create_url': reverse_lazy('new_user2')
    }
    return render(request, 'usuario/list.html', data)


# @login_required
# @user_passes_test(is_superuser)
# def new_user2(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('user_list2')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'usuario/create.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def new_user2(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('user_list2')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuario/create.html', {'form': form})

# @login_required
# @user_passes_test(is_superuser)
# def edit_user2(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('user_list2')
#     else:
#         form = CustomUserCreationForm(instance=user)
#     return render(request, 'usuario/update.html', {'form': form})


@login_required
@user_passes_test(is_superuser)
def edit_user2(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list2')
    else:
        form = CustomUserEditForm(instance=user)
    return render(request, 'usuario/update.html', {'form': form})


@login_required
@user_passes_test(is_superuser)
def delete_user2(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user_list2')

# @login_required
# @user_passes_test(is_superuser)
# def toggle_user(request, username):
#     user = get_object_or_404(User, username=username)
#     if request.method == 'POST':
#         user.is_active = not user.is_active
#         user.save()
#         return redirect('user_list2')


@login_required
def company_list(request):
    data = {
        'title': 'Listado de Empresas',
        'empresas': Empresa.objects.all(),
        'create_url': reverse_lazy('new_company')
    }
    return render(request, 'company/list.html', data)


@login_required
def new_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company/create.html', {'form': form})


@login_required
def edit_company(request, pk):
    company = get_object_or_404(Empresa, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company/update.html', {'form': form})


@login_required
def delete_company(request, pk):
    company = get_object_or_404(Empresa, pk=pk)
    company.delete()
    return redirect('company_list')

# Seccion Sucursales


@login_required
def sucursal_list(request):
    data = {
        'title': 'Listado de Sucursales',
        'sucursales': Sucursales.objects.all(),
        'create_url': reverse_lazy('new_sucursal')
    }
    return render(request, 'sucursal/list.html', data)


@login_required
def new_sucursal(request):
    if request.method == "POST":
        form = SucursalForm(request.POST)
        if form.is_valid():
            sucursal = form.save(commit=False)
            sucursal.save()
            return redirect('sucursal_list')
    else:
        form = SucursalForm()
    return render(request, 'sucursal/create.html', {'form': form})


@login_required
def edit_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursales, pk=pk)
    if request.method == "POST":
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            sucursal.save()
            return redirect('sucursal_list')
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'sucursal/update.html', {'form': form})


@login_required
def delete_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursales, pk=pk)
    sucursal.delete()
    return redirect('sucursal_list')

# USUARIOS


@login_required
def user_list(request):
    data = {
        'title': 'Listado de Empresas',
        'usuarios': Usuarios.objects.all(),
        'create_url': reverse_lazy('new_user')
    }
    return render(request, 'user/list.html', data)


@login_required
def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user/create.html', {'form': form})


@login_required
def edit_user(request, pk):
    user = get_object_or_404(Usuarios, username=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user/update.html', {'form': form})


@login_required
def delete_user(request, pk):
    user = get_object_or_404(Usuarios, pk=pk)
    user.delete()
    return redirect('user_list')

# GRUPOS DE PROVEEDORES


@login_required
def groupprovider_list(request):
    data = {
        'title': 'Listado de Grupos de Proveedores',
        'grupos': GruposProveedor.objects.all(),
        'create_url': reverse_lazy('new_groupprovider')
    }
    return render(request, 'group-provider/list.html', data)


@login_required
def new_groupprovider(request):
    if request.method == "POST":
        form = GroupProviderForm(request.POST)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.save()
            return redirect('groupprovider_list')
    else:
        form = GroupProviderForm()
    return render(request, 'group-provider/create.html', {'form': form})


@login_required
def edit_groupprovider(request, pk):
    grupos = get_object_or_404(GruposProveedor, pk=pk)
    if request.method == "POST":
        form = GroupProviderForm(request.POST, instance=grupos)
        if form.is_valid():
            form.save()
            return redirect('groupprovider_list')
    else:
        form = GroupProviderForm(instance=grupos)
    return render(request, 'group-provider/update.html', {'form': form})


@login_required
def delete_groupprovider(request, pk):
    gruppro = get_object_or_404(GruposProveedor, pk=pk)
    gruppro.delete()
    return redirect('groupprovider_list')

# Seccion PERSONAL


@login_required
def personal_list(request):
    data = {
        'title': 'Listado de Personal',
        'personal': Personal.objects.all(),
        'create_url': reverse_lazy('new_personal')
    }
    return render(request, 'personal/list.html', data)


@login_required
def new_personal(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.save()
            return redirect('personal_list')
    else:
        form = PersonalForm()
    return render(request, 'personal/create.html', {'form': form})


@login_required
def edit_personal(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == "POST":
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            personal.save()
            return redirect('personal_list')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'personal/update.html', {'form': form})


@login_required
def delete_personal(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    personal.delete()
    return redirect('personal_list')

# seccion Line


@login_required
def linea_list(request):
    data = {
        'title': 'Listado de Líneas',
        'lineas': LineasArticulos.objects.all(),
        'create_url': reverse_lazy('new_linea')
    }
    return render(request, 'line/list.html', data)


@login_required
def new_linea(request):
    if request.method == "POST":
        form = LineForm(request.POST)
        if form.is_valid():
            linea = form.save(commit=False)
            linea.save()
            return redirect('linea_list')
    else:
        form = LineForm()
    return render(request, 'line/create.html', {'form': form})


@login_required
def edit_linea(request, pk):
    linea = get_object_or_404(LineasArticulos, pk=pk)
    if request.method == "POST":
        form = LineForm(request.POST, instance=linea)
        if form.is_valid():
            form.save()
            return redirect('linea_list')
    else:
        form = LineForm(instance=linea)
    return render(request, 'line/update.html', {'form': form})


@login_required
def delete_linea(request, pk):
    linea = get_object_or_404(LineasArticulos, pk=pk)
    linea.delete()
    return redirect('linea_list')

# seccion Subline


@login_required
def sublinea_list(request):
    data = {
        'title': 'Listado de subLineas',
        'sublineas': SublineasArticulos.objects.all(),
        'create_url': reverse_lazy('new_sublinea')
    }
    return render(request, 'subline/list.html', data)


@login_required
def new_sublinea(request):
    if request.method == "POST":
        form = SublineForm(request.POST)
        if form.is_valid():
            sublinea = form.save(commit=False)
            sublinea.save()
            return redirect('sublinea_list')
    else:
        form = SublineForm()
    return render(request, 'subline/create.html', {'form': form})


@login_required
def edit_sublinea(request, pk):
    sublinea = get_object_or_404(SublineasArticulos, pk=pk)
    if request.method == "POST":
        form = SublineForm(request.POST, instance=sublinea)
        if form.is_valid():
            form.save()
            return redirect('sublinea_list')
    else:
        form = SublineForm(instance=sublinea)
    return render(request, 'subline/update.html', {'form': form})


@login_required
def delete_sublinea(request, pk):
    sublinea = get_object_or_404(SublineasArticulos, pk=pk)
    sublinea.delete()
    return redirect('sublinea_list')

# Marca


@login_required
def marca_list(request):
    data = {
        'title': 'Marca',
        'marcas': Marcas.objects.all(),
        'create_url': reverse_lazy('new_marca')
    }
    return render(request, 'marca/list.html', data)


def new_marca(request):
    if request.method == "POST":
        form = MarcasForm(request.POST)
        if form.is_valid():
            marca = form.save(commit=False)
            marca.save()
            return redirect('marca_list')
    else:
        form = MarcasForm()
    return render(request, 'marca/create.html', {'form': form})


@login_required
def edit_marca(request, pk):
    marca = get_object_or_404(Marcas, pk=pk)
    if request.method == "POST":
        form = MarcasForm(request.POST, instance=marca)
        if form.is_valid():
            marca.save()
            return redirect('marca_list')
    else:
        form = MarcasForm(instance=marca)
    return render(request, 'marca/update.html', {'form': form})


@login_required
def delete_marca(request, pk):
    marca = get_object_or_404(Marcas, pk=pk)
    marca.delete()
    return redirect('marca_list')

# Unidades de medida


@login_required
def unidades_list(request):
    data = {
        'title': 'Unidades de medida',
        'unidades': UnidadesMedida.objects.all(),
        'create_url': reverse_lazy('new_unidades')
    }
    return render(request, 'unit/list.html', data)


@login_required
def new_unidades(request):
    if request.method == "POST":
        form = UnidadesMedidaForm(request.POST)
        if form.is_valid():
            unidades = form.save(commit=False)
            unidades.save()
            return redirect('unidades_list')
    else:
        form = UnidadesMedidaForm()

    return render(request, 'unit/create.html', {'form': form})


@login_required
def edit_unidades(request, pk):
    unidades = get_object_or_404(UnidadesMedida, pk=pk)
    if request.method == "POST":
        form = UnidadesMedidaForm(request.POST, instance=unidades)
        if form.is_valid():
            unidades.save()
            return redirect('unidades_list')
    else:
        form = UnidadesMedidaForm(instance=unidades)
    return render(request, 'unit/update.html', {'form': form})


@login_required
def delete_unidades(request, pk):
    unidades = get_object_or_404(UnidadesMedida, pk=pk)
    unidades.delete()
    return redirect('unidades_list')

# ARTICULOS


@login_required
def articulos_list(request):
    data = {
        'title': 'Artículos',
        'articulos': Articulos.objects.all(),
        'create_url': reverse_lazy('new_articulos')
    }
    return render(request, 'articulo/list.html', data)


@login_required
def new_articulos(request):
    if request.method == "POST":
        form = ArticulosForm(request.POST)
        if form.is_valid():
            unidades = form.save(commit=False)
            unidades.save()
            return redirect('articulos_list')
    else:
        form = ArticulosForm()

    return render(request, 'articulo/create.html', {'form': form})


@login_required
def edit_articulos(request, pk):
    articulo = get_object_or_404(Articulos, pk=pk)
    if request.method == "POST":
        form = ArticulosForm(request.POST, instance=articulo)
        if form.is_valid():
            articulo = form.save()
            return redirect('articulos_list')
    else:
        form = ArticulosForm(instance=articulo)
    return render(request, 'articulo/update.html', {'form': form})


@login_required
def delete_articulos(request, pk):
    articulo = get_object_or_404(Articulos, pk=pk)
    articulo.delete()
    return redirect('articulos_list')

# INVENTARIO

@login_required
def inventarios_list(request):
    inventarios = Inventarios.objects.all()
    items_inventarios = ItemsInventario.objects.all()
    data = {
        'title': 'Inventarios',
        'inventarios': inventarios,
        'items': items_inventarios,
        'create_url': reverse_lazy('new_inventario')

    }
    return render(request, 'inventario/list.html', data)

@login_required
def new_inventario(request):
    error_message = None
    if request.method == "POST":
        form = InventariosForm(request.POST, user=request.user)

        if form.is_valid():
            empresa_Id = form.cleaned_data['empresa_Id']
            sucursal_id = form.cleaned_data['sucursal_id']

            existing_inventario = Inventarios.objects.filter(
                empresa_Id=empresa_Id,
                sucursal_id=sucursal_id
            ).exclude(pk=form.instance.pk if form.instance.pk else None).first()

            if existing_inventario:
                error_message = 'Ya existe un inventario con la misma empresa y sucursal.'
            else:
                inventario = form.save(commit=False)
                inventario.hora_inicio = timezone.now()  # Establecer la hora de inicio en el momento actual
                inventario.hora_fin = timezone.now()
                inventario.creado_por = request.user
                inventario.save()
                return redirect('inventarios_list')

    else:
        form = InventariosForm(user=request.user, initial={'hora_inicio': timezone.now()})  # Establecer la hora de inicio inicial

    return render(request, 'inventario/create.html', {'form': form, 'error_message': error_message})


@login_required
def edit_inventario(request, pk):
    inventario = get_object_or_404(Inventarios, pk=pk)
    if request.method == "POST":
        form = InventariosForm(request.POST, instance=inventario)
        if form.is_valid():
            # Establecer la hora de inicio al valor original
            form.instance.hora_inicio = inventario.hora_inicio
            # Establecer la hora de fin al valor actual
            form.instance.hora_fin = timezone.now()
            form.save()
            return redirect('inventarios_list')
    else:
        form = InventariosForm(instance=inventario, user=request.user)  # Pasa el usuario actual
    return render(request, 'inventario/update.html', {'form': form, 'inventario': inventario})


@login_required
def delete_inventario(request, pk):
    inventario = get_object_or_404(Inventarios, pk=pk)
    inventario.delete()
    return redirect('inventarios_list')

# ITEMS INVENTARIOS 
@login_required
def items_inventarios_list(request):
    items_inventarios = ItemsInventario.objects.all()
    data = {
        'title': 'Lista item por inventarios',
        'items': items_inventarios,
        'create_url': reverse_lazy('new_items_inventarios')

    }
    return render(request, 'items/list.html', data)

@login_required
def new_items_inventarios(request):
    if request.method == "POST":
        form = ItemsInventarioForm(request.POST)
        if form.is_valid():
            unidades = form.save(commit=False)
            unidades.save()
            return redirect('items_inventarios_list')
    else:
        form = ItemsInventarioForm()

    return render(request, 'items/create.html', {'form': form})

@login_required
def edit_items_inventarios(request, pk):
    inventario = get_object_or_404(ItemsInventario, pk=pk)
    if request.method == "POST":
        form = ItemsInventarioForm(request.POST, instance=ItemsInventario)
        if form.is_valid():
            form.save()
            return redirect('items_inventarios_list')
    else:
        form = ItemsInventarioForm(instance=ItemsInventario)
    return render(request, 'items/update.html', {'form': form, 'items': inventario})