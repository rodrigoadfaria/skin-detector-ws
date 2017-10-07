/**
* Samples
* @namespace thinkster.samples.services
*/
(function () {
  'use strict';

  angular
    .module('thinkster.samples.services')
    .factory('Samples', Samples);

  Samples.$inject = ['$http'];

  /**
  * @namespace Samples
  * @returns {Factory}
  */
  function Samples($http) {
    var Samples = {
      all: all,
      get: get
    };

    return Samples;

    ////////////////////

    /**
    * @name all
    * @desc Get all Samples
    * @returns {Promise}
    * @memberOf thinkster.samples.services.Samples
    */
    function all() {
      return $http.get('/api/v1/samples/');
    }


   /**
     * @name get
     * @desc Get the Samples of a given dataset
     * @param {string} dataset The dataset to get Samples from
     * @returns {Promise}
     * @memberOf thinkster.samples.services.Samples
     */
    function get(dataset) {
      return $http.get('/api/v1/datasets/' + dataset + '/samples/');
    }
  }
})();