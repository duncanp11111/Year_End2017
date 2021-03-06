/**
 * Reporter service sends data to Google Analytics for analysis. We don't name
 * this file 'analytics.js' in case an ad-blocker blocks it and breaks EarSketch.
 *
 * @author Creston Bunch
 */
app.factory('reporter', ['esconsole', 'reader', function (esconsole, reader) {

  var PAGE_LOADED = false;

  /**
   * Record a user login action.
   */
  function login(username) {
    ga('send', {
      hitType: 'event',
      eventCategory: 'user',
      eventAction: 'login',
    });
  }

  /**
   * Record a user logout action.
   */
  function logout(username) {
    ga('send', {
      hitType: 'event',
      eventCategory: 'user',
      eventAction: 'logout',
    });
  }

  /**
   * Record an exception that happens.
   */
  function exception(msg) {
    ga('send', {
      hitType: 'exception',
      exDescription: msg
    });
  }

  /**
   * Record a script compilation and result.
   *
   * @param language {string} The language python or JavaScript
   * @param success {boolean} Whether or not the compilation succeeded.
   * @param errorType {string} The type of error
   * @param duration {integer} How long the compilation took (milliseconds).
   */
  function compile(language, success, errorType, duration) {
    ga('send', {
      hitType: 'event',
      eventCategory: 'script',
      eventAction: 'compile',
      eventLabel: language,
    });

    if (!success) {
      ga('send', {
        hitType: 'event',
        eventCategory: 'script',
        eventAction: 'error',
        eventLabel: errorType,
      });
    }

    ga('send', {
      hitType: 'timing',
      timingCategory: 'script',
      timingVar: 'compile',
      timingValue: duration,
    });
  }

  /**
   * Record the time it took the page to load from start to when the sounds
   * browser is populated. Only do it once per page load.
   */
  function loadTime() {
    if (PAGE_LOADED == false) {
      var duration = window.performance.now();
      ga('send', {
        hitType: 'timing',
        timingCategory: 'load',
        timingVar: 'page',
        timingValue: duration,
      });
      PAGE_LOADED = true;
    }
  }

  /**
   * Report the complexity score of a script.
   *
   * @param language {string} The language python or javascript
   * @param script {string} The script source code
   */
  function complexity(language, script) {
    if (language == "python") {
      var complexity = reader.analyzePython(script);
      var total = reader.total(complexity);
    } else if (language == "javascript") {
      var complexity = reader.analyzeJavascript(script);
      var total = reader.total(complexity);
    } else {
      return;
    }

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'userFunc',
      eventLabel: complexity.userFunc,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'booleanConditionals',
      eventLabel: complexity.booleanConditionals,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'conditionals',
      eventLabel: complexity.conditionals,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'loops',
      eventLabel: complexity.loops,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'lists',
      eventLabel: complexity.lists,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'listOps',
      eventLabel: complexity.listOps,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'strOps',
      eventLabel: complexity.strOps,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'complexity',
      eventAction: 'total',
      eventLabel: total,
    });
  }

  /**
   * Report a shared script.
   *
   * @param method {string} The sharing method: link or soundcloud
   * @param license {string} The license used
   */
  function share(method, license) {
    ga('send', {
      hitType: 'event',
      eventCategory: 'share',
      eventAction: 'method',
      eventLabel: method,
    });

    ga('send', {
      hitType: 'event',
      eventCategory: 'share',
      eventAction: 'license',
      eventLabel: license,
    });
  }

  return {
      login: login,
      logout: logout,
      exception: exception,
      compile: compile,
      complexity: complexity,
      loadTime: loadTime,
      share: share,
  };

}]);

if (true) {
//if (window.location.hostname === 'earsketch.gatech.edu') {
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-33307046-2', 'auto');
  ga('send', 'pageview');
}



