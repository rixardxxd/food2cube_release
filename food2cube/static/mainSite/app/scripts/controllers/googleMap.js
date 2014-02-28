'use strict';

angular.module('food2cubeApp')
  .controller('googleMapCtrl', ['$scope', function ($scope) {
        $scope.map = {
            center: {
                latitude: 37.418591,
                longitude: -121.919399
            },
            zoom: 4
        };
  }]);


