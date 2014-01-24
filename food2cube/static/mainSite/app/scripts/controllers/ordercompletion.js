'use strict';

angular.module('food2cubeApp')
  .controller('OrderCompletionCtrl', ['$log','$scope', '$http','$location', '$routeParams',
        function ($log,$scope, $http,$location, $routeParams)
        {
            //$scope.option = $location.search('option');
            //$log.info($scope.option);

            if ($routeParams.option!= null) {
                $scope.option = $routeParams.option;
                $log.info($routeParams.option);
            }

        }
    ]);

