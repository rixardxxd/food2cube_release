'use strict';


angular.module('food2cubeApp')
  .factory('Menu', function () {
    var menu1 =
        {id: 100, name: 'eg1', category: 'Chinese', description: '',img: 'static/mainSite/app/img/eg1.png',
            price: '0.5'

        };

    var menu2 =   {id: 101, name: 'eg2',category: 'Japanese', description:'', img: 'static/mainSite/app/img/eg2.png',
            price: '0.5'
        };

    var order1 = 0;

    var order2 = 0;

    var menuService = {};

    menuService.getMenu1 = function(){
        return menu1;
    }
    menuService.getMenu2 = function(){
        return menu2;
    }
    menuService.getOrder1 = function(){
        return order1;
    }
    menuService.getOrder2 = function(){
        return order2;
    }
    menuService.setOrder1 = function(amount){
        order1 = amount;
    }
    menuService.setOrder2 = function(amount){
        order2 = amount;
    }


    return menuService;

  });