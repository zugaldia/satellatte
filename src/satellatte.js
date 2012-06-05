/*
 * See: http://mapbox.com/hosting/api-embed/ and http://leaflet.cloudmade.com/
 */

function Satellatte(message_element) {
	var satellatte = {},
		url = 'http://api.tiles.mapbox.com/v3/mapbox.mapbox-streets.jsonp',
		message_id = "#" + message_element,
		zoom_out = 3,
		zoom_in = 11,
		map;
	
	satellatte.set_message = function(text) {
		$(message_id).text(text);
	}
	
	satellatte.map_setup = function(map_element) {
	    map = new L.Map(map_element).setView(new L.LatLng(0, 0), zoom_out);
	    wax.tilejson(url, function(tilejson) {
	        map.addLayer(new wax.leaf.connector(tilejson));
	        satellatte.set_message('Map loaded.');
	    });
	}
	
	satellatte.marker = function(latitude, longitude, text, recent) {
		satellatte.set_message('Acquiring location...');
		
		// Fake timeout
		window.setTimeout(function() {
			map.panTo(new L.LatLng(latitude, longitude));
	    	map.setZoom(zoom_in);
	    	
	    	// Marker
	        var marker = new L.Marker(new L.LatLng(latitude, longitude));
	        map.addLayer(marker);
	        marker.bindPopup(text).openPopup();
	        
	        satellatte.set_message('Done.');
	        satellatte.recent_visits(recent);
		}, 3000);
	}
	
	satellatte.recent_visits = function(recent) {
		if (recent != '') {
			satellatte.set_message('We recently had visitors from: ' + recent);
		}
	}
	
	return satellatte;
}
