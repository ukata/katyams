var casper = require('casper').create({
      viewportSize: {width: 1920, height: 1080}
});
casper.start('https://ukata.me/contact/', function() {
    this.captureSelector('contact.png', 'body')});
casper.run();
