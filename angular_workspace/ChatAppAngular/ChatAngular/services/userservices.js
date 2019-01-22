app.service('userservices', function ($http, $location) {
    this.registerUser = function(data) {
        /**
         * declaring $http variable and returning to get an instance after $http service
         * to make rest API calls
         */
       return $http({
            //declaring method type
            method: 'POST',
            //calling register API call
            url: 'http://127.0.0.1:8000/accounts/signup/',
            //sending user register data
            data: data
        })
    },

    this.loginUser = function (data) {
        
        /**
         * declaring $http variable and returning to get an instance after $http service
         * to make rest API calls
         */
       return $http({
            //declaring method type
            method: 'POST',
            //calling register API call
            url: 'http://127.0.0.1:8000/accounts/login/',
            //sending user register data
            data: data
        })
    }
 
 });