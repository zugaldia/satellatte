var data = {
	"type": "FeatureCollection",
	"features": [
		{% for visit in all %}
			{ "type": "Feature",
  		  	  "geometry": { "type": "Point", "coordinates": [{{ visit.longitude }}, {{ visit.latitude }}] },
  		  	  "properties": { "name" : "{{ visit.text|escape }}" } },	
		{% endfor %}
	]
};
