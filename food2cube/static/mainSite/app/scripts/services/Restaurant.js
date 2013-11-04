'use strict';


angular.module('food2cubeApp')
  .factory('Restaurant', function () {
    var restaurants = [
        {id: 100, name: 'eg1', category: 'Chinese', img: 'static/mainSite/app/img/eg1.png'},
        {id: 101, name: 'eg2',category: 'Japanese', img: 'static/mainSite/app/img/eg2.png'},
        {id: 102, name: 'eg3', category: 'Indian', img: 'static/mainSite/app/img/eg3.png'},
        {id: 103, name: 'eg4',category: 'Japanese', img: 'static/mainSite/app/img/eg4.png'}

    ];
    var items = {};
    items.query = function() {

       var results = [];
    for (var i = 0; i < restaurants.length; i++ ) {
        if (i % 2 == 0) results.push([]);
        results[results.length-1].push(restaurants[i]);
    }
        return results;

    };
    return items;

  });