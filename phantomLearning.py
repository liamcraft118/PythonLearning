from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

var page = require('webpage').create();
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
console.log('The default user agent is ' + page.settings.userAgent);
phantom.exit()
// page.onConsoleMessage = function (msg) {
    // console.log(msg);
// };
// page.open('https://bbs.nga.cn/thread.php?fid=-7', function (status) {
    // console.log("Status: " + status);
    // var title = page.evaluate(function() {
        // return document.documentElement.outerHTML
    // });
    // console.log(title)
    // phantom.exit();
// });
