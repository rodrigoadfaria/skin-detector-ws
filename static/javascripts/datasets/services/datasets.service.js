/**
* Datasets
* @namespace thinkster.datasets.services
*/
(function () {
  'use strict';

  angular
    .module('thinkster.datasets.services')
    .factory('Datasets', Datasets);

  Datasets.$inject = ['$http'];

  /**
  * @namespace Datasets
  * @returns {Factory}
  */
  function Datasets($http) {
    var Datasets = {
      all: all,
      get: get
    };

    return Datasets;

    ////////////////////

    /**
    * @name all
    * @desc Get all Datasets
    * @returns {Promise}
    * @memberOf thinkster.datasets.services.Datasets
    */
    function all() {
      return $http.get('/api/v1/datasets/');
    }


   /**
     * @name get
     * @desc Get the Samples of a given dataset
     * @param {string} dataset The dataset to get Samples for
     * @returns {Promise}
     * @memberOf thinkster.datasets.services.Datasets
     */
    function get(dataset) {
      return $http.get('/api/v1/datasets/' + dataset);
    }
  }
})();