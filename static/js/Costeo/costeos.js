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
	$(document.getElementById('CombustibleId')).val(Math.round(($(document.getElementById('kmSencilloId')).val()/$(document.getElementById('rendimiento')).val())*$(document.getElementById('dieselSinIvaId')).val()));
	$(document.getElementById('CasetasId')).val(Math.round($(document.getElementById('casetaSingleId')).val()/1.16));
	$(document.getElementById('OperadorId')).val(Math.round($(document.getElementById('kmSencilloId')).val()*$(document.getElementById('operadorId')).val()));
	var res=roundToTwo(Number($(document.getElementById('CombustibleId')).val())
	+Number($(document.getElementById('CasetasId')).val())
	+Number($(document.getElementById('OperadorId')).val()));
	$(document.getElementById('SubTotalId')).val(res);
	$(document.getElementById('MttoUnidadId')).val(Math.round($(document.getElementById('kmSencilloId')).val()*$(document.getElementById('mttoUnidadXkmId')).val()));
	$(document.getElementById('LlantasUnidadId')).val(Math.round($(document.getElementById('kmSencilloId')).val()*$(document.getElementById('llantasId')).val()));
	$(document.getElementById('GPSId')).val(Math.round($(document.getElementById('kmSencilloId')).val()*(Number($(document.getElementById('rentaGPSId')).val()/$(document.getElementById('kmsMaximoId')).val()))));
	$(document.getElementById('SeguroId')).val(Math.round($(document.getElementById('kmSencilloId')).val()*(Number($(document.getElementById('seguroId')).val()/$(document.getElementById('kmsMaximoId')).val()))));
	$(document.getElementById('PlacasTenenciaCostId')).val(Math.round($(document.getElementById('kmSencilloId')).val()*(Number($(document.getElementById('placasTenenciaId')).val()/$(document.getElementById('kmsMaximoId')).val()))));
	res=Number($(document.getElementById('MttoUnidadId')).val())
	+Number($(document.getElementById('LlantasUnidadId')).val())
	+Number($(document.getElementById('GPSId')).val())
	+Number($(document.getElementById('SeguroId')).val())
	+Number($(document.getElementById('PlacasTenenciaCostId')).val());
	$(document.getElementById('SubTotal2Id')).val(roundToTwo(res));
	res=roundToTwo(Number($(document.getElementById('SubTotalId')).val())+Number($(document.getElementById('SubTotal2Id')).val()));
	$(document.getElementById('AdmvoId')).val(Math.round(res*($(document.getElementById('admvoId')).val()/100)));
	$(document.getElementById('FinancierosId')).val(Math.round(res*($(document.getElementById('financierosId')).val()/100)));
	$(document.getElementById('DeprUnidadId')).val(Math.round($(document.getElementById('depTractoId')).val()*$(document.getElementById('kmSencilloId')).val()));
	$(document.getElementById('DeprRemolqueId')).val(Math.round($(document.getElementById('depCajaId')).val()*$(document.getElementById('kmSencilloId')).val()*$(document.getElementById('unidadId')).val()));

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
	$(document.getElementById('id_TotalCostosAux')).val("$"+parseFloat(roundToTwo(res)).toLocaleString("en-US"));
	document.getElementById('id_TotalCostosP').innerHTML = "$"+parseFloat(roundToTwo(res)).toLocaleString("en-US");
	if($(document.getElementById('id_MopPor')).val()!=0 && $(document.getElementById('id_MopPor')).val()!=""){
		res=Number($(document.getElementById('id_TotalCostos')).val())*($(document.getElementById('id_MopPor')).val()/100)
		$(document.getElementById('id_MopAux')).val(convertidorDivisaMXN(roundToTwo(res)));
		$(document.getElementById('id_Mop')).val(roundToTwo(res));
	}
	else{
		document.getElementById("id_MopPor").value = 15;
		document.getElementById("id_MopAux").value = convertidorDivisaMXN(0);
		document.getElementById("id_Mop").value = 0;
	}

	if(document.getElementById('id_FactorAjustePor').value !=0 && document.getElementById('id_FactorAjustePor').value!="")
	{
		res=Number($(document.getElementById('id_TotalCostos')).val())*($(document.getElementById('id_FactorAjustePor')).val()/100)
		$(document.getElementById('id_FactorAjusteAux')).val(convertidorDivisaMXN(roundToTwo(res)));
		$(document.getElementById('id_FactorAjuste')).val(roundToTwo(res));
	}
	else{
		document.getElementById("id_FactorAjustePor").value = 0;
		document.getElementById("id_FactorAjusteAux").value = convertidorDivisaMXN(0);
		document.getElementById("id_FactorAjuste").value = 0;
	}
	res=Number($(document.getElementById('id_TotalCostos')).val())+Number($(document.getElementById('id_Mop')).val())+Number($(document.getElementById('id_FactorAjuste')).val())
	$(document.getElementById('id_TotalTransportista')).val(roundToTwo(res));
	$(document.getElementById('id_TotalTransportistaAux')).val("$"+parseFloat(roundToTwo(res)).toLocaleString("en-US"));
}

function filltables()
{
	document.getElementById('tdMeses').innerHTML = convertidorFormatoNum($(document.getElementById('mesesId')).val());
	document.getElementById('tdCostoUnidad').innerHTML = convertidorDivisaMXN($(document.getElementById('costosUnidadId')).val());
	document.getElementById('tdUnidad').innerHTML = ""+ convertidorDivisaMXN(roundToTwo($(document.getElementById('costosUnidadId')).val()/ $(document.getElementById('mesesId')).val()))+"";
	document.getElementById('tdCostosCaja').innerHTML = convertidorDivisaMXN($(document.getElementById('costosCajaId')).val());
	document.getElementById('tdCaja').innerHTML = ""+convertidorDivisaMXN(roundToTwo($(document.getElementById('costosCajaId')).val()/$(document.getElementById('mesesId')).val()))+"";
	document.getElementById('tdViajesMes').innerHTML = convertidorFormatoNum($(document.getElementById('viajesMesId')).val());
	document.getElementById('tdKmsMesXunidad').innerHTML = convertidorFormatoNum($(document.getElementById('kmsMesXunidadId')).val());
	document.getElementById('tdkmsMaximo').innerHTML = convertidorFormatoNum($(document.getElementById('kmsMaximoId')).val());
	document.getElementById('tdKunidad').innerHTML = convertidorFormatoNum($(document.getElementById('unidadId')).val());
	document.getElementById('tdKmSencillo').innerHTML = convertidorFormatoNum($(document.getElementById('kmSencilloId')).val());
	document.getElementById('tdKmMensuales').innerHTML = convertidorFormatoNum($(document.getElementById('kmMensualesId')).val());
	document.getElementById('tdCasetaSingle').innerHTML = convertidorDivisaMXN($(document.getElementById('casetaSingleId')).val());
	document.getElementById('tdRendimiento').innerHTML = convertidorFormatoNum($(document.getElementById('rendimiento')).val());
	document.getElementById('tdDiesel').innerHTML = convertidorDivisaMXN($(document.getElementById('dieselId')).val());
	document.getElementById('tdDieselSinIva').innerHTML = convertidorDivisaMXN($(document.getElementById('dieselSinIvaId')).val());
	document.getElementById('tddepTracto').innerHTML = convertidorDivisaMXN($(document.getElementById('depTractoId')).val());
	document.getElementById('tddepCaja').innerHTML = convertidorDivisaMXN($(document.getElementById('depCajaId')).val());
	document.getElementById('tdrentaGPS').innerHTML = convertidorDivisaMXN($(document.getElementById('rentaGPSId')).val());
	document.getElementById('tdGPS').innerHTML = ""+convertidorFormatoNum(roundToTwo(($(document.getElementById('rentaGPSId')).val()/Number($(document.getElementById('kmsMaximoId')).val()))))+"";
	document.getElementById('tdplacasTenencia').innerHTML = convertidorDivisaMXN($(document.getElementById('placasTenenciaId')).val());
	document.getElementById('tdPlacas').innerHTML = ""+convertidorFormatoNum(roundToTwo(($(document.getElementById('placasTenenciaId')).val()/Number($(document.getElementById('kmsMaximoId')).val()))))+"";
	document.getElementById('tdseguro').innerHTML = convertidorDivisaMXN($(document.getElementById('seguroId')).val());
	document.getElementById('tdSegurokm').innerHTML = ""+convertidorFormatoNum(roundToTwo(($(document.getElementById('seguroId')).val()/Number($(document.getElementById('kmsMaximoId')).val()))))+"";
	document.getElementById('tdAdmvo').innerHTML = convertidorFormatoNum($(document.getElementById('admvoId')).val());
	document.getElementById('tdFinancieros').innerHTML = convertidorFormatoNum($(document.getElementById('financierosId')).val());
	document.getElementById('tdMtto').innerHTML = convertidorFormatoNum($(document.getElementById('mttoUnidadXkmId')).val());
	document.getElementById('tdLlantas').innerHTML = convertidorFormatoNum($(document.getElementById('llantasId')).val());
	document.getElementById('tdOperador').innerHTML = convertidorFormatoNum($(document.getElementById('operadorId')).val());
	document.getElementById('tdCombustible').innerHTML = convertidorDivisaMXN($(document.getElementById('CombustibleId')).val());
	document.getElementById('tdCasetas').innerHTML = convertidorDivisaMXN($(document.getElementById('CasetasId')).val());
	document.getElementById('tdOperadorOperativo').innerHTML = convertidorDivisaMXN($(document.getElementById('OperadorId')).val());
	document.getElementById('tdSubtotal1').innerHTML = convertidorDivisaMXN($(document.getElementById('SubTotalId')).val());
	document.getElementById('tdMttoUnidad').innerHTML = convertidorDivisaMXN($(document.getElementById('MttoUnidadId')).val());
	document.getElementById('tdLlantasUnidad').innerHTML = convertidorDivisaMXN($(document.getElementById('LlantasUnidadId')).val());
	document.getElementById('tdGPSCostos').innerHTML = convertidorDivisaMXN($(document.getElementById('GPSId')).val());
	document.getElementById('tdSeguroCostos').innerHTML = convertidorDivisaMXN($(document.getElementById('SeguroId')).val());
	document.getElementById('tdPlacasTenencia').innerHTML = convertidorDivisaMXN($(document.getElementById('PlacasTenenciaCostId')).val());
	document.getElementById('tdSubTotal2').innerHTML = convertidorDivisaMXN($(document.getElementById('SubTotal2Id')).val());
	document.getElementById('tdAdmvoCostos').innerHTML = convertidorDivisaMXN($(document.getElementById('AdmvoId')).val());
	document.getElementById('tdFinancierosCostos').innerHTML = convertidorDivisaMXN($(document.getElementById('FinancierosId')).val());
	document.getElementById('tdDeprUnidad').innerHTML = convertidorDivisaMXN($(document.getElementById('DeprUnidadId')).val());
	document.getElementById('tdDeprRemolque').innerHTML = convertidorDivisaMXN($(document.getElementById('DeprRemolqueId')).val());
	document.getElementById('tdSubtotal3').innerHTML = convertidorDivisaMXN($(document.getElementById('SubTotal3Id')).val());

	if($(document.getElementById('id_TotalCostos')).val()!="")
	{
		document.getElementById('tdComb').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('CombustibleId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdCast').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('CasetasId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdOper').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('OperadorId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdsub1').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('SubTotalId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdMttoUnidadPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('MttoUnidadId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdLlantasUnidadPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('LlantasUnidadId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdGPSCostosPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('GPSId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdSeguroCostosPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('SeguroId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdPlacasTenenciaPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('PlacasTenenciaCostId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdSubTotal2Por').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('SubTotal2Id')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdAdmvoCostosPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('AdmvoId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdFinancierosCostosPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('FinancierosId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdDeprUnidadPor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('DeprUnidadId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdDeprRemolquePor').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('DeprRemolqueId')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
		document.getElementById('tdSubtotal3Por').innerHTML = convertidorFormatoNum(Math.round((Number($(document.getElementById('SubTotal3Id')).val())/Number($(document.getElementById('id_TotalCostos')).val()))*100))+'%';
	}
}

function roundToTwo(num) {
	var dec=2;
	if ((typeof num !== 'number') || (typeof dec !== 'number'))
	return false;

		var num_sign = num >= 0 ? 1 : -1;

		return (Math.round((num*Math.pow(10,dec))+(num_sign*0.0001))/Math.pow(10,dec)).toFixed(dec);
}

$('#id_CasetasAux').on('change',function () {
	document.getElementById("tdCasetaSingle").value = convertidorFormatoNum(document.getElementById("id_Casetas").value);
	document.getElementById("casetaSingleId").value = document.getElementById("id_Casetas").value;
	if(document.getElementById('kmSencilloId').value != "" && document.getElementById('id_Casetas').value != "" && document.getElementById('id_Kilometros').value != ""){
		CalculaCosteo();
		filltables();
	}
});

$('#id_KilometrosAux').on('change',function () {
	if(document.getElementById("id_ViajeRedondo").checked == true){
		$(document.getElementById('kmSencilloId')).val(document.getElementById("id_Kilometros").value*2);
		$(document.getElementById('casetaSingleId')).val(document.getElementById('id_Casetas').value*2);
	}else{
		$(document.getElementById('kmSencilloId')).val(document.getElementById("id_Kilometros").value);
		$(document.getElementById('casetaSingleId')).val(document.getElementById('id_Casetas').value);
	}

	if(document.getElementById('kmSencilloId').value != "" && document.getElementById('id_Casetas').value != "" && document.getElementById('id_Kilometros').value != ""){
		CalculaCosteo();
		filltables();
	}
});

$('#id_MopPor').on('change',function (){
	if(document.getElementById('kmSencilloId').value != "" && document.getElementById('id_Casetas').value != "" && document.getElementById('id_Kilometros').value != ""){
		CalculaCosteo();
		filltables();
	}
});

$('#id_FactorAjustePor').on('change',function () {
	if(document.getElementById('kmSencilloId').value != "" && document.getElementById('id_Casetas').value != "" && document.getElementById('id_Kilometros').value != ""){
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
	if(document.getElementById(tdname).innerHTML != '<input type="text" id="inputG" onkeydown="return formatoNumD(this,event);" onkeyup="formatoNumU(this,event,'+hiddenName+','+tdnameAux+');" class="form-control input-small" value="">')
	{
		changecellvar=tdname;
		document.getElementById(tdname).innerHTML='<input type="text" id="inputG" onkeydown="return formatoNumD(this,event);" onkeyup="formatoNumU(this,event,'+hiddenName+','+tdnameAux+');" class="form-control input-small" value="">';
	}
}

function formatoNumD(e, event) {
	var texto = document.getElementById(e.id).value;
	var simbolo = event.key;
	var cadena = texto+simbolo;
	cadena = cadena.replace(/\$/g, "");
	cadena = cadena.replace(/,/g, "");

	if(event.key == "Backspace"){
		return true;
	}

	var RE = /^([0-9]+\.?[0-9]{0,2})$/;
	if (RE.test(cadena)){
		var respuesta =(cadena+"").split(".")[1];
		if(simbolo == "." && respuesta == ""){
		   cadena = parseFloat(cadena).toLocaleString("en-US");
		   cadena += ".";
		}
		else if(simbolo == 0 && respuesta == 0){
		   cadena = parseFloat(cadena).toLocaleString("en-US");
		   cadena += ".0";
		}
		else{
		   cadena = parseFloat(cadena).toLocaleString("en-US");
		}
		e.value = cadena;
		return false;
	}
	else{
		return false;
	}
}

function formatoNumU(e,event,hiddenName,tdname){
	var cadena = e.value;
	cadena = cadena.replace(/\$/g, "");
	cadena = cadena.replace(/,/g, "");

	var RE = /^([0-9]+\.?[0-9]{0,2})$/;
	if (RE.test(cadena)){
		var cadenaAux = cadena;
		var respuesta =(cadena+"").split(".")[1];
		
		if(respuesta == ""){
			cadena = parseFloat(cadena).toLocaleString("en-US");
			cadena += ".";
		}
		else if(respuesta == 0){
			cadena = parseFloat(cadena).toLocaleString("en-US");
			cadena += ".0";
		}
		else{
			cadena = parseFloat(cadena).toLocaleString("en-US");
		}

		e.value = cadena;
		
		if(event.which == '13')
		{
			if(cadenaAux!='')
			{
				$(document.getElementById(hiddenName)).val(cadenaAux);
				document.getElementById(tdname).innerHTML='';
				CalculaCosteo();
				filltables();
				tdname="false";
			}
	
		}
		return false;
	}

	if(event.which == 13){
		if(cadena==""){
			document.getElementById(tdname).innerHTML= convertidorFormatoNum($(document.getElementById(hiddenName)).val());
		}
	}
}

function convertidorFormatoNum(cadena){
	if(cadena==""){
		cadena = 0;
	}
	cadena = parseFloat(cadena).toLocaleString("en-US");
	return cadena;
}

function convertidorDivisaMXN(cadena){
	if(cadena==""){
		cadena = 0;
	}
	cadena = "$"+parseFloat(cadena).toLocaleString("en-US");
	return cadena;
}