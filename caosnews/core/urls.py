from django.urls import path
from .views import index, form_perrito, form_mod_vehiculo, form_contacto ,gatos, perros, crud, salir, sesion, crearcuenta,paginaprincipal, nacional,tendencia,policial,deporte,mod_crud


urlpatterns = [
    path('nacional',nacional,name="nacional"),
    path('deporte',deporte,name="deporte"),
    path('policial',policial,name="policial"),    
    path('tendencia',tendencia,name="tendencia"),
    path('',paginaprincipal,name="paginaprincipal"),

    path('index',index,name="index"),
    path('contacto',form_contacto,name="form-contacto"),
    
    path('Visión',gatos,name='gatos'),

    path('Medicamentos',crud,name="crud"),

    path('Misión',perros,name='perros'),

    path('mod_crud',mod_crud,name='mod_crud'),

    path('sesion',sesion, name= 'sesion'),

    path('salir', salir, name='salir'),

    path("register", crearcuenta, name="crearcuenta"),

    path('form_perrito',form_perrito,name="form_perrito"),
    path('form-mod-vehiculo/<id>',form_mod_vehiculo,name="form_mod_vehiculo")
]