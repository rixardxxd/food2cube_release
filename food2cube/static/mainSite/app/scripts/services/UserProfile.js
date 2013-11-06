'use strict';

angular.module('food2cubeApp')
  .factory('UserProfile', ['$http','$q', function ($http,$q) {
    var loggedIn = false;
    var loggedInFailed = false;
    var signedup = false;


    return {
      isLoggedIn: function () {
        return loggedIn;
      },
      doLogin: function (data) {

        var deferred = $q.defer();
        $http({
          method : 'POST',
          url : '/api/login/',
          data : data
        }).success(function (data, status, headers, config) {
            loggedIn = true;
            loggedInFailed = false;
            deferred.resolve(data);


        }).error(function (data, status, headers, config) {
            //TODO: Show error message
            loggedIn = false;
            loggedInFailed = true;
            deferred.reject(data);



        });

          return deferred.promise;
      },

      doSignup: function (data){
            var deferred = $q.defer();

            $http({
                method : 'POST',
                url : '/api/signup/',
                data: data
            }).success(function (data,status,headers,config){
                    signedup = true;
                    deferred.resolve(data);
            }).error(function (data, status, headers, config) {
            //TODO: Show error message
                    signedup = false;
                    deferred.reject(data);


            });

            return deferred.promise;
       }

    };
  }]);
