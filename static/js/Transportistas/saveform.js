function agregaRuta(id) {
  $.ajax({
    url: "AddRutas/"+id+"/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#TransportistaModal").modal("show");
    },
    success: function (data) {
      $("#TransportistaModal .modal-content").html(data.html_form);
    }
  });
}
function agregaRuta(id) {
  $.ajax({
    url: "AddRutas/"+id+"/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#TransportistaModal").modal("show");
    },
    success: function (data) {
      $("#TransportistaModal .modal-content").html(data.html_form);
    }
  });
}
function agregaContacto(id) {
  $.ajax({
    url: "AddContacto/"+id+"/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#TransportistaModal").modal("show");
    },
    success: function (data) {
      $("#TransportistaModal .modal-content").html(data.html_form);
      document.getElementById("id_Modifica").style.visibility = "hidden";
      document.getElementById("id_Modifica").disabled = false;
      document.getElementById("id_Modifica").style.display = "none";
    }
  });
}

function agregaTransportistas() {
  $.ajax({
    url: "AddTrasnportista/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#TransportistaModal").modal("show");
    },
    success: function (data) {
      $("#TransportistaModal .modal-content").html(data.html_form);
    }
  });
}

function updateTransportista(id) {
  $.ajax({
    url: "UpdateTransportista/"+id+"/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#TransportistaModal").modal("show");
    },
    success: function (data) {
      $("#TransportistaModal .modal-content").html(data.html_form);
       var url = 'https://api-sepomex.hckdrk.mx/query/info_cp/' + $(document.getElementById('id_CodigoPostal')).val();
        $.ajax({
            type: 'GET',
            url: url,
            success: function (data) {
                var temp= $(document.getElementById('id_Colonia')).value;
                var idnet=0
                var colonia= document.getElementById('id_Colonia');
                $(colonia).empty();
                $.each(data, function (i, value) {
                  if( value.response.asentamiento == temp){
                    idenet=i;
                  }
                  $(colonia).append($('<option>').text(value.response.asentamiento).attr('value', value.response.asentamiento));

                });
                document.getElementById("id_Colonia").selectedIndex = idnet;
            },

            
        })
    }
  });
}

function updateContacto(id,idcarrier) {
  $.ajax({
    url: "contactoUpdate/"+id+"/"+idcarrier+"/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#TransportistaModal").modal("show");
    },
    success: function (data) {
      $("#TransportistaModal .modal-content").html(data.html_form);
      readonlyContacto();
    }
  });
}

function UpdateRuta(id) {
  $.ajax({
    url: "updateRutas/"+id+"/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#TransportistaModal").modal("show");
    },
    success: function (data) {
      $("#TransportistaModal .modal-content").html(data.html_form);
      agregaLoadModRutas(data.estadoOri,data.cuidadOri,data.estadoDes,data.cuidadDes);
      readonlyRutas();
    }
  });
}

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
              $("#TransportistaModal").modal("hide");
               location.reload(true);
          }
          else {
              if(data.Error)
              {
                Swal.fire(data.ErrorType)
              }
          }
      }

  });
  return false;
  };


$("#TransportistaModal").on("submit", ".js-Transportista-form", saveForm);


function readonlyContacto()
{
    document.getElementById('TituloID').innerHTML="Contacto";
    document.getElementById("id_Titulo").readOnly = true;
    document.getElementById("id_FirstName").readOnly = true;
    document.getElementById("id_MiddleName").readOnly = true;
    document.getElementById("id_LastName").readOnly = true;
    document.getElementById("id_mothermaidenname").readOnly = true;
    document.getElementById("id_JobTitle").readOnly = true;
    document.getElementById("id_Telefono").readOnly = true;
    document.getElementById("id_Telefono").disabled = true;
    document.getElementById("id_EmailAddress").readOnly = true;
    document.getElementById("id_AditionalEmailAddress").readOnly = true;
    document.getElementById("id_Guardar").disabled = true;
    document.getElementById("id_Guardar").style.visibility = "hidden";
    document.getElementById('TituloID').innerHTML="Contacto";
    

}

function modContacto()
{
    document.getElementById("id_Modifica").style.visibility = "hidden";
    document.getElementById("id_Modifica").disabled = false;
    document.getElementById("id_Modifica").style.display = "none";
    document.getElementById("id_Titulo").readOnly = false;
    document.getElementById("id_FirstName").readOnly = false;
    document.getElementById("id_MiddleName").readOnly = false;
    document.getElementById("id_LastName").readOnly = false;
    document.getElementById("id_mothermaidenname").readOnly = false;
    document.getElementById("id_JobTitle").readOnly = false;
    document.getElementById("id_Telefono").readOnly = false;
    document.getElementById("id_Telefono").disabled = false;
    document.getElementById("id_EmailAddress").readOnly = false;
    document.getElementById("id_AditionalEmailAddress").readOnly = false;
    document.getElementById('TituloID').innerHTML="Contacto";
    document.getElementById("id_Guardar").disabled = false;
    document.getElementById("id_Guardar").style.visibility = "";
    document.getElementById('TituloID').innerHTML="Modifica Contacto";

    

}