angular
  .module('app')
  .component('navigationAdminComponent', {
    templateUrl: '/src/components/navigationAdmin/navigationAdminView.html',
    bindings: {
    },
    controller: navigationAdminComponentController
  })
;

function navigationAdminComponentController() {

  var vm = this;
  vm.$onInit = onInit;

  function onInit() {

  }

}