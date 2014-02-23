'use strict';

angular.module('food2cubeApp', ['ngRoute','ui.bootstrap'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/mainSite/app/views/restaurant.html',
        controller: 'RestaurantCtrl'

        })
      .when('/checkout', {
        templateUrl: 'static/mainSite/app/views/checkout.html',
        controller: 'CheckoutCtrl'
      })
      .when('/ordercompletion/:option', {
        templateUrl: 'static/mainSite/app/views/ordercompletion.html',
        controller: 'OrderCompletionCtrl'
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
