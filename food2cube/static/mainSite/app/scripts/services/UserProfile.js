'use strict';

angular.module('food2cubeApp')
  .factory('UserProfile', ['$http', function ($http) {
    var loggedIn = false;
    var firstName;
    var lastName;

    return {
      isLoggedIn: function () {
        return loggedIn;
      },
      doLogin: function (data) {
        $http({
          method : 'POST',
          url : '/api/login',
          data : data
        }).success(function (data, status, headers, config) {
            loggedIn = true;
            firstName = data.firstName;
            lastName = data.lastName;
        }).error(function (data, status, headers, config) {
            //TODO: Show error message
        });
      }
    };
  }]);
