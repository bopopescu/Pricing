$('.CP').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                $(document.getElementById('id_Municipio')).val(data[0].response.municipio);
                $(document.getElementById('id_Estado')).val(data[0].response.estado);
                var colonia= document.getElementById('id_Colonia');
                $(colonia).empty();
                $.each(data, function (i, value) {
                    $(colonia).append($('<option>').text(value.response.asentamiento).attr('value', value.response.asentamiento));
                });
            },
            
        });
    });
var servidor = "http://gaia.inegi.org.mx/sakbe_v3.1/";
var municipioOrigen="";
var municipioDestino="";
var cpEstado="0";
$('.CPOrigen').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                selectEstado('id_EstadoOrigen',data[0].response.estado);
                municipioOrigen=data[0].response.municipio;
                
                $.post(servidor+"buscadestino",
                    {
                        type:"json",    
                        buscar: data[0].response.municipio,      
                        proj: "MERC",
                        num:1,
                        key: "x4cGBaOC-423Z-A9ii-AKwM-QWiCfq63rMu9"
                    },
                    function( json ){                      
                        $(document.getElementById('HiddenId1')).val(json.data[0].id_dest);   
                        Rutacuotas();  
                    }
                ); 
            },
        });
    });

function selectEstado(testado, estado){
    for(var i = 0;i < document.getElementById(testado).length;i++){
            if(document.getElementById(testado).options[i].value == estado ){
                document.getElementById(testado).selectedIndex = i;
                $(document.getElementById(testado)).change();
                  
            }
        }
}

$('.CPDestino').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                selectEstado('id_EstadoDestino',data[0].response.estado);
                municipioDestino=data[0].response.municipio;
                $.post(servidor+"buscadestino",
                    {
                        type:"json",    
                        buscar: data[0].response.municipio,      
                        proj: "MERC",
                        num:1,
                        key: "x4cGBaOC-423Z-A9ii-AKwM-QWiCfq63rMu9"
                    },
                    function( json ){                      
                        $(document.getElementById('HiddenId2')).val(json.data[0].id_dest); 
                        Rutacuotas();  
                    }
                ); 
            },
            
        });
    });

function Rutacuotas()
{
    var h1=$(document.getElementById('HiddenId1')).val();
    var h2=$(document.getElementById('HiddenId2')).val();
    $.post(servidor+"cuota",
        {
        dest_i: h1,
        dest_f: h2,
        v: 7,
        type:"json",
        proj:"MERC",
        key: "x4cGBaOC-423Z-A9ii-AKwM-QWiCfq63rMu9"
        },
          function( json ){                      
                 $(document.getElementById('id_Kilometros')).val(json.data.long_km);
                 $(document.getElementById('id_Casetas')).val(json.data.costo_caseta); 
         
    });         
}

$.ajax({
    type: 'GET',
    url: "https://api-sepomex.hckdrk.mx/query/get_estados",
    success: function (data) {
        var carrier= document.getElementById('id_EstadoOrigen');
        $.each(data.response.estado, function (i, value) {
            $(carrier).append($('<option>').text(value).attr('value',value));
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
        });
    },
    
});

$('#id_EstadoOrigen').on('change',function () {
        $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/"+ $(this).val(),
        success: function (data) {
            var carrier= document.getElementById('id_CiudadOrigen');
            $(carrier).empty();
            $(carrier).append($('<option>').text('Ciudad').attr('value',""));
            $.each(data.response.municipios, function (i, value) {
                $(carrier).append($('<option>').text(value).attr('value',value));
                if(value==municipioOrigen)
                {
                    carrier.selectedIndex = (i+1).toString();
                }
            });
        },
        
    });
    var estado=$(this).val();
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_cp_por_estado/"+ estado,
        success: function (data) {
            cpEstado = data.response.cp[0];

        },
        
    });
});

$('#id_CiudadOrigen').on('change',function () {
    var estado=$(document.getElementById('id_EstadoOrigen')).val();
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_cp_por_municipio/"+ $(this).val(),
        success: function (data) {
            $.each(data.response.cp, function (i, value) {
                if(parseInt(cpEstado)<=parseInt(value)){
                    $(document.getElementById('id_CPOrigen')).val(value);
                    CPchangecuotas('HiddenId1','id_CiudadOrigen',estado);
                    return false;
                }
            });

        },
        
    });
});

$('#id_EstadoDestino').on('change',function () {
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/"+ $(this).val(),
        success: function (data) {
            var carrier= document.getElementById('id_CiudadDestino');
            $(carrier).empty();
            $(carrier).append($('<option>').text('Ciudad').attr('value',""));
            $.each(data.response.municipios, function (i, value) {
                $(carrier).append($('<option>').text(value).attr('value',value));
                if(value==municipioDestino)
                {
                    carrier.selectedIndex = (i+1).toString();
                }
            });
        },
        
    });
    var estado=$(this).val();
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_cp_por_estado/"+ estado,
        success: function (data) {
            cpEstado = data.response.cp[0];

        },
        
    });
});

$('#id_CiudadDestino').on('change',function () {
    var estado=$(document.getElementById('id_EstadoDestino')).val();
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_cp_por_municipio/"+ $(this).val(),
        success: function (data) {
            $.each(data.response.cp, function (i, value) {
                if(parseInt(cpEstado)<=parseInt(value)){
                    $(document.getElementById('id_CPDestino')).val(value);
                    CPchangecuotas('HiddenId2','id_CiudadDestino',estado);
                    return false;
                }
            });
        },
        
    });
});
function CPchangecuotas(thidden1,tcuidad,estado){
    
    $.post(servidor+"buscadestino",
        {
            type:"json",    
            buscar: $(document.getElementById(tcuidad)).val(),      
            proj: "MERC",
            num:50,
            key: "x4cGBaOC-423Z-A9ii-AKwM-QWiCfq63rMu9"
        },
        function( json ){
            $.each(json.data, function (i, value) {
                if(comparaestados(estado,value.ent_abr)!=false)
                {            
                    $(document.getElementById(thidden1)).val(value.id_dest); 
                    return false;
                } 
            }); 
            Rutacuotas();  
        }
    ); 
}

function comparaestados(estado,abreviacion)
{
    var res="";
    var string=abreviacion.replace(/\s/g,'');
    string=string.replace(/\./g,'');
    switch(string) {
        case "Ags":
            res="Aguascalientes";
        break;
        case "BC":
            res="Baja California";
        break;
        case "BCS":
            res="Baja California Sur";
        break;
        case "Camp":
            res="Campeche";
        break;
        case "Coah":
            res="Coahuila de Zaragoza";
        break;
        case "Col":
            res="Colima";
        break;
        case "Chia":
            res="Chiapas";
        break;
        case "Chih":
            res="Chihuahua";
        break;
        case "DF":
            res="Ciudad de México";
        break;
        case "Dgo":
            res="Durango";
        break;
        case "Gto":
            res="Guanajuato";
        break;
        case "Gro":
            res="Guerrero";
        break;
        case "Hgo":
            res="Hidalgo";
        break;
        case "Jal":
            res="Jalisco";
        break;
        case "Mex":
            res="México";
        break;
        case "Mich":
            res="Michoacán de Ocampo";
        break;
        case "Mor":
            res="Morelos";
        break;
        case "Nay":
            res="Nayarit";
        break;
        case "NL":
            res="Nuevo León";
        break;
        case "Oax":
            res="Oaxaca";
        break;
        case "Pue":
            res="Puebla";
        break;
        case "Qro":
            res="Querétaro";
        break;
        case "Qroo":
            res="Quintana Roo";
        break;
        case "SLP":
            res="San Luis Potosí";
        break;
        case "Sin":
            res="Sinaloa";
        break;
        case "Son":
            res="Sonora";
        break;
        case "Tab":
            res="Tabasco";
        break;
        case "Tams":
            res="Tamaulipas";
        break;
        case "Tlax":
            res="Tlaxcala";
        break;
        case "Ver":
            res="Veracruz de Ignacio de la Llave";
        break;
        case "Yuc":
            res="Yucatán";
        break;
        case "Zac":
            res="Zacatecas";
        break;

    }
    if(res==estado)
        return true;
    else
        return false;
}