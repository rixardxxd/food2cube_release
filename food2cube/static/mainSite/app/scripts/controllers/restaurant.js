'use strict';

angular.module('food2cubeApp')
    .controller('RestaurantCtrl', ['$scope', 'Restaurant', function ($scope, Restaurant) {
    $scope.restaurants = Restaurant.query();

  }]);
