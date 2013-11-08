'use strict';

angular.module('food2cubeApp')
  .factory('Checkout', function ()
  {
    var functions = {};

    functions.queryTestData = function()
    {
      return [
        {id: 1, name: 'Ken\'s Fried Chicken', price: 1  , amount: 1 },
        {id: 2, name: 'Ken\'s Fried Duck'   , price: 10 , amount: 2 }
      ];
    };

    //temporary not used
    functions.updateAmount = function(items,id, amount)
    {
        var item;
        for (item in items)
        {
            if(item.id == id)
            {
                item.amount = amount;
                break;
            }
        }
    };

    return functions;
  });