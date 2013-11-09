'use strict';


angular.module('food2cubeApp')
  .factory('Restaurant', function () {
    var restaurants = [
        {id: 100, name: 'eg1', category: 'Chinese', img: 'static/mainSite/app/img/eg1.png',menus:[
            {name:'aaa1',price:'5'},
            {name:'bbb1',price:'6'}

        ]

        },
        {id: 101, name: 'eg2',category: 'Japanese', img: 'static/mainSite/app/img/eg2.png',menus:[
            {name:'aaa2',price:'5'},
            {name:'bbb2',price:'6'}
        ]
        },
        {id: 102, name: 'eg3', category: 'Indian', img: 'static/mainSite/app/img/eg3.png',menus:[
            {name:'aaa3',price:'5'},
            {name:'bbb3',price:'6'}
        ]
        },
        {id: 103, name: 'eg4',category: 'Japanese', img: 'static/mainSite/app/img/eg4.png',
        menus:[
            {name:'aaa4',price:'5'},
            {name:'bbb4',price:'6'}
           ]
        }

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