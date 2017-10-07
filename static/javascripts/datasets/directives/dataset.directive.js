/**
* Dataset
* @namespace thinkster.datasets.directives
*/
(function () {
  'use strict';

  angular
    .module('thinkster.datasets.directives')
    .directive('dataset', dataset);

  /**
  * @namespace Dataset
  */
  function dataset() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf thinkster.datasets.directives.Dataset
    */
    var directive = {
      restrict: 'E',
      scope: {
        dataset: '=',
        onclick_fired: '&ondataset'
      },
      link: function(scope, elem, attrs) {
        elem.bind('click', function() {
          scope.onclick_fired();
        });
      },
      templateUrl: '/static/templates/datasets/dataset.html'
    };

    return directive;
  }
})();