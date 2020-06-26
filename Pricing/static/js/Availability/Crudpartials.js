$(function () {

            /* Functions */

            var loadForm = function () {
            var btn = $(this);
            $.ajax({
              url: btn.attr("data-url"),
              type: 'get',
              dataType: 'json',
              beforeSend: function () {
                $("#myModal").modal("show");
              },
              success: function (data) {
                $("#myModal .modal-content").html(data.html_form);
                loadCarrier();
              }
            });
            };

            var saveForm = function () {
            var form = $(this);
            $.ajax({
                url: form.attr("action"),
                data: form.serialize(),
                type: form.attr("method"),
                dataType: 'json',
                success: function (data)
                {
                    if (data.form_is_valid) {
                        $("#sample_5 tbody").html(data.Equipo_list);
                        $("#myModal").modal("hide");
                        document.getElementById('id_total').innerHTML=data.equipoTotal;
                    }
                    else {
                        $("#myModal .modal-content").html(data.html_form);

                    }
                }

            });
            return false;
            };

            /* Binding */

            // Create book
            $(".js-create-book").on('click',loadForm);
            $("#myModal").on("submit", ".js-book-create-form", saveForm);

            // Update book
            $("#sample_5").on("click", ".js-update-book", loadForm);
            $("#myModal").on("submit", ".js-book-update-form", saveForm);

            $("#sample_5").on("click", ".js-delete-book", loadForm);
            $("#myModal").on("submit", ".js-book-delete-form", saveForm);

             $("#ModalCarrier").on("submit", ".updateCarrier-form", CarrierSaveForm);

        });

        function loadCarrier (){
            $.ajax({
                type: 'GET',
                url: "/../costeo/loadTransport",
                success: function (data) {
                    var carrier= document.getElementById('id_Carrier');
                    $(document.getElementById('id_Rutas')).empty();
                    $(document.getElementById('id_Rutas')).append($('<option>').text("").attr('value', ""));
                    $.each(data, function (i, value) {
                        $(carrier).append($('<option>').text(value.fields.RazonSocial).attr('value', value.pk));
                    });
                },
            });
        }
        
        function LoadCarrierForm(urlupdate) {
            $.ajax({
              url: urlupdate,
              type: 'get',
              dataType: 'json',
              beforeSend: function () {
                $("#ModalCarrier").modal("show");
              },
              success: function (data) {
                $("#ModalCarrier .modal-content").html(data.html_form);

              }
            });
        };
        var CarrierSaveForm = function () {
            var form = $(this);
            $.ajax({
                url: form.attr("action"),
                data: form.serialize(),
                type: form.attr("method"),
                dataType: 'json',
                success: function (data)
                {
                    if (data.form_is_valid) {
                        $("#sample_5 tbody").html(data.Equipo_list);
                        $("#ModalCarrier").modal("hide");
                        document.getElementById('id_total').innerHTML=data.equipoTotal;
                    }
                    else {
                        $("#ModalCarrier .modal-content").html(data.html_form);

                    }
                }

            });
            return false;
            };