angular
  .module('app')
  .component('sidebarComponent', {
    templateUrl: '/src/components/sidebar/sidebarView.html',
    bindings: {
        name: '@',
        list: '<'
    },
    controller: sidebarComponentController
  })
;

function sidebarComponentController() {

  var vm = this;
  vm.$onInit = onInit;

  function onInit() {
  }

}