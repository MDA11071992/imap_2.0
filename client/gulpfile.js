var gulp = require('gulp'),
  concat = require('gulp-concat-util'),
  uglify = require('gulp-uglify'),
  rename = require('gulp-rename'),
  less = require('gulp-less'),
  merge = require('merge-stream'),
  browserSync = require('browser-sync').create(),
  modRewrite = require('connect-modrewrite'),
  gsi = require('gulp-scripts-index'),
  argv = require('yargs').argv,
  // Add AngularJS dependency injection annotations with ng-annotate
  ngAnnotate = require('gulp-ng-annotate'),
  angularFilesort = require('gulp-angular-filesort'),
  htmlmin = require('gulp-htmlmin'),
  // Gulp task to precompile AngularJS templates with $templateCache
  templateCache = require('gulp-angular-templatecache'),
  // A stylesheet, javascript and webcomponent reference injection plugin for gulp. No more manual editing of your index.html!
  inject = require('gulp-inject'),
  cleanCSS = require('gulp-clean-css'),
  gulpSequence = require('gulp-sequence'),
  sourcemaps = require('gulp-sourcemaps'),
  // Static asset revision by appending content hash to file names unicorn.css → unicorn-098f6bcd.css
  rev = require('gulp-rev'),
  // Wrap all code in file to IIFE for clear global scope
  iife = require('gulp-iife'),
  // Prevent pipe breaking caused by errors from gulp plugins.
  plumber = require('gulp-plumber'),
  path = require('path'),
  clean = require('gulp-clean'),
  util = require('gulp-util'),
  eslint = require('gulp-eslint');

var historyApiFallback = require('connect-history-api-fallback');

gulp.task('serve', function() {
  browserSync.init({
    server: {
      baseDir: "./",
      middleware: [ historyApiFallback() ]
    }
  });
});

gulp.task('fonts', function () {
  return gulp.src('./src/fonts/**/*.*')
    .pipe(gulp.dest('./dist/fonts/'));
});

gulp.task('img', function () {
  return gulp.src('./src/img/**/*.*')
    .pipe(gulp.dest('./dist/img/'));
});

gulp.task('clean:all', function () {
  return gulp
    .src([
      'dist/',
      'index.html'
    ], {read: false})
    .pipe(clean());
});

gulp.task('css', function () {
  return gulp
    .src([
      'src/less/main.less',
      'src/components/**/*.less'
    ])
    .pipe(less({
      paths: [path.join(__dirname)]
    }))
    .pipe(concat('styles.css'))
    .pipe(gulp.dest('dist/css/'));
});

gulp.task('css:minify', ['css'], function () {
  return gulp
    .src([
      'dist/css/styles.css'
    ])
    .pipe(plumber())
    .pipe(sourcemaps.init())
    .pipe(cleanCSS({
      keepSpecialComments: 0
    }))
    .pipe(rev())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(sourcemaps.write('./'))
    .pipe(plumber.stop())
    .pipe(gulp.dest('dist/css/'));
});

gulp.task('scripts', function () {
  return gulp
    .src([
      'src/**/*.js'
    ])
    .pipe(plumber())
    .pipe(sourcemaps.init())
    .pipe(ngAnnotate())
    .pipe(iife())
    .pipe(angularFilesort())
    .pipe(concat('scripts.js'))
    .pipe(gulp.dest('dist/js/'))
    .pipe(uglify())
    .pipe(rev())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(sourcemaps.write('./'))
    .pipe(plumber.stop())
    .pipe(gulp.dest('dist/js/'));
});

gulp.task('views', function () {
  return gulp
    .src([
      'src*/**/*.html',
      '!src/index.html'
    ])
    .pipe(plumber())
    .pipe(templateCache('views.js', {
      module: 'app',
      transformUrl: function (url) {
        return url.replace(/^src\//, '/src/')
      }
    }))
    .pipe(sourcemaps.init())
    .pipe(gulp.dest('dist/js/'))
    .pipe(uglify())
    .pipe(rev())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(sourcemaps.write('./'))
    .pipe(plumber.stop())
    .pipe(gulp.dest('dist/js/'));
});

gulp.task('lint', function () {
  return gulp
    .src('src/**/*.js')
    // eslint() attaches the lint output to the "eslint" property
    // of the file object so it can be used by other modules.
    .pipe(eslint())
    // eslint.format() outputs the lint results to the console.
    // Alternatively use eslint.formatEach() (see Docs).
    .pipe(eslint.format())
    // To have the process exit with an error code (1) on
    // lint error, return the stream and pipe to failAfterError last.
    .pipe(eslint.failAfterError());
});

gulp.task('index:all-src', function () {
  return gulp
    .src('src/index.html')
    .pipe(plumber())
    .pipe(inject(
      gulp
        .src('src/**/*.js')
        .pipe(angularFilesort())
    ))
    .pipe(inject(
      gulp
        .src('dist/css/*.css', {read: false})
    ))
    .pipe(plumber.stop())
    .pipe(gulp.dest('./'));
});

gulp.task('index:merged-min', ['views', 'fonts', 'img', 'css:minify', 'scripts'], function () {
  return gulp
    .src('src/index.html')
    .pipe(plumber())
    .pipe(inject(gulp.src(
      [
        'dist/js/*.min.js',
        'dist/css/*.min.css'
      ], {
        read: false
      }
    )))
    .pipe(plumber.stop())
    .pipe(gulp.dest('./'));
});

//wrapper for task "serve"
gulp.task('index:all-src-with-css', gulpSequence('clean:all', 'fonts', 'img', 'css', 'index:all-src'));

// run lite-server
gulp.task('server', function () {
  browserSync.init({
    startPath: '/index.html',
    open: 'external',
    server: {
      baseDir: "./",
      middleware: [
        modRewrite([
          '!\\.\\w+$ /index.html [L]'
        ])
      ],
    }
  });
});

// ++==================================++
// || For developer                    ||
// ++==================================++
gulp.task('serve', ['index:all-src-with-css'], function () {

  browserSync.init({
    startPath: '/index.html',
    host: 'localhost',
    open: 'external',
    server: {
      baseDir: "./",
      middleware: [
        modRewrite([
          '!\\.\\w+$ /index.html [L]'
        ])
      ],
    }
  });

  gulp.watch('src/**/*.less', ['css']);

  gulp.watch([
    'src/**/*.js',
    'src/**/*.html',
    'dist/css/*.css'
  ], function (event) {
    util.log(event.type, 'file:', event.path);

    if (/\/src\/index\.html$/.test(event.path)
      || event.type === 'added'
      || event.type === 'deleted'
    ) {

      util.log('INJECTOR', event.type, 'file:', event.path);

      gulp.start('index:all-src', function (err) {
        if (err) return;
        if (!argv.withoutWatch) {
          browserSync.reload(event);
        }
      });
    } else {
      if (!argv.withoutWatch) {
        browserSync.reload(event)
      }
    }
  });
});

// ++=================================++
// || Main task fo dev server         ||
// ++=================================++
gulp.task('dev', ['index:all-src-with-css']);

// ++===================================================++
// || Main task fo production server  ||
// ++===================================================++
gulp.task('default', gulpSequence('clean:all', 'index:merged-min'));