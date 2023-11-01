from django.urls import path, include
from .views import *
#E:\Workspace\app\inv\system\views
urlpatterns = [
    #path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('home', home, name='home'),  

    # path('users/list/', list_users, name='list_users'),
    path('users/list/', user_list2, name='user_list2'),
    path('users/new/', new_user2, name='new_user2'),
    path('users/edit/<str:pk>/', edit_user2, name='edit_user2'),
    path('users/delete/<str:pk>/', delete_user2, name='delete_user2'),
    # path('users/toggle_user/<str:id>/', toggle_user, name='toggle_user'),

    #Empresa
    path('company/list/', company_list, name='company_list'),
    path('company/new/', new_company, name='new_company'),
    path('company/edit/<uuid:pk>/', edit_company, name='edit_company'),
    path('company/eliminar/<uuid:pk>/', delete_company, name='delete_company'),

    #Sucursal
    path('sucursal/list/', sucursal_list, name='sucursal_list'),
    path('sucursal/new/', new_sucursal, name='new_sucursal'),
    path('sucursal/edit/<uuid:pk>/', edit_sucursal, name='edit_sucursal'),
    path('sucursal/eliminar/<uuid:pk>/', delete_sucursal, name='delete_sucursal'),

    #CRUD Usuarios
    path('user/list/', user_list, name='user_list'),
    path('user/new/', new_user, name='new_user'),
    path('user/edit/<str:pk>/', edit_user, name='edit_user'),
    path('user/delete/<str:pk>/', delete_user, name='delete_user'),

    #CRUD GruposProveedores
    path('group-provider/list/', groupprovider_list, name='groupprovider_list'),
    path('group-provider/new/', new_groupprovider, name='new_groupprovider'),
    path('group-provider/edit/<uuid:pk>/', edit_groupprovider, name='edit_groupprovider'),
    path('group-provider/delete/<uuid:pk>/',delete_groupprovider, name='delete_groupprovider'),

    #Personal
    path('personal/list/', personal_list, name='personal_list'),
    path('personal/new/', new_personal, name='new_personal'),
    path('personal/edit/<uuid:pk>/', edit_personal, name='edit_personal'),
    path('personal/eliminar/<uuid:pk>/', delete_personal, name='delete_personal'),

    # LiNEA
    path('linea/list/', linea_list, name='linea_list'),
    path('linea/new/', new_linea, name='new_linea'),
    path('linea/edit/<uuid:pk>/', edit_linea, name='edit_linea'),
    path('linea/eliminar/<uuid:pk>/', delete_linea, name='delete_linea'),
    
    # SUBLiNEA
    path('sublinea/list/', sublinea_list, name='sublinea_list'),
    path('sublinea/new/', new_sublinea, name='new_sublinea'),
    path('sublinea/edit/<uuid:pk>/', edit_sublinea, name='edit_sublinea'),
    path('sublinea/eliminar/<uuid:pk>/', delete_sublinea, name='delete_sublinea'),

    #Marcas
    path('marca/list/', marca_list, name='marca_list'),
    path('marca/new/', new_marca, name='new_marca'),
    path('marca/edit/<uuid:pk>/', edit_marca, name='edit_marca'),
    path('marca/eliminar/<uuid:pk>/', delete_marca, name='delete_marca'),
    
    #Unidades de medida
    path('unit/list/', unidades_list, name='unidades_list'),
    path('unit/new/', new_unidades, name='new_unidades'),
    path('unit/edit/<str:pk>/', edit_unidades, name='edit_unidades'),
    path('unit/eliminar/<str:pk>/', delete_unidades, name='delete_unidades'),

   #Articulos
    path('articulo/list/', articulos_list, name='articulos_list'),
    path('articulo/new/', new_articulos, name='new_articulos'),
    path('articulo/edit/<str:pk>/', edit_articulos, name='edit_articulos'),
    path('articulo/eliminar/<str:pk>/', delete_articulos, name='delete_articulos'),
  
    #Articulos
    path('inventario/list/', inventarios_list, name='inventarios_list'),
    path('inventario/new/', new_inventario, name='new_inventario'),
    path('inventario/edit/<uuid:pk>/', edit_inventario, name='edit_inventario'),
    path('inventario/delete/<uuid:pk>/', delete_inventario, name='delete_inventario'),
    path('inventarios/<uuid:inventario_id>/', inventarios_list, name='inventarios_list'),

    #path('inventario/list/<uuid:inventario_id>/', get_filtered_items, name='inventarios_items'),


    #Items
    path('items-inventario/new/', new_items_inventarios, name='new_items_inventarios'),
    path('items-inventario/list/', items_inventarios_list, name='items_inventarios_list'),
    path('items-inventario/edit/<uuid:pk>/', edit_items_inventarios, name='edit_items_inventarios'),
 ]