/**
* Datasets
* @namespace thinkster.datasets.directives
*/
(function () {
  'use strict';

  angular
    .module('thinkster.datasets.directives')
    .directive('datasets', datasets);

  /**
  * @namespace Datasets
  */
  function datasets() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf thinkster.datasets.directives.Datasets
    */
    var directive = {
      controller: 'DatasetsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        datasets: '='
      },
      templateUrl: '/static/templates/datasets/datasets.html'
    };

    return directive;
  }
})();