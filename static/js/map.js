$(document).ready(function(){
    var mymap = L.map('map').setView([40.7128, -74.0059], 13);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZ3JlZ2R1dGNoZXIiLCJhIjoiY2o0OTRsc21wMGtmcTMzbndhenEyM3ZleiJ9.RNOyza98KMzFaColycxWLA', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);

    function onMapClick(e) {
        alert("You clicked the map at " + e.latlng);
    }

    mymap.on('click', onMapClick);
});

