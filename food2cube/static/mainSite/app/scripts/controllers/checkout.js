'use strict';

angular.module('food2cubeApp')
  .controller('CheckoutCtrl', ['$scope', 'Checkout', '$http',
        function ($scope, Checkout, $http)
        {
            //In practise, $scope.items should be added in former page, not generated in service.
            $scope.items = Checkout.queryTestData();

            console.log("items = ");
            console.log($scope.items);

            $scope.doUpdateAmount = function(id, amount)
            {
                console.log("Update Item Amount : id="+id+" New Amount="+amount);
                Checkout.updateAmount($scope.items, id, amount);
                console.log("items = ");
                console.log($scope.items);
            }

        }
    ]);