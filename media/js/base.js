
function setup_map() {
    map = L.map('map').setView([0, 0], 4);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoibmVib2dlbyIsImEiOiJjajRvN2RraTYxdDgxMzJvNzdiNHZ2aHFwIn0.TneQlUn7VVs65h9auKZlKg'
    }).addTo(map);
    return map;
}

function create_marker(map, media_url, id, lat_string, lon_string, desc) {
    var lat = parseFloat(lat_string);
    var lon = parseFloat(lon_string);
    var icon = new L.Icon({
	iconUrl: media_url+'js/images/marker-icon.png',
	shadowUrl: media_url+'js/images/marker-shadow.png'
    });
    var marker = L.marker([lat, lon], {icon: icon});
    if (desc!=undefined) {
	marker.bindPopup('<div class="map-popup"><a href="incident/'+id+'">'+desc+'</a></div>');
    }
    marker.addTo(map);
};
