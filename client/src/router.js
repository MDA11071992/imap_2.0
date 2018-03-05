angular
    .module('app')
    .config(function ($stateProvider, $urlRouterProvider) {
      $urlRouterProvider.otherwise("/app/main/services");
      $stateProvider
          .state('submitLogin', {
            url: '/login',
            permissions: false,
            module: false,
            template: '<login-component></login-component>'
          })
          .state('app', {
            url: '/app',
            abstract: true,
            permissions: false,
            module: false,
            template: '<app-component' +
            ' video="$resolve.video">' +
            '</app-component>',
            resolve: {
              video: ['advertisementEntity', function (advertisementEntity) {
                return advertisementEntity.fetchAll();
              }]
            }
          })
          .state('app.route', {
            url: '/route?room',
            permissions: false,
            module: false,
            views: {
              'navigation@app': {
                template: '<navigation-component ' +
                '</navigation-component>'
              },
              'content@app': {
                template: '<route-component ' +
                '</route-component>'
              }
            }
          })
          .state('app.main', {
            url: '/main',
            abstract: true,
            permissions: false,
            module: false,
            views: {
              'navigation@app': {
                template: '<navigation-component ' +
                '</navigation-component>'
              },
              'content@app': {
                template: '<main-component ' +
                '</main-component>'
              }
            }
          })
          .state('app.main.services', {
            url: '/services',
            permissions: false,
            module: false,
            views: {
              'sidebar@app.main': {
                template: '<sidebar-component ' +
                'name="services"' +
                'list="$resolve.list">' +
                '</sidebar-component>'
              }
            },
            resolve: {
              list: ['serviceEntity', function (serviceEntity) {
                return serviceEntity.fetchAll();
              }]
            }
          })
          .state('app.main.services.service', {
            url: '/:id',
            permissions: false,
            module: false,
            views: {
              'content@app.main': {
                template: '<service-content-component ' +
                'content="$resolve.content">' +
                '</service-content-component>'
              }
            },
            resolve: {
              content: ['$stateParams', 'serviceEntity', function ($stateParams, serviceEntity) {
                return serviceEntity.fetchOne($stateParams.id);
              }]
            }
          })
          .state('app.main.rooms', {
            url: '/rooms',
            permissions: false,
            module: false,
            views: {
              'sidebar@app.main': {
                template: '<sidebar-component ' +
                'name="rooms"' +
                'list="$resolve.list">' +
                '</sidebar-component>'
              }
            },
            resolve: {
              list: ['roomEntity', function (roomEntity) {
                return roomEntity.fetchAll();
              }]
            }
          })
          .state('app.main.rooms.room', {
            url: '/:id',
            permissions: false,
            module: false,
            views: {
              'content@app.main': {
                template: '<room-content-component ' +
                'content="$resolve.content">' +
                '</room-content-component>'
              }
            },
            resolve: {
              content: ['$stateParams', 'roomEntity', function ($stateParams, roomEntity) {
                return roomEntity.fetchOne($stateParams.id);
              }]
            }
          })
          .state('app.main.therapy', {
            url: '/therapy',
            permissions: false,
            module: false,
            views: {
              'sidebar@app.main': {
                template: '<sidebar-component ' +
                'name="therapy"' +
                'list="$resolve.list">' +
                '</sidebar-component>'
              }
            },
            resolve: {
              list: ['therapyEntity', function (therapyEntity) {
                return therapyEntity.fetchAll();
              }]
            }
          })
          .state('app.main.therapy.treat', {
            url: '/:therapyId',
            permissions: false,
            module: false,
            views: {
              'content@app.main': {
                template: '<therapy-content-component ' +
                'item="$resolve.item">' +
                '</therapy-content-component>'
              }
            },
            resolve: {
              item: ['$stateParams', 'therapyEntity', function ($stateParams, therapyEntity) {
                return therapyEntity.fetchOne($stateParams.therapyId);
              }]
            }
          })
          .state('app.main.therapy.treat.subtherapy', {
            url: '/:subTherapyId',
            permissions: false,
            module: false,
            views: {
              'content@app.main': {
                template: '<therapy-content-component ' +
                'subtherapy="true" ' +
                'item="$resolve.item"> ' +
                '</therapy-content-component>'
              }
            },
            resolve: {
              item: ['$stateParams', 'subTherapyEntity', function ($stateParams, subTherapyEntity) {
                return subTherapyEntity.fetchOne($stateParams.subTherapyId);
              }]
            }
          })
          .state('admin', {
            url: '/admin',
            abstract: true,
            permissions: false,
            module: false,
            template: '<admin-component></admin-component>',
            resolve: {
              authenticate: ['$state', '$auth', function ($state, $auth) {
                if(!$auth.isAuthenticated()) {
                  $state.go('submitLogin', {}, {reload: true});
                }
              }]
            }
          })
          .state('admin.sсhemeList', {
            url: '/schemelist',
            permissions: false,
            module: false,
            views: {
              'content@admin': {
                  template: '<scheme-component ' +
                            'schemelist="$resolve.schemelist">' +
                            '</scheme-component>'
              }
            },
            resolve: {
              schemelist: ['schemeEntity', function (schemeEntity) {
                return schemeEntity.fetchAll();
              }]
            }
          })
          .state('admin.schemeUpdate', {
            url: '/schemelist/:schemeId',
            permissions: false,
            module: false,
            views: {
              'content@admin': {
                  template: '<scheme-update-component ' +
                            'model="$resolve.item">' +
                            '</scheme-update-component>'
              }
            },
            resolve: {
              item: ['$stateParams', 'schemeEntity', function ($stateParams, schemeEntity) {
                return schemeEntity.fetchOne($stateParams.schemeId);
              }]
            }
          })
          .state('admin.buildingList', {
            url: '/buildinglist',
            permissions: false,
            module: false,
            views: {
              'content@admin': {
                  template: '<building-list-component ' +
                            'buildings="$resolve.buildings">' +
                            '</building-list-component>'
              }
            },
            resolve: {
              buildings: ['buildingEntity', function (buildingEntity) {
                return buildingEntity.fetchAll();
              }]
            }
          })
          .state('admin.buildingList.floorCreate', {
            url: '/:buildingId/floor/',
            permissions: false,
            module: false,
            views: {
              'content@admin': {
                  template: '<floor-create-component ' +
                      'buildings="$resolve.buildings">' +
                      '</floor-create-component>'
              }
            }
          })
          .state('admin.buildingList.floorUpdate', {
            url: '/:buildingId/floor/:floorId',
            permissions: false,
            module: false,
            views: {
              'content@admin': {
                 template: '<floor-update-component ' +
                            'model="$resolve.item"' +
                            'buildings="$resolve.buildings" >' +
                            '</floor-update-component>'
              }
            },
            resolve: {
              item: ['$stateParams', 'floorEntity', function ($stateParams, floorEntity) {
                return floorEntity.fetchOne($stateParams.floorId);
              }]
            }
          })
    });