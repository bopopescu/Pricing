function agregaRuta(id) {
  $.ajax({
    url: "AddRutas/"+id+"/",
    type: 'get',
    dataType: 'json',
    beforeSend: function () {
      $("#rutasModal").modal("show");
    },
    success: function (data) {
      $("#rutasModal .modal-content").html(data.html_form);
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
              $("#rutasModal").modal("hide");
          }
          else {
              $("#rutasModal .modal-content").html(data.html_form);
          }
      }

  });
  return false;
  };
$("#rutasModal").on("submit", ".js-book-delete-form", saveForm);