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

/* TODO not sure if this is the correct place to add this code */
/*
$( document ).ready(function() {
    if('http://localhost:5000/#/company/1'==window.location.href){
	    $('body')[0].style.background="none";
    }
});
*/
