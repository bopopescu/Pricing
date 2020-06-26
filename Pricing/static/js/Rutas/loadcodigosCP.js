function agregaLoadModRutas(estadoOri, cuidadOri,estadoDes, cuidadDes) {
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_estados",
        success: function (data) {
            var carrier= document.getElementById('id_EstadoOrigen');
            $.each(data.response.estado, function (i, value) {
                $(carrier).append($('<option>').text(value).attr('value',value));
                if(value == estadoOri)
                    carrier.selectedIndex = (i+1).toString();
            });

            $.ajax({
                type: 'GET',
                url: "https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/"+ estadoOri,
                success: function (data) {
                    var carrier= document.getElementById('id_CiudadOrigen');
                    $(carrier).empty();
                    $(carrier).append($('<option>').text('Ciudad').attr('value',""));
                    $.each(data.response.municipios, function (i, value) {
                        $(carrier).append($('<option>').text(value).attr('value',value));
                        if(value==cuidadOri)
                        {
                            carrier.selectedIndex = (i+1).toString();
                        }
                    });
                },
                
            });
        },
    
    });
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_estados",
        success: function (data) {
            var carrier= document.getElementById('id_EstadoDestino');
            $.each(data.response.estado, function (i, value) {
                $(carrier).append($('<option>').text(value).attr('value',value));
                if(value == estadoDes)
                    carrier.selectedIndex = (i+1).toString();
            });
            $.ajax({
                type: 'GET',
                url: "https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/"+ estadoDes,
                success: function (data) {
                    var carrier= document.getElementById('id_CiudadDestino');
                    $(carrier).empty();
                    $(carrier).append($('<option>').text('Ciudad').attr('value',""));
                    $.each(data.response.municipios, function (i, value) {
                        $(carrier).append($('<option>').text(value).attr('value',value));
                        if(value==cuidadDes)
                        {
                            carrier.selectedIndex = (i+1).toString();
                        }
                    });
                },
                
            });
        },
        
    });
    

}

function readonlyRutas()
{
    document.getElementById("id_NombreRuta").readOnly = true;
    document.getElementById("id_CPOrigen").readOnly = true;
    document.getElementById("id_EstadoOrigen").disabled = true;
    document.getElementById("id_CiudadOrigen").disabled = true;
    document.getElementById("id_CPDestino").readOnly = true;
    document.getElementById("id_CiudadDestino").disabled = true;
    document.getElementById("id_EstadoDestino").disabled = true;
    document.getElementById("id_Kilometros").readOnly = true;
    document.getElementById("id_Casetas").readOnly = true;
    document.getElementById("id_Guardar").disabled = true;
    document.getElementById("id_Guardar").style.visibility = "hidden";
    document.getElementById('TituloID').innerHTML="Ruta";
    

}

function modRutas()
{
    document.getElementById("id_Modifica").style.visibility = "hidden";
    document.getElementById("id_Modifica").disabled = false;
    document.getElementById("id_Modifica").style.display = "none";
    document.getElementById("id_NombreRuta").readOnly = false;
    document.getElementById("id_CPOrigen").readOnly = false;
    document.getElementById("id_EstadoOrigen").disabled = false;
    document.getElementById("id_CiudadOrigen").disabled = false;
    document.getElementById("id_CPDestino").readOnly = false;
    document.getElementById("id_CiudadDestino").disabled = false;
    document.getElementById("id_EstadoDestino").disabled = false;
    document.getElementById("id_Kilometros").readOnly = false;
    document.getElementById("id_Casetas").readOnly = false;
    document.getElementById("id_Guardar").disabled = false;
    document.getElementById("id_Guardar").style.visibility = "";
    document.getElementById('TituloID').innerHTML="Modifica Ruta";

    

}