
function setup_map() {
    var centre_lat=0.417;
    var centre_lon=37.781;
    var initial_zoom=6;
    map = L.map('map').setView([centre_lat, centre_lon], initial_zoom);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoibmVib2dlbyIsImEiOiJjajRvN2RraTYxdDgxMzJvNzdiNHZ2aHFwIn0.TneQlUn7VVs65h9auKZlKg'
    }).addTo(map);
    return map;
}

function create_marker(map, id, lat_string, lon_string, desc) {
    var lat = parseFloat(lat_string);
    var lon = parseFloat(lon_string);
    var icon = new L.Icon({
	iconUrl: media_url+'js/images/marker-icon.png',
	shadowUrl: media_url+'js/images/marker-shadow.png'
    });
    var marker = L.marker([lat, lon], {icon: icon});
    if (desc!=undefined) {
	console.log('<div class="map-popup"><a href="/incident/'+id+'">'+desc+'</a></div>')
	marker.bindPopup('<div class="map-popup"><a href="/incident/'+id+'">'+desc+'</a></div>');
    }
    marker.addTo(map);
};

var clicked=false;
var marker=false;
var media_url=false;

function do_draggable_marker(map) {
    map.on('click',
	   function (e) {
	       if (!clicked) {
		   clicked=true; 
		   var pos = e.latlng;
		   document.getElementById("id_lat").value = pos.lat; 
		   document.getElementById("id_lon").value = pos.lng;		 

		   var icon = new L.Icon({
		       iconUrl: media_url+'js/images/marker-icon.png',
		       shadowUrl: media_url+'js/images/marker-shadow.png'
		   });		   
		   marker = L.marker(pos, {draggable: true, icon: icon});
		   marker.on('drag', function (e) {
		       document.getElementById("id_lat").value = e.latlng.lat; 
		       document.getElementById("id_lon").value = e.latlng.lng;		 
		   });
		   marker.on('click', L.DomEvent.stopPropagation);
		   marker.addTo(map);
               }
	   });
}


function getLocationConstant() {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(onGeoSuccess,onGeoError);  
    } else {
        alert("Your browser or device doesn't support Geolocation");
    }
}

// If we have a successful location update
function onGeoSuccess(event) {
    update_pos(event.coords.latitude,event.coords.longitude);
}

// If something has gone wrong with the geolocation request
function onGeoError(event) {
    //alert("Error code " + event.code + ". " + event.message);
    var latLong;
    $.getJSON("http://ipinfo.io", function(ipinfo){
	console.log("Found location ["+ipinfo.loc+"] by ipinfo.io");
	latLong = ipinfo.loc.split(",");
	update_pos(latLong[0],latLong[1])
    });
}

function update_pos(lat,lon) {
    document.getElementById("id_lat").value = lat; 
    document.getElementById("id_lon").value = lon;
    map.setView(new L.LatLng(lat,lon), 8);
    if (marker) {
	var newLatLng = new L.LatLng(lat,lon);
	marker.setLatLng(newLatLng); 
    } else {
	var icon = new L.Icon({
	    iconUrl: media_url+'js/images/marker-icon.png',
	    shadowUrl: media_url+'js/images/marker-shadow.png'
	});		   
	marker = L.marker(new L.LatLng(lat,lon), {draggable: true, icon: icon});
	marker.on('drag', function (e) {
	    document.getElementById("id_lat").value = e.latlng.lat; 
	    document.getElementById("id_lon").value = e.latlng.lng;		 
	});
	marker.on('click', L.DomEvent.stopPropagation);
	marker.addTo(map);
    }
}
