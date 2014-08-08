var geocoder;
var map;
var infowindow = new google.maps.InfoWindow();

function initialize() {
	geocoder = new google.maps.Geocoder();
    var mapOptions = {
        center: new google.maps.LatLng(39.5,-98.35),
        zoom: 4,
        styles: mapstypes
    };
    window.map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

	var funcs = [];
	
	function createfunc(t) {
		return function(results, status) {
			if (status == google.maps.GeocoderStatus.OK) {
				addMarker(results[0].geometry.location, t);
		  	}
      	};
	}

	for (var i = 0; i < tweets.length; i++) {
		var t = tweets[i];
		funcs[i] = createfunc(t);
	}

    for (var i = 0; i < tweets.length; i++) {
        var t = tweets[i];
    	geocoder.geocode( { 'address': t.userlocation}, funcs[i]);
    }
}

function addMarker(location, t) {
    var contentString = '<div id="content">' +
        '<h1>' + t.username + '</h1>' +
        '<h2>' + t.time + '</h2>' +
        '<p>' + t.text + '</p></div>';

	var pinColor = "";
	if(t.sent == "pos") {
		var pinColor = "00CC33";
	} else if (t.sent == "neg") {
		var pinColor = "FE7569";
	}
	var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + 		pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34));
    var pinShadow = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_shadow",
        new google.maps.Size(40, 37),
        new google.maps.Point(0, 0),
        new google.maps.Point(12, 35));

    var marker = new google.maps.Marker({
        position: location,
        icon: pinImage,
        shadow: pinShadow,
        map: map,
        title: t.text,
        draggable: false
    });
    google.maps.event.addListener(marker, 'click', function() {
        infowindow.setContent(contentString);
        infowindow.open(window.map, marker);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);
