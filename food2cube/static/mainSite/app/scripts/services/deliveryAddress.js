'use strict';

angular.module('food2cubeApp')
  .factory('DeliveryAddress', function () {
     var addresses = [
        {address:'cisco parking lot 1', img: 'static/mainSite/app/img/eg1.png'
        },
        {address:'cisco parking lot 2', img: 'static/mainSite/app/img/eg1.png'
        },
        {address:'cisco parking lot 3', img: 'static/mainSite/app/img/eg1.png'
        }
      ];

    return addresses;
  });
