# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoria(models.Model):
    idcategoria = models.IntegerField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(db_column='nombreCategoria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    idcliente = models.IntegerField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nombrecliente = models.CharField(db_column='nombreCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    pais = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    codigopostal = models.IntegerField(db_column='codigoPostal', blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(blank=True, null=True)
    clientecol = models.CharField(db_column='Clientecol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Despacho(models.Model):
    iddespacho = models.IntegerField(db_column='idDespacho', primary_key=True)  # Field name made lowercase.
    nombrecompania = models.CharField(db_column='nombreCompania', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(blank=True, null=True)
    ordenes_idordenes = models.ForeignKey('Ordenes', models.DO_NOTHING, db_column='Ordenes_idOrdenes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'despacho'


class Detallesorden(models.Model):
    idproducto = models.IntegerField(db_column='idProducto')  # Field name made lowercase.
    idorden = models.IntegerField(db_column='idOrden', primary_key=True)  # Field name made lowercase.
    preciounidad = models.IntegerField(db_column='precioUnidad', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    descuento = models.IntegerField(blank=True, null=True)
    ordenes_idordenes = models.ForeignKey('Ordenes', models.DO_NOTHING, db_column='Ordenes_idOrdenes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detallesorden'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ordenes(models.Model):
    idordenes = models.IntegerField(db_column='idOrdenes', primary_key=True)  # Field name made lowercase.
    fechasolicitud = models.DateTimeField(db_column='fechaSolicitud')  # Field name made lowercase.
    fechaenvio = models.DateTimeField(db_column='fechaEnvio')  # Field name made lowercase.
    medioenvio = models.CharField(db_column='MedioEnvio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccionenvio = models.CharField(db_column='direccionEnvio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ciudadenvio = models.CharField(db_column='ciudadEnvio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    regionenvio = models.CharField(db_column='regionEnvio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paisenvio = models.CharField(db_column='paisEnvio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.IntegerField(db_column='codigoPostal', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.CharField(db_column='idCliente', max_length=45)  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_idCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordenes'


class Producto(models.Model):
    idproducto = models.IntegerField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='nombreProducto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idproveedor = models.IntegerField(db_column='idProveedor', blank=True, null=True)  # Field name made lowercase.
    idcategoria = models.IntegerField(db_column='idCategoria', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)
    preciounitario = models.IntegerField(db_column='precioUnitario', blank=True, null=True)  # Field name made lowercase.
    proveedor_idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_idProveedor')  # Field name made lowercase.
    categoria_idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Categoria_idCategoria')  # Field name made lowercase.
    detallesorden_idorden = models.ForeignKey(Detallesorden, models.DO_NOTHING, db_column='DetallesOrden_idOrden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.IntegerField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    nombrecompania = models.CharField(db_column='nombreCompania', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombrecontacto = models.CharField(db_column='nombreContacto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cargocontacto = models.CharField(db_column='cargoContacto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    codigopostal = models.IntegerField(db_column='codigoPostal', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    sitioweb = models.CharField(db_column='sitioWeb', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'
