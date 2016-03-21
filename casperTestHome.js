var casper = require('casper').create({
      viewportSize: {width: 1920, height: 1080}
});



casper.start('https://ukata.me/', function() {
    this.captureSelector('ukata.png', 'body')});

casper.run();
