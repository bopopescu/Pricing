        $('#id_Carrier').on('change',function () {

                if(document.getElementById("id_Carrier").value != "")
                {
                    $.ajax({
                        type: 'GET',
                        url: "/../costeo/loadRutas/"+document.getElementById("id_Carrier").value+"/",
                        success: function (data) {
                            var ruta= document.getElementById('id_Rutas');
                            $(ruta).empty();
                            $(ruta).append($('<option>').text("Select").attr('value', ''));
                            $.each(data, function (i, value) {
                                $(ruta).append($('<option>').text(value.fields.NombreRuta).attr('value', value.pk));
                            });
                        },

                    });

                }
                else
                {
                    $(document.getElementById('id_Rutas')).empty();
                    $(document.getElementById('id_Rutas')).append($('<option>').text("").attr('value', ""));

                }
            });