$('.CP').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                $(document.getElementById('id_Ciudad')).val(data[0].response.municipio);
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
$('.CPOrigen').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                $(document.getElementById('id_CiudadOrigen')).val(data[0].response.municipio);
                $(document.getElementById('id_EstadoOrigen')).val(data[0].response.estado);
                $.post(servidor+"buscadestino",
                    {
                        type:"json",    
                        buscar: $(document.getElementById('id_CiudadOrigen')).val(),      
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

$('.CPDestino').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                $(document.getElementById('id_CiudadDestino')).val(data[0].response.municipio);
                $(document.getElementById('id_EstadoDestino')).val(data[0].response.estado);
                $.post(servidor+"buscadestino",
                    {
                        type:"json",    
                        buscar: $(document.getElementById('id_CiudadDestino')).val(),      
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

function Rutacuotas(){
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