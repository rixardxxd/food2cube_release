'use strict';

angular.module('food2cubeApp')
  .controller('CompanyCtrl', ['$scope', 'Company', function ($scope, Company) {
    $scope.companies = Company.query();
  }]);
