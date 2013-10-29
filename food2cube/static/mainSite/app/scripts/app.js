'use strict';

angular.module('food2cubeApp', ['ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
<<<<<<< HEAD
        templateUrl: 'http://localhost:5000/static/mainSite/app/views/main.html',
        controller: 'MainCtrl'
      })
      .when('/company/:companyName', {
        templateUrl: 'http://localhost:5000/static/mainSite/app/views/company.html',
=======
        templateUrl: 'static/mainSite/app/views/main.html',
        controller: 'MainCtrl'
      })
      .when('/company/:companyName', {
        templateUrl: 'static/mainSite/app/views/company.html',
>>>>>>> d8468662c29cb3dc85ec6de185a37c744d07368c
        controller: 'CompanyCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

/* TODO not sure if this is the correct place to add this code */
/*
$( document ).ready(function() {
    if('http://localhost:5000/#/company/1'==window.location.href){
	    $('body')[0].style.background="none";
    }
});
*/
