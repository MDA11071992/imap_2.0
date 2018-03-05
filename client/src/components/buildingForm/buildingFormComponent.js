angular
  .module('app')
  .component('buildingFormComponent', {
    templateUrl: '/src/components/buildingForm/buildingFormView.html',
    bindings: {
        building: '<'
    },
    controller: buildingFormComponentController
  });

function buildingFormComponentController($scope) {

  var vm = this;
  vm.$onInit = onInit;
  vm.removeBuilding = removeBuilding;
  vm.clearErrors = clearErrors;

  function onInit() {
    vm.building.coordinate = vm.building.coordinate || {};
    vm.building.noValid = false;
  }

  function removeBuilding() {
    $scope.$emit('removeBuildingListener', vm.building);
  }

  function clearErrors() {
     vm.building.noValid = false;
  }

}