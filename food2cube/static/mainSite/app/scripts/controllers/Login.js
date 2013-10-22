'use strict';

angular.module('food2cubeApp')
  .controller('LoginCtrl', ['$scope', 'UserProfile', function ($scope, UserProfile) {
    $scope.isLoggedIn = UserProfile.isLoggedIn();
    $scope.doLogin = function() {
      UserProfile.doLogin($scope.user);
    }
  }]);
