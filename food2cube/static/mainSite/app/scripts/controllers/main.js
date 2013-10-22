'use strict';

angular.module('food2cubeApp')
  .controller('MainCtrl', ['$scope', 'Company', function ($scope, Company) {
    $scope.companies = Company.query();
  }]);
