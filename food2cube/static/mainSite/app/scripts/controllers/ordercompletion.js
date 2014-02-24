'use strict';

angular.module('food2cubeApp')
  .controller('OrderCompletionCtrl', ['$log','$scope', '$http','$location', '$routeParams','DeliveryAddress',
        function ($log,$scope, $http,$location, $routeParams,DeliveryAddress)
        {
            //$scope.option = $location.search('option');
            //$log.info($scope.option);

            if ($routeParams.firstName!= null) {
                $scope.firstName = $routeParams.firstName;
                $log.info($routeParams.firstName);

            }

            if ($routeParams.lastName!= null) {
                $scope.lastName = $routeParams.lastName;
                $log.info($routeParams.lastName);

            }

            if ($routeParams.email!= null) {
                $scope.email = $routeParams.email;
                $log.info($routeParams.email);

            }

            if ($routeParams.phone!= null) {
                $scope.phone = $routeParams.phone;
                $log.info($routeParams.phone);

            }

        }
    ]);

