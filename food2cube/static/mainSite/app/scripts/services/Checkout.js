'use strict';

angular.module('food2cubeApp')
  .factory('Checkout', function ()
  {
    var items = {};

    items.query = function()
    {
      return [
        {id: 1, name: 'Ken\'s Fried Chicken', price: 1  , amount: 1 },
        {id: 2, name: 'Ken\'s Fried Duck'   , price: 10 , amount: 2 }
      ];
    };

    return items;
  });