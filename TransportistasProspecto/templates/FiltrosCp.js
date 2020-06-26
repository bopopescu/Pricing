
var servidor = "http://gaia.inegi.org.mx/sakbe_v3.1/";
$('.id_FiltroCPOrigen').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                selectEstado('id_FiltroEstadoOrigen',data[0].response.estado);
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


$('.id_FiltroCPDestino').change(function () {
        var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(this).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                selectEstado('id_FiltroEstadoDestino',data[0].response.estado);
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


$.ajax({
    type: 'GET',
    url: "https://api-sepomex.hckdrk.mx/query/get_estados",
    success: function (data) {
        var carrier= document.getElementById('id_FiltroEstadoOrigen');
        $.each(data.response.estado, function (i, value) {
            $(carrier).append($('<option>').text(value).attr('value',value));
        });
    },
    
});
$.ajax({
    type: 'GET',
    url: "https://api-sepomex.hckdrk.mx/query/get_estados",
    success: function (data) {
        var carrier= document.getElementById('id_FiltroEstadoDestino');
        $.each(data.response.estado, function (i, value) {
            $(carrier).append($('<option>').text(value).attr('value',value));
        });
    },
    
});

$('#id_FiltroEstadoOrigen').on('change',function () {
        $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/"+ $(this).val(),
        success: function (data) {
            var carrier= document.getElementById('id_FiltroCiudadOrigen');
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

$('#id_FiltroCiudadOrigen').on('change',function () {
    var estado=$(document.getElementById('id_EstadoOrigen')).val();
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_cp_por_municipio/"+ $(this).val(),
        success: function (data) {
            $.each(data.response.cp, function (i, value) {
                if(parseInt(cpEstado)<=parseInt(value)){
                    $(document.getElementById('id_FiltroCPOrigen')).val(value);
                    CPchangecuotas('HiddenId1','id_FiltroCiudadOrigen',estado);
                    return false;
                }
            });

        },
        
    });
});

$('#id_FiltroEstadoDestino').on('change',function () {
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/"+ $(this).val(),
        success: function (data) {
            var carrier= document.getElementById('id_FiltroCiudadDestino');
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

$('#id_FiltroCiudadDestino').on('change',function () {
    var estado=$(document.getElementById('id_FiltroEstadoDestino')).val();
    $.ajax({
        type: 'GET',
        url: "https://api-sepomex.hckdrk.mx/query/get_cp_por_municipio/"+ $(this).val(),
        success: function (data) {
            $.each(data.response.cp, function (i, value) {
                if(parseInt(cpEstado)<=parseInt(value)){
                    $(document.getElementById('id_FiltroCPDestino')).val(value);
                    CPchangecuotas('HiddenId2','id_FiltroCiudadDestino',estado);
                    return false;
                }
            });
        },
        
    });
});