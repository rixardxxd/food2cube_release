'use strict';

angular.module('food2cubeApp')
  .controller('CheckoutCtrl', ['$scope', 'Company', function ($scope, Company)
  {
    $scope.companies = Company.query();






  }]);
