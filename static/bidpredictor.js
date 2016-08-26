

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

	var average = document.getElementById("average_field").value;
	var std = document.getElementById("std_dev_field").value;
	var opening = document.getElementById("open_field").value;
	
	var request = gapi.client.ebaybidsendpoints.calculateClosing({'opening': opening, 'average': average, 'std': std});
	
	request.execute(BidInfoCallback);

}

function BidInfoCallback(response) {

	alert(response.msg);

}