Satellatte is a simple app to test Google AppEngine's geolocation headers. It automatically detects your location (city, region, country, lat/lon pair) and shows it in a marker in a full-screen map.

You can see it in action here: http://satellatte.appspot.com

NOTES
-----

* If you want to know more about these geolocation headers you can check the [official documentation](https://developers.google.com/appengine/docs/python/runtime#Request_Headers).

* The interactive map is handled by [MapBox's Wax](http://mapbox.com/wax) and [CloudMade's Leaflet](http://leaflet.cloudmade.com).

* The tiles are based on the beautiful [MapBox Streets](http://mapbox.com/maps) and are hosted by MapBox.

* Your location is stored with the sole purpose of showing a "recent visits" box. You can get the data from [this URL](http://satellatte.appspot.com/visitors.js).

* If you make changes to satellatte.js you need to re-minimize it with [Closure](https://developers.google.com/closure) or change the link in the HTML head.

Feel free to do whatever you want with this code under the terms of the BSD license below.

LICENSE
-------

Copyright (c) 2012, Antonio Zugaldia
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. All advertising materials mentioning features or use of this software
   must display the following acknowledgement:
   This product includes software developed by Antonio Zugaldia.

4. Neither the name of Antonio Zugaldia nor the
   names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
