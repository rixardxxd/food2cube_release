'use strict';

angular.module('food2cubeApp', ['ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/mainSite/app/views/main.html',
        controller: 'MainCtrl'
      })
      .when('/company/:companyName', {
        templateUrl: 'static/mainSite/app/views/company.html',
        controller: 'CompanyCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
