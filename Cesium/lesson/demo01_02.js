 var viewer = new Cesium.Viewer('cesiumContainer', {
    infoBox: false,
    selectionIndicator: false,
    shadows: true,
    shouldAnimate: true,
});
var scene = viewer.scene;
scene.globe.depthTestAgainstTerrain = true;

if (!scene.sampleHeightSupported) {
    window.alert("This browser does not support sampleHeight.");
}

var longitude = -2.1480545852753163;
var latitude = 0.7688240036937101;
var range = 0.000002;
var duration = 4.0;

var entity = viewer.entities.add({
    position: Cesium.Cartesian3.fromRadians(longitude, latitude),
    model: {
        uri: "../data/models/GroundVehicle/GroundVehicle.glb",
    },
});

var point = viewer.entities.add({
    position: new Cesium.CallbackProperty(updatePosition, false),
    point: {
        pixelSize: 10,
        color: Cesium.Color.YELLOW,
        disableDepthTestDistance: Number.POSITIVE_INFINITY,
    },
    label: {
        show: false,
        showBackground: true,
        font: "14px monospace",
        horizontalOrigin: Cesium.HorizontalOrigin.LEFT,
        verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
        pixelOffset: new Cesium.Cartesian2(5, 5),
        disableDepthTestDistance: Number.POSITIVE_INFINITY,
    },
});

var objectsToExclude = [point];
var cartographic = new Cesium.Cartographic();

function updatePosition(time, result) {
    var offset = (time.secondsOfDay % duration) / duration;
    cartographic.longitude = longitude - range + offset * range * 2.0;
    cartographic.latitude = latitude;

    var height;
    if (scene.sampleHeightSupported) {
        height = scene.sampleHeight(cartographic, objectsToExclude);
    }

    if (Cesium.defined(height)) {
        cartographic.height = height;
        point.label.text = Math.abs(height).toFixed(2).toString() + " m";
        point.label.show = true;
    } else {
        cartographic.height = 0.0;
        point.label.show = false;
    }

    return Cesium.Cartographic.toCartesian(
        cartographic,
        Cesium.Ellipsoid.WGS84,
        result
    );
}
viewer.trackedEntity = entity;