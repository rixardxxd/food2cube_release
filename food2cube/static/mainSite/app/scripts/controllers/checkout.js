'use strict';

angular.module('food2cubeApp')
  .controller('CheckoutCtrl', ['$scope', 'Checkout',
        function ($scope, Checkout)
        {
            $scope.items = Checkout.query();


        }
    ]);