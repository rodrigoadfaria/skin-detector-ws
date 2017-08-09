/**
* IndexController
* @namespace thinkster.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Datasets', 'Snackbar'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, Authentication, Datasets, Snackbar) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.datasets = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf thinkster.layout.controllers.IndexController
    */
    function activate() {
      Datasets.all().then(datasetsSuccessFn, datasetsErrorFn);

      /**
      * @name datasetsSuccessFn
      * @desc Update datasets array on view
      */
      function datasetsSuccessFn(data, status, headers, config) {
        vm.datasets = data.data;
      }


      /**
      * @name datasetsErrorFn
      * @desc Show snackbar with error
      */
      function datasetsErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
  }
})();