let mix = require('laravel-mix');

mix.combine([
    'porfolio/consulting/static/consulting/assets/css/style.css',
    'porfolio/consulting/static/consulting/assets/css/icons.css',
    'porfolio/consulting/static/consulting/assets/css/magnific-popup.css',
    'porfolio/consulting/static/consulting/assets/css/slick.min.css',
    'porfolio/consulting/static/consulting/assets/css/bootstrap.min.css'
], 'porfolio/consulting/static/consulting/assets/css/all.css')
.minify('porfolio/consulting/static/consulting/assets/css/all.css');

mix.combine([
    'porfolio/consulting/static/consulting/assets/js/jquery.min.js',
    'porfolio/consulting/static/consulting/assets/js/modernizr.min.js',
    'porfolio/consulting/static/consulting/assets/js/jquery.easing.js',
    'porfolio/consulting/static/consulting/assets/js/popper.min.js',
    'porfolio/consulting/static/consulting/assets/js/bootstrap.min.js',
    'porfolio/consulting/static/consulting/assets/js/slick.min.js',
    'porfolio/consulting/static/consulting/assets/js/scrollUp.min.js',
    'porfolio/consulting/static/consulting/assets/js/counterup.min.js',
    'porfolio/consulting/static/consulting/assets/js/jquery.sticky-kit.js',
    'porfolio/consulting/static/consulting/assets/js/magnific-popup.min.js',
    'porfolio/consulting/static/consulting/assets/js/jquery.easypiechart.min.js',
    'porfolio/consulting/static/consulting/assets/js/active.js'
], 'porfolio/consulting/static/consulting/assets/js/all.js')
.minify('porfolio/consulting/static/consulting/assets/js/all.js');
