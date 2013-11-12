'use strict';

//angular.module('food2cubeApp');



    angular.module('food2cubeApp').controller('RestaurantCtrl', ['$scope', '$modal','$log', function ($scope,$modal,$log) {
                var menu1 =
        {id: 100, name: 'eg1', category: 'Chinese', description: '',img: 'static/mainSite/app/img/eg1.png',
            price: '8.5'

        };

                var menu2 =   {id: 101, name: 'eg2',category: 'Japanese', img: 'static/mainSite/app/img/eg2.png',
            price: '8.75'
        };
                $scope.menu1 = menu1;
                $scope.menu2 = menu2;
                $scope.order1 = 0;
                $scope.order2 = 0;



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



