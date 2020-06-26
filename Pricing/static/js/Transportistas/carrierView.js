function myFunction(name) {

  if (document.getElementById(name).height==100) {
    document.getElementById(name).className = "largesize";
  }
  else
  {
    document.getElementById(name).className = "smallsize";
  }
}
function changetarjetas(name) {

  if (document.getElementById(name).height==150 && document.getElementById(name).className != "largesize") {
    document.getElementById(name).className = "largesize";
  }
  else
  {
    document.getElementById(name).className = "smallsizeTarj";
  }
}

$(function () {
	$('.datetime-input').datetimepicker({
	    format:'YYYY-MM-DD HH:mm:ss'
	});
});
$('#swmodalAlta').click(function () {
      $('#ExpedienteModal').modal().hide();
  });
  $('#swmodalActaConstitutiva').click(function () {
      $('#ExpedienteModal').modal().hide();
  });
  $('#swmodalCedulaFiscal').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalIFERepresentante').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalComDom').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalCarBan').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalConCon').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalConSer').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalConTar').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalDes').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalPer').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
  $('#swmodalLic').click(function () {
      $('#ExpedienteModal').modal('hide');
  });
    $('#close1').click(function () {
      $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close2').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close3').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close4').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close5').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close6').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close7').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close8').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close9').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close10').click(function () {
    $('#ExpedienteModal').modal().css('overflow-y', 'auto');
      $('#ExpedienteModal').modal('show');
  });
  $('#close11').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });
  $('#close12').click(function () {
    $('#ExpedienteModal').modal().css('display', 'block');
      $('#ExpedienteModal').modal('show');
  });

var ctx = document.getElementById('myChart').getContext('2d');
ctx.canvas.width = 200;
ctx.canvas.height = 200;
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Viajes Tot.', 'Kms. Tot.'],
        datasets: [{
            data: [1250, 6250],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
    	legend: {
            display: false
        },
    	responsive: false,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});