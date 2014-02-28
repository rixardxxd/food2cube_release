'use strict';

angular.module('food2cubeApp')
  .controller('googleMapCtrl', ['$scope', function ($scope) {
        $scope.map = {
            center: {
                latitude: -121.9191404,
                longitude: 37.4137296
            },
            zoom: 4
        };
  }]);


