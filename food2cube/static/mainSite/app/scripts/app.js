'use strict';

angular.module('food2cubeApp', ['ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/company/:companyName', {
        templateUrl: 'views/company.html',
        controller: 'CompanyCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
