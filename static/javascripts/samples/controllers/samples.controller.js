/**
* SamplesController
* @namespace thinkster.samples.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.samples.controllers')
    .controller('SamplesController', SamplesController);

  SamplesController.$inject = ['$scope', '$location', '$routeParams', 'Samples', 'Snackbar'];

  /**
  * @namespace SamplesController
  */
  function SamplesController($scope, $location, $routeParams, Samples, Snackbar) {
    var vm = this;

    vm.samples = [];
    render($routeParams.dataset_id)

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf thinkster.samples.controllers.SamplesController
    */
    function render(dataset_id) {
      Samples.get(dataset_id).then(samplesSuccessFn, samplesErrorFn);

      /**
      * @name samplesSuccessFn
      * @desc Update samples array on view
      */
      function samplesSuccessFn(data, status, headers, config) {
        vm.samples = data.data;
        console.log(vm.samples);
      }


      /**
      * @name samplesErrorFn
      * @desc Show snackbar with error
      */
      function samplesErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
 
  }
})();