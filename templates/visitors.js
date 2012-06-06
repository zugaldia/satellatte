var data = {
	"type": "FeatureCollection",
	"features": [
		{% for visit in visits %}
			{ "type": "Feature",
  		  	  "geometry": { "type": "Point", "coordinates": [{{ visit.lon }}, {{ visit.lat }}] },
  		  	  "properties": { "name" : "{{ visit.name|escape }} on {{ visit.date|escape }}" } },	
		{% endfor %}
	]
};
