angular
  .module('app')
  .component('loginComponent', {
    templateUrl: '/src/components/login/loginView.html',
    bindings: {},
    controller: loginComponentController
  })
;

function loginComponentController($auth, $state) {

  var vm = this;
  vm.$onInit = onInit;
  vm.handleLoginBtnClick = handleLoginBtnClick;
  vm.clearErrors = clearErrors;

  function onInit() {
    vm.user = {};
    vm.error = false;
  }

  function handleLoginBtnClick() {
      $auth.login(vm.user)
        .then(function(resp) {
          $state.go('admin.sсhemeList', {}, {reload: true});

        })
        .catch(function(resp) {
          vm.error = true;
          vm.msg = resp.data.non_field_errors[0];
        });
  }
  
  function clearErrors() {
     vm.error = false;
     vm.msg = "";
  }

}