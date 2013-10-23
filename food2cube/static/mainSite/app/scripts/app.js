'use strict';

angular.module('food2cubeApp', ['ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'http://localhost:5000/static/mainSite/app/views/main.html',
        controller: 'MainCtrl'
      })
      .when('/company/:companyName', {
        templateUrl: 'http://localhost:5000/static/mainSite/app/views/company.html',
        controller: 'CompanyCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
