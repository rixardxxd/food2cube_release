'use strict';

//angular.module('food2cubeApp')
//  .controller('LoginCtrl', ['$scope', 'UserProfile', function ($scope, UserProfile) {
//    $scope.isLoggedIn = UserProfile.isLoggedIn();
//    $scope.doLogin = function() {
//      UserProfile.doLogin($scope.user,function(loginFailed,user){
//          $scope.loginFailed = loginFailed;
//          $scope.user = user;
//          if(!loginFailed)
//          $('#signin').modal('hide')
//      });
//    }
//  }]);


angular.module('food2cubeApp')
  .controller('LoginCtrl', ['$scope', 'UserProfile', function ($scope, UserProfile) {
    $scope.isLoggedIn = UserProfile.isLoggedIn();
    $scope.doLogin = function() {
      UserProfile.doLogin($scope.user).then(
          function(data){
            $scope.loginFailed = false;
            $('#signin').modal('hide');
          },
          function(data){
             $scope.loginFailed = true;
          }
      );

    }
  }]);


angular.module('food2cubeApp')
  .controller('SignupCtrl', ['$scope', 'UserProfile', function ($scope, UserProfile) {

    $scope.doSignup = function() {
      UserProfile.doSignup($scope.signupuser).then(
          function(data){
            $scope.signupfailed = false;
            $('#signup').modal('hide');
             console.log(data);
          },
          function(data){
             $scope.signupfailed = true;
             console.log(String(data));
              console.log('key value' + String(data).indexOf('duplicate key value'));

              if(String(data).indexOf('duplicate key value')!=-1){
              $scope.emailalreadyexists = true;

              }
              else{
              $scope.servererrorexists = true;
              }
          }
      );

    };

    $scope.emailalreadyexists = false;
    $scope.servererrorexists = false;

  }]);
