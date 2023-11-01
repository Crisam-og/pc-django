# Generated by Django 4.2.6 on 2023-11-01 00:12

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('articulo_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo_sku', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('factor_compra', models.IntegerField()),
                ('factor_reparto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresa_Id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nro_documento', models.CharField(max_length=11, verbose_name='Nro Documento')),
                ('razon_social', models.CharField(max_length=150, verbose_name='Razon Social')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='GruposProveedor',
            fields=[
                ('grupo_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo_grupo', models.CharField(max_length=15)),
                ('grupo_descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('empresa_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.empresa', verbose_name='Empresa')),
                ('responsable_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventarios',
            fields=[
                ('inventario_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('fecha_inventario', models.DateField(auto_now_add=True)),
                ('nro_inventario', models.IntegerField()),
                ('hora_inicio', models.TimeField(auto_now=True)),
                ('hora_fin', models.TimeField()),
                ('total_inventario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('estado', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('closed', 'Closed')], max_length=20)),
                ('creado_por', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
                ('empresa_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='LineasArticulos',
            fields=[
                ('linea_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo_linea', models.CharField(max_length=15)),
                ('linea_descripcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('grupo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.gruposproveedor')),
                ('responsable_linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('marca_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo_marca', models.CharField(max_length=14)),
                ('marca_nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_documento',
            fields=[
                ('tipo_documento_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadesMedida',
            fields=[
                ('unidad_medida_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('unidad_nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('username', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('sucursal_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(max_length=150, verbose_name='Nombre comercial')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('empresa_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.empresa', verbose_name='Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='SublineasArticulos',
            fields=[
                ('sublinea_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo_sublinea', models.CharField(max_length=15)),
                ('sublinea_descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('linea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.lineasarticulos')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('personal_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre_personal', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion_personal', models.CharField(max_length=150, verbose_name='Direccion')),
                ('tipo_documento', models.CharField(choices=[('DNI', 'DNI'), ('CARNET', 'CARNET'), ('PASSAPORT', 'PASAPORTE')], max_length=10, verbose_name='Tipo documento')),
                ('nro_documento', models.CharField(max_length=11, verbose_name='Documento')),
                ('empresa_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.empresa', verbose_name='Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='ItemsInventario',
            fields=[
                ('item_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nro_item', models.IntegerField()),
                ('stock_fisico', models.DecimalField(decimal_places=2, max_digits=12)),
                ('devoluciones_pendientes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_unidades_stock', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_item', models.DecimalField(decimal_places=2, max_digits=12)),
                ('articulo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.articulos')),
                ('inventario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.inventarios')),
            ],
        ),
        migrations.AddField(
            model_name='inventarios',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.personal'),
        ),
        migrations.AddField(
            model_name='inventarios',
            name='sucursal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.sucursales'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='empresa_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.empresa'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='grupo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.gruposproveedor'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='linea_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.lineasarticulos'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='marca_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.marcas'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='sublinea_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.sublineasarticulos'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='unidad_medida_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.unidadesmedida'),
        ),
        migrations.AlterUniqueTogether(
            name='inventarios',
            unique_together={('fecha_inventario', 'empresa_Id', 'sucursal_id')},
        ),
    ]
