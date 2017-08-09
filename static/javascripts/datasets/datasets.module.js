(function () {
  'use strict';

  angular
    .module('thinkster.datasets', [
      'thinkster.datasets.controllers',
      'thinkster.datasets.directives',
      'thinkster.datasets.services'
    ]);

  angular
    .module('thinkster.datasets.controllers', []);

  angular
    .module('thinkster.datasets.directives', ['ngDialog']);

  angular
    .module('thinkster.datasets.services', []);
})();