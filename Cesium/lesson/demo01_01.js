var viewer = new Cesium.Viewer("cesiumContainer"); 
 var pinBuilder = new Cesium.PinBuilder();

    var 锦江区 = viewer.entities.add({
        name : '锦江区',
        position : Cesium.Cartesian3.fromDegrees(104.07, 30.67),
        billboard : {
            image : pinBuilder.fromColor(Cesium.Color.ROYALBLUE, 48).toDataURL(),
            verticalOrigin : Cesium.VerticalOrigin.BOTTOM
        }
    });

    var 青羊区 = viewer.entities.add({
        name : '青羊区',
        position : Cesium.Cartesian3.fromDegrees(104.05,30.68),
        billboard : {
            image : pinBuilder.fromText('青羊区', Cesium.Color.BLACK, 48).toDataURL(),
            verticalOrigin : Cesium.VerticalOrigin.BOTTOM
        }
    });

    var url = Cesium.buildModuleUrl('Assets/Textures/maki/grocery.png');
    var 成华区 = Cesium.when(pinBuilder.fromUrl(url, Cesium.Color.GREEN, 48), function(canvas) {
        return viewer.entities.add({
            name : '成华区',
            position : Cesium.Cartesian3.fromDegrees(104.10, 30.67),
            billboard : {
                image : canvas.toDataURL(),
                verticalOrigin : Cesium.VerticalOrigin.BOTTOM
            }
        });
    });

    //Create a red pin representing a hospital from the maki icon set.
    var 华西医院 = Cesium.when(pinBuilder.fromMakiIconId('hospital', Cesium.Color.RED, 48), function(canvas) {
        return viewer.entities.add({
            name : '华西医院',
            position : Cesium.Cartesian3.fromDegrees(104.30, 30.9211275),
            billboard : {
                image : canvas.toDataURL(),
                verticalOrigin : Cesium.VerticalOrigin.BOTTOM
            }
        });
    });

    //add the lable 
    function offsetByDistance() {
        Sandcastle.declare(offsetByDistance);
            viewer.entities.add({
                position : Cesium.Cartesian3.fromDegrees(104.08,30.67),
                label : {
                    text : 'chengdu',
                    font : '20px sans-serif',
                    showBackground : true,
                    horizontalOrigin : Cesium.HorizontalOrigin.CENTER,
                    pixelOffsetScaleByDistance : new Cesium.NearFarScalar(1.5e2, 3.0, 1.5e7, 0.5)
                }
            });
   //    viewer.zoomTo(viewer.entities);
    }

    function fadeByDistance() {
        Sandcastle.declare(fadeByDistance);
        viewer.entities.add({
            position : Cesium.Cartesian3.fromDegrees(104.08,30.67),
            label : {
                text : 'Chengdu',
               // showBackground : true,
                translucencyByDistance : new Cesium.NearFarScalar(1.5e2, 1.0, 1.5e8, 0.0)
            }
        });
        viewer.zoomTo(viewer.entities);

    }

    function scaleByDistance() {
        Sandcastle.declare(scaleByDistance);

        viewer.entities.add({
            position : Cesium.Cartesian3.fromDegrees(104.08,30.67),
            label : {
                text : 'chengdu',
              //  showBackground : true,
                scaleByDistance : new Cesium.NearFarScalar(1.5e2, 2.0, 1.5e7, 0.0)
            }
        });
     //   viewer.zoomTo(viewer.entities);

    }

    function setRightToLeft() {
        Sandcastle.declare(setRightToLeft);
        Cesium.Label.enableRightToLeftDetection = true; //Only needs to be set once at the beginning of the application.
        viewer.entities.add({
         //  showBackground : true,
            position : Cesium.Cartesian3.fromDegrees(104.08,30.67),
            label : {
                text : '成都 都城',
                scaleByDistance : new Cesium.NearFarScalar(1.5e2, 2.0, 1.5e7, 0.0)
            }
        });
         // viewer.zoomTo(viewer.entities);
    }
 
//menus
    Sandcastle.addToolbarMenu([{
        text : 'Offset label by distance',
        onselect : function() {
            offsetByDistance();
            Sandcastle.highlight(offsetByDistance);
        }
    }, {
        text : 'Fade label by distance',
        onselect : function() {
            fadeByDistance();
            Sandcastle.highlight(fadeByDistance);
        }
    }, {
        text : 'Scale label by distance',
        onselect : function() {
            scaleByDistance();
            Sandcastle.highlight(scaleByDistance);
        }
    }, {
        text : 'Set label with right-to-left language',
        onselect : function() {
            setRightToLeft();
            Sandcastle.highlight(setRightToLeft);
        }
    }]);


//Since some of the pins are created asynchronously, wait for them all to load before zooming/
    Cesium.when.all([锦江区, 青羊区, 成华区, 华西医院], function(pins){
        viewer.zoomTo(pins);
    });

    Sandcastle.reset = function() {
   //    viewer.entities.removeAll();
    };



 
