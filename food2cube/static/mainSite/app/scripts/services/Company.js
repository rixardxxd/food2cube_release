'use strict';

angular.module('food2cubeApp')
  .factory('Company', function () {
    var items = {};
    items.query = function() {
      return [
<<<<<<< HEAD
        {id: 1, name: 'Oracle', img: 'http://localhost:5000/static/mainSite/app/img/oracle.jpg'},
        {id: 2, name: 'Yahoo', img: 'http://localhost:5000/static/mainSite/app/img/yahoo.png'}
=======
        {id: 1, name: 'Oracle', img: 'static/mainSite/app/img/oracle.jpg'},
        {id: 2, name: 'Yahoo', img: 'static/mainSite/app/img/yahoo.png'}
>>>>>>> d8468662c29cb3dc85ec6de185a37c744d07368c
      ];
    };
    return items;
  });
