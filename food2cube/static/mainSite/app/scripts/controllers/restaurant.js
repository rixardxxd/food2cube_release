'use strict';

//angular.module('food2cubeApp');



    angular.module('food2cubeApp').controller('RestaurantCtrl', ['$scope', '$modal','$log','Menu','$location', function ($scope,$modal,$log,Menu,$location) {

                $scope.menu1 = Menu.getMenu1();
                $log.info(Menu.getMenu1());
                $scope.menu2 = Menu.getMenu2();
                $scope.order1 = 0;
                $scope.order2 = 0;

                $scope.goBack = function ( path ) {
                    $location.path( path );
                };
                $scope.proceed = function ( path ) {
                    Menu.setOrder1($scope.order1);
                    Menu.setOrder2($scope.order2);
                    $location.path( path );
                };



               var ModalInstanceCtrl = function ($scope, $modalInstance, menu1,menu2,order1,order2) {

                          $scope.menu1 = menu1;
                          $scope.menu2 = menu2;
                          $scope.order1 = order1;

                          $scope.order2 = order2;
                          $scope.tips = 0;


                          $scope.ok = function () {
                            $modalInstance.close();
                          };

                          $scope.cancel = function () {
                            $modalInstance.dismiss('cancel');

                          };
               };


                $scope.open = function () {

                var modalInstance = $modal.open({
                  templateUrl: 'myModalContent.html',
                  controller: ModalInstanceCtrl,
                  resolve: {
                    menu1: function () {

                      return $scope.menu1;
                    },
                    menu2: function () {

                      return $scope.menu2;
                    },
                    order1: function () {

                      return $scope.order1;
                    },

                    order2: function () {

                      return $scope.order2;
                    }
                  }
                });

                modalInstance.result.then(function () {

                }, function () {
                  $log.info('Modal dismissed at: ' + new Date());
                });
              };

  }]);



