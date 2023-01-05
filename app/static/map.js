const attribution =
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const map = L.map("map");
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: attribution,
}).addTo(map);
const records = JSON.parse(document.getElementById("records-data").textContent);
let feature = L.geoJSON(records).addTo(map);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });


