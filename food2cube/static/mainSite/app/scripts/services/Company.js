'use strict';

angular.module('food2cubeApp')
  .factory('Company', function () {
    var items = {};
    items.query = function() {
      return [

        {id: 1, name: 'Oracle', img: 'static/mainSite/app/img/oracle.jpg'},
        {id: 2, name: 'Yahoo', img: 'static/mainSite/app/img/yahoo.png'}
      ];
    };
    return items;
  });
