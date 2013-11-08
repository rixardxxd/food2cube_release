'use strict';

//angular.module('food2cubeApp');

    angular.module('food2cubeApp').controller('RestaurantCtrl', ['$scope', 'Restaurant','$modal','$log', function ($scope, Restaurant,$modal,$log) {
                $scope.restaurants = Restaurant.query();

                $scope.items = ['item1', 'item2', 'item3'];


               var ModalInstanceCtrl = function ($scope, $modalInstance, items) {

                          $scope.items = items;
                          $scope.selected = {
                            item: $scope.items[0]
                          };

                          $scope.ok = function () {
                            $modalInstance.close($scope.selected.item);
                          };

                          $scope.cancel = function () {
                            $modalInstance.dismiss('cancel');

                          };
               };


                $scope.open = function () {

                var modalInstance = $modal.open({
                  templateUrl: '/static/mainSite/app/views/myModalContent.html',
                  controller: ModalInstanceCtrl,
                  resolve: {
                    items: function () {
                        $log.info('cccc');
                      return $scope.items;
                    }
                  }
                });

                modalInstance.result.then(function (selectedItem) {
                  $scope.selected = selectedItem;
                }, function () {
                  $log.info('Modal dismissed at: ' + new Date());
                });
              };

  }]);



//var ModalDemoCtrl = function ($scope, $modal, $log) {
//
//  $scope.items = ['item1', 'item2', 'item3'];
//
//  $scope.open = function () {
//
//    var modalInstance = $modal.open({
//      templateUrl: 'static/mainSite/app/views/myModalContent.html',
//      controller: ModalInstanceCtrl,
//      resolve: {
//        items: function () {
//            $log.info($scope.items);
//          return $scope.items;
//        }
//      }
//    });
//
//    modalInstance.result.then(function (selectedItem) {
//      $scope.selected = selectedItem;
//    }, function () {
//      $log.info('Modal dismissed at: ' + new Date());
//    });
//  };
//};
//
//var ModalInstanceCtrl = function ($scope, $modalInstance, items) {
//
//  $scope.items = items;
//  $scope.selected = {
//    item: $scope.items[0]
//  };
//
//  $scope.ok = function () {
//    $modalInstance.close($scope.selected.item);
//  };
//
//  $scope.cancel = function () {
//    $modalInstance.dismiss('cancel');
//  };
//};
