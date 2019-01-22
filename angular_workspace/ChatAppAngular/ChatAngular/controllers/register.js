app.controller('register', function ($scope, userservices ,$state) {
    $scope.register = function () {

        //store register data in a data object 
            var data = {
                userName: $scope.userName,
                email: $scope.email,
                Password: $scope.Password,
            }
            console.log(data);
            //call userService method registerUser() and passing user data to it
            userservices.registerUser(data).then(
                //execute in case of a successfull response
                function successCallback(response) {
                    console.log("register successful ");
                    console.log(response.data);
                     $state.go('login');
                },
                //execute in case of unsucessfull response
                function errorCallback(response) {
                    console.log("register Unsuccessful ");
                    console.log(response.data);
                }
            );
        }
    });