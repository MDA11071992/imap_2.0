angular
    .module('app')
    .component('buildingListComponent', {
      templateUrl: '/src/components/buildingList/buildingListView.html',
      bindings: {
        buildings: '<'
      },
      controller: buildingListComponentController
    })
;

function buildingListComponentController(floorEntity) {

  var vm = this;
  vm.$onInit = onInit;
  vm.removeFloor = removeFloor;

  function onInit() {

  }
  
  function removeFloor(floor, floorIndex, buildingId) {
    vm.buildings.forEach(function (building, index) {
      if(building.id == buildingId) {
        building.floors.splice(floorIndex,1);
      }
    });
    var f = new floorEntity();
    var obj = angular.merge(f, floor);
    obj.$destroy();
  }

}
