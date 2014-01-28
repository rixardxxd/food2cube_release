'use strict';
 var data = {

                    cmd: "_ext-enter",
                    redirect_cmd: "_cart",
                    first_name: "wwww",
                    last_name: "bbb",
                    night_phone_a: "4083067511",
                    business: "rixardxxd@gmail.com",
                    upload: "1",
                    rm: "2",
                    charset: "utf-8",
                    cancel_return: "http://morning-cove-6125.herokuapp.com/#/company/1",
                    return: "http://morning-cove-6125.herokuapp.com/#/ordercompletion/1",
                    no_shipping: "1",
                    cn: "Will be delivered to address 1"


                };
var addresses = [
    {address: "cisco 1", img: "img1"},
    {address: "cisco 2", img: "img2"},
    {address: "cisco 3", img: "img3"}
];


angular.module('food2cubeApp')
  .controller('CheckoutCtrl', ['$log','$scope', 'Checkout', '$http','Menu','$location',
        function ($log,$scope, Checkout, $http,Menu,$location)
        {
                 //In practise, $scope.items should be added in former page, not generated in service.
                var menuList = [];
                var Menu1 = Menu.getMenu1();
                Menu1.amount = Menu.getOrder1();
                menuList.push(Menu1);
                var Menu2 = Menu.getMenu2();
                Menu2.amount = Menu.getOrder2();
                menuList.push(Menu2);
                $scope.items = menuList;

                $scope.tips = 0 ;

                var calculate = function()
                {
                     var amount = 0;
                    for(var i = 0;i < menuList.length; i ++){
                       amount = amount + menuList[i].amount * menuList[i].price;
                    }
                    amount = (1 + $scope.tips) * amount;
                    $log.info($scope.tips);
                    $scope.totalAmount = amount;

                    return amount;

                }

                $scope.totalAmount = calculate();
                $scope.doUpdateAmount = calculate;

                 $scope.goBack = function ( path ) {
                        $location.path( path );
                    };

                $scope.checkout =  function () {

                    $log.info("Menu1 " + Menu1.amount);
                    $log.info("Menu2 " + Menu2.amount);
                var count = 1;
                if(Menu1.amount > 0){
                   data["item_name_" + count] = Menu1.name;
                   data["amount_" + count] = Menu1.price;
                   data["quantity_" + count] = Menu1.amount;
                    count = count + 1;
                }
                if(Menu2.amount > 0){
                    data["item_name_" + count] = Menu2.name;
                    data["amount_" + count] = Menu2.price;
                    data["quantity_" + count] = Menu2.amount;
                }

                // build form
                var form = $('<form/></form>');
                form.attr("action", "https://www.paypal.com/cgi-bin/webscr");

              //  form.attr("https://www.sandbox.paypal.com/cgi-bin/webscr?");
                form.attr("method", "POST");
                form.attr("style", "display:none;");
                addFormFields(form, data);
              //  addFormFields(form, parms.options);
                $("body").append(form);
                $log.info(form);
                // submit form
                form.submit();
                form.remove();
            }


            $scope.addresses = addresses;
            $scope.address = addresses[0];
        }
    ]);


function addFormFields(form, data) {
    if (data != null) {
        $.each(data, function (name, value) {
            if (value != null) {
                var input = $("<input></input>").attr("type", "hidden").attr("name", name).val(value);
                form.append(input);
            }
        });
    }
}