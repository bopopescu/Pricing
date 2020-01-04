	    	var changecellvar="false";
	    	function ocultaPremisas() {
			  var x = document.getElementById("PreimisasHide");
			  if (x.style.display === "none") {
			    x.style.display = "block";
			 	filltables();
			  } else {
			    x.style.display = "none";
			  }
			}

			function CalculaCosteo()
			{
				$(document.getElementById('depTractoId')).val(roundToTwo(($(document.getElementById('costosUnidadId')).val()/ $(document.getElementById('mesesId')).val())/$(document.getElementById('kmsMesXunidadId')).val()));
				$(document.getElementById('depCajaId')).val(roundToTwo(($(document.getElementById('costosCajaId')).val()/ $(document.getElementById('mesesId')).val())/$(document.getElementById('kmsMesXunidadId')).val()));
				$(document.getElementById('CombustibleId')).val(roundToTwo(($(document.getElementById('kmSencilloId')).val()/$(document.getElementById('rendimiento')).val())*$(document.getElementById('dieselSinIvaId')).val()));
				$(document.getElementById('CasetasId')).val(roundToTwo($(document.getElementById('casetaSingleId')).val()/1.16));
				$(document.getElementById('OperadorId')).val(roundToTwo($(document.getElementById('kmSencilloId')).val()*$(document.getElementById('operadorId')).val()));
				var res=roundToTwo(Number($(document.getElementById('CombustibleId')).val())
				+Number($(document.getElementById('CasetasId')).val())
				+Number($(document.getElementById('OperadorId')).val()));
            	$(document.getElementById('SubTotalId')).val(res);
            	$(document.getElementById('MttoUnidadId')).val(roundToTwo($(document.getElementById('kmSencilloId')).val()*$(document.getElementById('mttoUnidadXkmId')).val()));
            	$(document.getElementById('LlantasUnidadId')).val(roundToTwo($(document.getElementById('kmSencilloId')).val()*$(document.getElementById('llantasId')).val()));
            	$(document.getElementById('GPSId')).val(roundToTwo($(document.getElementById('kmSencilloId')).val()*(Number($(document.getElementById('rentaGPSId')).val()/$(document.getElementById('kmsMaximoId')).val()))));
            	$(document.getElementById('SeguroId')).val(roundToTwo($(document.getElementById('kmSencilloId')).val()*(Number($(document.getElementById('seguroId')).val()/$(document.getElementById('kmsMaximoId')).val()))));
            	$(document.getElementById('PlacasTenenciaCostId')).val(roundToTwo($(document.getElementById('kmSencilloId')).val()*(Number($(document.getElementById('placasTenenciaId')).val()/$(document.getElementById('kmsMaximoId')).val()))));
            	res=Number($(document.getElementById('MttoUnidadId')).val())
            	+Number($(document.getElementById('LlantasUnidadId')).val())
            	+Number($(document.getElementById('GPSId')).val())
            	+Number($(document.getElementById('SeguroId')).val())
            	+Number($(document.getElementById('PlacasTenenciaCostId')).val());
            	$(document.getElementById('SubTotal2Id')).val(roundToTwo(res));
            	res=roundToTwo(Number($(document.getElementById('SubTotalId')).val())+Number($(document.getElementById('SubTotal2Id')).val()));
            	$(document.getElementById('AdmvoId')).val(roundToTwo(res*($(document.getElementById('admvoId')).val()/100)));
            	$(document.getElementById('FinancierosId')).val(roundToTwo(res*($(document.getElementById('financierosId')).val()/100)));
            	$(document.getElementById('DeprUnidadId')).val(roundToTwo($(document.getElementById('depTractoId')).val()*$(document.getElementById('kmSencilloId')).val()));
            	$(document.getElementById('DeprRemolqueId')).val(roundToTwo($(document.getElementById('depCajaId')).val()*$(document.getElementById('kmSencilloId')).val()*$(document.getElementById('unidadId')).val()));
            	res=Number($(document.getElementById('AdmvoId')).val())
            	+Number($(document.getElementById('FinancierosId')).val())
            	+Number($(document.getElementById('DeprUnidadId')).val())
            	+Number($(document.getElementById('DeprRemolqueId')).val());
            	res=roundToTwo(res);
            	$(document.getElementById('SubTotal3Id')).val(res);
            	res=Number($(document.getElementById('SubTotalId')).val())
            	+Number($(document.getElementById('SubTotal2Id')).val())
            	+Number($(document.getElementById('SubTotal3Id')).val());
            	$(document.getElementById('id_TotalCostos')).val(roundToTwo(res));
            	res=Number($(document.getElementById('id_TotalCostos')).val())*($(document.getElementById('id_MopPor')).val()/100)
            	$(document.getElementById('id_Mop')).val(roundToTwo(res));
            	res=Number($(document.getElementById('id_TotalCostos')).val())+Number($(document.getElementById('id_Mop')).val())
            	$(document.getElementById('id_TotalTransportista')).val(roundToTwo(res));
			}

			function filltables()
			{
				document.getElementById('tdMeses').innerHTML = $(document.getElementById('mesesId')).val();
				document.getElementById('tdCostoUnidad').innerHTML = $(document.getElementById('costosUnidadId')).val();
				document.getElementById('tdUnidad').innerHTML = ""+ roundToTwo($(document.getElementById('costosUnidadId')).val()/ $(document.getElementById('mesesId')).val())+"";
				document.getElementById('tdCostosCaja').innerHTML =$(document.getElementById('costosCajaId')).val();
				document.getElementById('tdCaja').innerHTML = ""+roundToTwo($(document.getElementById('costosCajaId')).val()/$(document.getElementById('mesesId')).val())+"";
				document.getElementById('tdViajesMes').innerHTML = $(document.getElementById('viajesMesId')).val();
				document.getElementById('tdKmsMesXunidad').innerHTML = $(document.getElementById('kmsMesXunidadId')).val();
				document.getElementById('tdkmsMaximo').innerHTML = $(document.getElementById('kmsMaximoId')).val();
				document.getElementById('tdKunidad').innerHTML = $(document.getElementById('unidadId')).val();
				document.getElementById('tdKmSencillo').innerHTML = $(document.getElementById('kmSencilloId')).val();
				document.getElementById('tdKmRoundTrip').innerHTML = $(document.getElementById('kmRoundTripId')).val();
				document.getElementById('tdKmMensuales').innerHTML = $(document.getElementById('kmMensualesId')).val();
				document.getElementById('tdCasetaSingle').innerHTML = $(document.getElementById('casetaSingleId')).val();
				document.getElementById('tdRendimiento').innerHTML = $(document.getElementById('rendimiento')).val();
				document.getElementById('tdDiesel').innerHTML = $(document.getElementById('dieselId')).val();
				document.getElementById('tdDieselSinIva').innerHTML = $(document.getElementById('dieselSinIvaId')).val();
				document.getElementById('depTracto').innerHTML = $(document.getElementById('depTractoId')).val();
				document.getElementById('depCaja').innerHTML = $(document.getElementById('depCajaId')).val();
				document.getElementById('tdrentaGPS').innerHTML = $(document.getElementById('rentaGPSId')).val();
				document.getElementById('tdGPS').innerHTML = ""+roundToTwo(($(document.getElementById('rentaGPSId')).val()/Number($(document.getElementById('kmsMaximoId')).val())))+"";
				document.getElementById('tdplacasTenencia').innerHTML = $(document.getElementById('placasTenenciaId')).val();
				document.getElementById('tdPlacas').innerHTML = ""+roundToTwo(($(document.getElementById('placasTenenciaId')).val()/Number($(document.getElementById('kmsMaximoId')).val())))+"";
				document.getElementById('tdseguro').innerHTML = $(document.getElementById('seguroId')).val();
				document.getElementById('tdSegurokm').innerHTML = ""+roundToTwo(($(document.getElementById('seguroId')).val()/Number($(document.getElementById('kmsMaximoId')).val())))+"";
				document.getElementById('tdAdmvo').innerHTML = $(document.getElementById('admvoId')).val();
				document.getElementById('tdFinancieros').innerHTML = $(document.getElementById('financierosId')).val();
				document.getElementById('tdMtto').innerHTML = $(document.getElementById('mttoUnidadXkmId')).val();
				document.getElementById('tdLlantas').innerHTML = $(document.getElementById('llantasId')).val();
				document.getElementById('tdOperador').innerHTML = $(document.getElementById('operadorId')).val();
				document.getElementById('tdDOperador').innerHTML = $(document.getElementById('dobleOpId')).val();
				document.getElementById('tdCombustible').innerHTML = $(document.getElementById('CombustibleId')).val();
				document.getElementById('tdCasetas').innerHTML = $(document.getElementById('CasetasId')).val();
				document.getElementById('tdOperadorOperativo').innerHTML =$(document.getElementById('OperadorId')).val();
				document.getElementById('tdSubtotal1').innerHTML =$(document.getElementById('SubTotalId')).val();
				document.getElementById('tdMttoUnidad').innerHTML =$(document.getElementById('MttoUnidadId')).val();
				document.getElementById('tdLlantasUnidad').innerHTML =$(document.getElementById('LlantasUnidadId')).val();
				document.getElementById('tdGPSCostos').innerHTML = $(document.getElementById('GPSId')).val();
				document.getElementById('tdSeguroCostos').innerHTML =$(document.getElementById('SeguroId')).val();
				document.getElementById('tdPlacasTenencia').innerHTML =$(document.getElementById('PlacasTenenciaCostId')).val();
				document.getElementById('tdSubTotal2').innerHTML =$(document.getElementById('SubTotal2Id')).val();
				document.getElementById('tdAdmvoCostos').innerHTML =($(document.getElementById('AdmvoId')).val());
            	document.getElementById('tdFinancierosCostos').innerHTML =($(document.getElementById('FinancierosId')).val());
            	document.getElementById('tdDeprUnidad').innerHTML =($(document.getElementById('DeprUnidadId')).val());
            	document.getElementById('tdDeprRemolque').innerHTML =($(document.getElementById('DeprRemolqueId')).val());
            	document.getElementById('tdSubtotal3').innerHTML =($(document.getElementById('SubTotal3Id')).val());
				if($(document.getElementById('id_TotalCostos')).val()!="")
				{
					document.getElementById('tdComb').innerHTML = Math.round((Number($(document.getElementById('CombustibleId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdCast').innerHTML = Math.round((Number($(document.getElementById('CasetasId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdOper').innerHTML = Math.round((Number($(document.getElementById('GPSId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdsub1').innerHTML = Math.round((Number($(document.getElementById('SubTotalId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdMttoUnidadPor').innerHTML = Math.round((Number($(document.getElementById('MttoUnidadId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdLlantasUnidadPor').innerHTML = Math.round((Number($(document.getElementById('LlantasUnidadId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdGPSCostosPor').innerHTML = Math.round((Number($(document.getElementById('GPSId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdSeguroCostosPor').innerHTML = Math.round((Number($(document.getElementById('SeguroId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdPlacasTenenciaPor').innerHTML = Math.round((Number($(document.getElementById('PlacasTenenciaCostId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdSubTotal2Por').innerHTML = Math.round((Number($(document.getElementById('SubTotal2Id')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdAdmvoCostosPor').innerHTML =Math.round((Number($(document.getElementById('AdmvoId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdFinancierosCostosPor').innerHTML = Math.round((Number($(document.getElementById('FinancierosId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdDeprUnidadPor').innerHTML = Math.round((Number($(document.getElementById('DeprUnidadId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdDeprRemolquePor').innerHTML =Math.round((Number($(document.getElementById('DeprRemolqueId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
					document.getElementById('tdSubtotal3Por').innerHTML = Math.round((Number($(document.getElementById('SubTotal3Id')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100)+'%';
				}
			}
			function roundToTwo(num) {
				var dec=2;
			    if ((typeof num !== 'number') || (typeof dec !== 'number'))
				return false;

				  var num_sign = num >= 0 ? 1 : -1;

				  return (Math.round((num*Math.pow(10,dec))+(num_sign*0.0001))/Math.pow(10,dec)).toFixed(dec);
			}
			$.ajax({
            type: 'GET',
            url: "/costeo/loadUnidades",
            success: function (data) {
                var unidad= document.getElementById('id_IDUnidad');
                $.each(data, function (i, value) {
                    $(unidad).append($('<option>').text(value.fields.Nombre).attr('value', value.pk));
                });
            },

            });
             $.ajax({
            type: 'GET',
            url: "/costeo/loadTransport",
            success: function (data) {
                var carrier= document.getElementById('id_IDTransportista');
                $(document.getElementById('id_IDRuta')).empty();
                $(document.getElementById('id_IDRuta')).append($('<option>').text("").attr('value', ""));
                $.each(data, function (i, value) {
                    $(carrier).append($('<option>').text(value.fields.RazonSocial).attr('value', value.pk));
                });
                $(document.getElementById('id_mopPor')).val(15);
				if(update==1)
				{
					$(document.getElementById('id_IDTransportista')).val(transportista).change();
					$('#id_IDTransportista').attr('disabled',true);
					$("#id_CPDest").prop("readonly",true);
					$("#id_CPOrig").prop("readonly",true);
				}
            },

            });
			$('#id_IDTransportista').on('change',function () {
				if(document.getElementById("id_IDTransportista").value != "")
				{
					$.ajax({
			            type: 'GET',
			            url: "/costeo/loadRutas/"+document.getElementById("id_IDTransportista").value+"/",
			            success: function (data) {
			                var ruta= document.getElementById('id_IDRuta');
			                $(ruta).empty();
			                $(ruta).append($('<option>').text("Select").attr('value', ''));
			                $.each(data, function (i, value) {
			                    $(ruta).append($('<option>').text(value.fields.NombreRuta).attr('value', value.pk));
			                });
			                if(update==1)
				    		{
				    			$(document.getElementById('id_IDRuta')).val(route).change();
				    			$('#id_IDRuta').attr('disabled',true);
				    		}
			            },
			        });
				}
				else
				{
					$(document.getElementById('id_IDRuta')).empty();
					$(document.getElementById('id_IDRuta')).append($('<option>').text("").attr('value', ""));
				}
			});
			$('#id_IDRuta').on('change',function () {

				if(document.getElementById("id_IDRuta").value != "")
				{
					$.ajax({
			            type: 'GET',
			            url: "/costeo/getRuta/"+document.getElementById("id_IDRuta").value+"/",
			            success: function (data) {
			                var km= document.getElementById('id_Kilometraje');
			                var tipo= document.getElementById('id_Tipo');
			                $(km).val(data[0].fields.Kilometros);
			                $(document.getElementById('casetaSingleId')).val(data[0].fields.Casetas);
			                $(document.getElementById('kmSencilloId')).val(data[0].fields.Kilometros);
			                $(document.getElementById('id_CPOrig')).val(data[0].fields.CPOrigen);
			                $(document.getElementById('id_CPDest')).val(data[0].fields.CPDestino);
			                filltables();
			                CalculaCosteo();
			                if(data[0].fields.ViajeRedondo==false)
			                	$(tipo).val("Sencillo")
			                else
			                	$(tipo).val("Redondo")
			            },

			        });

				}
				else
				{
					$(document.getElementById('id_Kilometraje')).val("");
					$(document.getElementById('id_Tipo')).val("");
					$(document.getElementById('id_CPOrig')).val("");
			        $(document.getElementById('id_CPDest')).val("");
				}
			});
			$('#id_Kilometraje').on('change',function () {
				$(document.getElementById('kmSencilloId')).val($(document.getElementById('id_Kilometraje')).val());
				CalculaCosteo();
				filltables();
			});
			$('#id_MopPor').on('change',function () {
				if(Number($(document.getElementById('id_MopPor')).val())<=14)
				{
					$(document.getElementById('id_MopPor')).val(15);
					CalculaCosteo();
					filltables();
				}
				else
				{
				CalculaCosteo();
				filltables();
				}

			});
			function clickcell(tdname,hiddenName)
			{
				changecellvar="false";
				hiddenName="'"+hiddenName+"'";
				tdnameAux="'"+tdname+"'";
				value='this.value';
				if(document.getElementById(tdname).innerHTML != '<input type="text" onkeypress="editrow(event,'+hiddenName+','+value+','+tdnameAux+')" class="form-control input-small" value="">')
				{
					changecellvar=tdname;
					document.getElementById(tdname).innerHTML='<input type="text" onkeypress="editrow(event,'+hiddenName+','+value+','+tdnameAux+')" class="form-control input-small" value="">';
				}

			}
			function editrow(e,hiddenName,value,tdname)
			{
			    if(e.which == '13')
			    {
			    	if(value!='')
			    	{
				    	$(document.getElementById(hiddenName)).val(value);
				    	document.getElementById(tdname).innerHTML='';
				    	CalculaCosteo();
						filltables();
						tdname="false";
					}
					else
					{
						document.getElementById(tdname).innerHTML=$(document.getElementById(hiddenName)).val();
					}

			    }
			}