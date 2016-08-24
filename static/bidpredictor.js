

function init() {

	var rootpath = "//" + window.location.host + "/_ah/api";

	gapi.client.load('ebaybidsendpoints', 'v1', loadCallback, rootpath);

}

function loadCallback() {

	enableButton()

}

function enableButton() {

	button = document.getElementById("submit_values");
	button.onclick = function(){BidInfo()};
	button.value = "Predict closing price";

}

function BidInfo() {

	var average = document.getElementById("average_field");
	var std = document.getElementById("std_dev_field");
	var opening = document.getElementById("open_field");
	
	var request = gapi.client.ebaybidsendpoints.calculateClosing({'average': average, 'std' : std, 'opening' : opening});
	request.execute(BidInfoCallback);

}

function BidInfoCallback(response) {

	alert(response.msg);
	
}