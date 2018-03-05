angular
  .module('app')
  .component('adminComponent', {
    templateUrl: '/src/components/admin/adminView.html',
    bindings: { },
    controller: adminComponentController
  })
;

function adminComponentController($auth, $state, ngDialog) {

  var vm = this;
  vm.$onInit = onInit;
  vm.logOut = logOut;
  vm.showInfo = showInfo;

  function onInit() {
    
  }
  
  function logOut() {
    $auth.logout();
    $state.go('submitLogin');
  }

  function showInfo() {
    ngDialog.open({
      template: '<info-component></info-component>',
      plain: true,
      className: 'ngdialog-theme-default__info',
      showClose: false
    });
  }
}
