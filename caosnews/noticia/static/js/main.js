(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el Item?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();

function valForm(){
    var vNom = $('#nombre').val();
    var vTel = $('#telefono').val();
    var vDir = $('#direccion').val();
    var vMail = $('#correo').val();
    var vMensaje = $('#mensaje').val();

    if (vNom === null || vNom === "") {
        Err_Color("nombre");
        Err_Contenido("nombre");
        return false;
    }else{
        var expresion = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if (!expresion.test(vNom)){
            Error_Color("nombre");
            Err_Contenido("No se permiten caracteres especiales o numeros");
            return false;
        } 
    }

    if (vMail === null || vMail === "") {
        Err_Color("correo");
        Err_Contenido("correo");
        return false;
    }else{
        var expresion = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if (!expresion.test(vMail)){
            Err_Color("correo");
            Err_Contenido("No se permiten caracteres especiales o numeros");
            return false;
        } 
    }

    if (vTel === null || vTel === "") {
        Err_Color("telefono");
        Err_Contenido("telefono");
        return false;
    }else{
        var temp = parseInt(vTel);
        if (temp < 9999999){
            Err_Color("telefono");
            Err_Contenido("El numero debe poseer al menos 8 digitos");
            return false;
        } 
    }

    if (vDir === null || vDir === "") {
        Err_Color("direccion");
        Err_Contenido("direccion");
        return false;
    }

    $('form').submit();
    return true;
}

function Err_Color(id_div){
    $('#'+id_div).css('border', '1px solid red');
}

function Err_Contenido(dato){
    alert("Error al ingresar: "+dato)
}

function ColorDefault(id_div){
    $('#'+id_div).css('border', '1px');
}

$('input').focus(function(){
    ColorDefault('nombre');
    ColorDefault('correo');
    ColorDefault('telefono');
    ColorDefault('direccion');   
})