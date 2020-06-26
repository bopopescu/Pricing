$.ajax({
    type: 'GET',
    url: "loadCarriers",
    success: function (data) {
        var carrier= document.getElementById('id_IDCarrier');
        $(carrier).empty();
        $.each(data, function (i, value) {
            $(carrier).append($('<option>').text(value.fields.RazonSocial).attr('value', value.pk));
        });
    },
    
});

$.ajax({
    type: 'GET',
    url: "loadCarriers",
    success: function (data) {
        var carrier= document.getElementById('id_IDTransportista');
        $(carrier).empty();
        $.each(data, function (i, value) {
            $(carrier).append($('<option>').text(value.fields.RazonSocial).attr('value', value.pk));
        });
    },
    
});