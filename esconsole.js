app.factory('esconsole', ['$window', function ($window) {
    /*==================== new logger / print functions ====================*/
    var ESConsoleTraceLevel = 3;
    var ESConsoleExcludedTags = [];
    var ESConsoleIncludedTags = ['WARNING', 'ERROR', 'FATAL'];
    var ESLogExcludedTags = ['TEMP', 'EXCLUDE', 'NOLOG', 'META'];
    var ESLogIncludedTags = ['INFO', 'USER', 'WARNING', 'ERROR', 'FATAL'];

    /**
     * A public function that queries URL parameters for setting the esconsole and logging configurations. Called from the main controller at the app initialization. Following parameters are currently supported: trace={number} sets the global trace level, with number between 0 to 4. hide={tag(s)} to temporarily hide console log printing for certain tags. Input can be such as hide=foo, hide='foo', hide=foo,bar, hide=[foo,bar] (Note: double quotes would break: hide=%27foo%27). print/show={tag(s)} for overriding tags to be always printed, even ones already hidden. exclude={tag(s)} for temporarily disabling some tagged messages from being logged (for error report). include={tag(s)} for overriding the excluded tags.
     * @name getURLParameters
     * @function
     * @example
     * // Sets the traceLevel to 1, adds 'TEMP' to the tag list for not printing, adds 'MISC' and 'DEBUG' for the tag list for not logging.
     * // URL:
     * .../EarSketch/webclient/index.html?trace=1&hide=temp&exclude=["misc",DEBUG]
     */
    function getURLParameters() {
        var wdw = $window || window;

        var query = wdw.location.search.substring(1);
        var params = query.split('&');
        params.forEach(function (p) {
            var keyVal = p.split('=');
            if (keyVal.length >= 2) {
                var key = keyVal[0].toLowerCase();
                var val = keyVal[1];

                switch (key) {
                    case 'trace':
                        setESConsoleTraceLevel(decodeURIComponent(val), null);
                        break;
                    case 'print':
                    case 'show':
                        addESTagToPrint(parseArrayish(decodeURIComponent(val)));
                        break;
                    case 'hide':
                        addESTagToNotPrint(parseArrayish(decodeURIComponent(val)));
                        break;
                    case 'include':
                        addESTagToLog(parseArrayish(decodeURIComponent(val)));
                        break;
                    case 'exclude':
                        addESTagToNotLog(parseArrayish(decodeURIComponent(val)));
                        break;
                    default:
                        break;
                }

            }
        });

        function parseArrayish(arrayish) {
            var values;

            if (arrayish === undefined) {
                return [];
            }

            // remove all quotes
            arrayish = arrayish.replace(/['"]+/g, '');

            var array = arrayish.match(/\[.*\]/);

            if (array) {
                values = array[0].substring(1, array[0].length - 1).split(',');
            } else {
                values = arrayish.split(',');
            }

            return values;
        }
    }

    /**
     * Adds the esconsole tags to be always included for printing. Included tags override the excluded tags.
     * @name addESTagToPrint
     * @function
     * @param tags {string|array} A string or an array of strings.
     * @example
     * addESTagToPrint('MISC');
     * addESTagToPrint(['this', 'that']);
     */
    function addESTagToPrint(tags) {
        if (typeof(tags) === 'string') {
            ESConsoleIncludedTags.push(tags.toUpperCase());
        } else if (tags instanceof Array) {
            tags.forEach(function (tag) {
                if (typeof(tag) === 'string') {
                    ESConsoleIncludedTags.push(tag.toUpperCase());
                }
            });
        }
        esconsole('Setting the tags to always show in the esconsole printing: ' + ESConsoleIncludedTags.toString(), 'meta', 0);
        return ESConsoleIncludedTags;
    }

    /**
     * Sets the esconsole tags to be excluded from printing. Note that the excluded tags may still be overridden by the always-included tags.
     * @name addESTagToNotPrint
     * @function
     * @param tags {string|array} A string or an array of strings.
     * @example
     * addESTagToNotPrint('MISC');
     * addESTagToNotPrint(['this', 'that']);
     */
    function addESTagToNotPrint(tags) {
        if (typeof(tags) === 'string') {
            ESConsoleExcludedTags.push(tags.toUpperCase());
        } else if (tags instanceof Array) {
            tags.forEach(function (tag) {
                if (typeof(tag) === 'string') {
                    ESConsoleExcludedTags.push(tag.toUpperCase());
                }
            });
        }
        esconsole('Setting the tags to be hidden in the esconsole printing: ' + ESConsoleExcludedTags.toString(), 'meta', 0);
        return ESConsoleExcludedTags;
    }


    /**
     * Sets the global trace level for the esconsole function. If esconsole() locally specifies a trace level, the global level is ignored.
     * @param traceLevel {number} 0/null: no trace, 1: print caller function name (if availalbe), 2: print caller function name and source code location, 3: print a longer source code location (may be linked), 4: print full stack trace.
     * @param [saveToCookie=false] {boolean} To be implemented.
     * @returns {string}
     */
    function setESConsoleTraceLevel(traceLevel, saveToCookie) {
        if (typeof(traceLevel) === 'number') {
            ESConsoleTraceLevel = traceLevel;
        } else if (!isNaN(parseInt(traceLevel))) {
            ESConsoleTraceLevel = parseInt(traceLevel);
        }
        return esconsole('Setting the esconsole trace level: ' + traceLevel, 'meta', 0);
    }


    /**
     * A custom console.log function for ES developers. Tags can be set and filtered from being printed as well as being recorded to the developer log.
     * @name esconsole
     * @function
     * @param message {string|number|object|function} A message, value, or object to be printed in the developer console. By default, the message is recorded in the developer log for up to the MAX_LOGMESSAGGES set in the interpreter.js. With certain tags, the message will be skipped from logging.
     * @param [tag='DEV'] {string|array|null} All characters are converted to the upper case. A null value or '<empty>' will hide the tag when printing. Using tags such as 'TEMP', 'EXCLUDE', and 'NOLOG' will prevent the message from being recorded in the developer log, which can be modified with setESTagToLog() or setESTagToNotLog(). When using multiple tags, if any one is set to be filtered out, the message will be not printed or logged.
     * @param [traceLevel=3] {number} 0/null: no trace, 1: print caller function name (if availalbe), 2: print caller function name and source code location, 3: print a longer source code location (may be linked), 4: print full stack trace.
     * @param [logLevel=1] {number} Overrides the logg 0: no logging regardless of the tag filtering. 1 (default): logged with the tag filtering taken into account. 2: always logged regardless of the tag filtering.
     *
     * @example
     * esconsole('hello world');
     * -> [DEV] hello world at (caller:file:line:char)
     *
     * @example
     * esconsole(value, 'debug', 1);
     * -> [DEBUG] {
 *      foo: 123,
 *      bar: 456
 * } @ caller function
     *
     * @example
     * esconsole('just checking', 'temp', 0);
     * -> [TEMP] just checking // This will not be logged.
     *
     * @example
     * esconsole('multiple tags', ['debug', 'util']);
     * -> [DEBUG][UTIL] multiple tags at ...
     *
     * @example
     * addESTagToNotPrint('UTIL');
     * * esconsole('multiple tags', ['debug', 'misc']);
     * -> [DEBUG][MISC] multiple tags at ...
     * esconsole('multiple tags', ['debug', 'util']);
     * -> no output (still logged)
     */
    function esconsole(message, tag, traceLevel, logLevel) {
        var log = '';
        var output;
        var TAG;
        var trace;
        var defaultTraceLevel = 3;
        var defaultIndentation = 4;
        var location = '';
        var messageIsError = false;

        // TODO: always set the trace level of logs to 2?

        if (message && message.constructor.name.match(/Error/g)) {
            messageIsError = true;
        }

        if (tag instanceof Array) {
            if (tag.length === 1) {
                if ([null, ''].indexOf(tag[0]) >= 0) {
                    TAG = '';
                } else {
                    if (typeof(tag[0]) === 'string') {
                        TAG = tag[0].toUpperCase();
                    } else {
                        TAG = 'DEV'
                    }
                    log += '[' + TAG + '] ';
                }
            } else if (tag.length > 1) {
                TAG = [];
                tag.forEach(function (t) {
                    if (typeof(t) === 'string') {
                        log += '[' + t.toUpperCase() + ']';
                        TAG.push(t.toUpperCase());
                    }
                });
                log += ' ';
            }
        } else {
            if ([null, ''].indexOf(tag) >= 0) {
                TAG = '';
            } else {
                if (typeof(tag) === 'string') {
                    TAG = tag.toUpperCase();
                } else {
                    TAG = 'DEV'
                }
                log += '[' + TAG + '] ';
            }
        }

        if (typeof(message) === 'object') {
            if (messageIsError) {
                log += message;

            } else {
                log += JSON.stringify(message, null, defaultIndentation);
            }
        } else if (typeof(message) === 'function') {
            log += message.toString(defaultIndentation);
        } else {
            log += message;
        }

        if (traceLevel === undefined || traceLevel === null) {
            if (typeof(ESConsoleTraceLevel) === 'number') {
                traceLevel = ESConsoleTraceLevel;
            } else {
                traceLevel = defaultTraceLevel;
            }
        } else if (!isNaN(parseInt(traceLevel))) {
            traceLevel = parseInt(traceLevel);
        } else {
            traceLevel = defaultTraceLevel;
        }

        if (logLevel === undefined) {
            logLevel = 1;
        } else {
            if (!isNaN(parseInt(logLevel))) {
                logLevel = parseInt(logLevel);
            }
        }

        if (traceLevel === 1) {
            if (esconsole.caller) {
                log += ' @ ' + esconsole.caller.name + '()';
            } else {
                log += ' @ ' + '<anonymous>';
            }
        }

        if (traceLevel === 2) {
            if (esconsole.caller) {
                log += ' @ ' + esconsole.caller.name + '()';
            } else {
                log += ' @ ' + '<anonymous>';
            }

            trace = (new Error()).stack.toString().split(/\r\n|\n/);
            if (trace[0] === 'Error') {
                location = trace[2];
            } else {
                location = trace[1];
            }

            location = location.match(/\/\w+\.js\:\d+\:\d+/);
            if (location) {
                log += ' @ ' + location[0].substring(1)
            }
        }

        if (traceLevel === 3) {
            trace = (new Error()).stack.toString().split(/\r\n|\n/);
            if (trace[0] === 'Error') {
                location = trace[2];
            } else {
                location = trace[1];
            }
            log += ' ' + location;
        }

        if (traceLevel === 4) {
            if (messageIsError) {
                log += ' ' + message.stack.toString();
            } else {
                log += ' ' + (new Error()).stack.toString();
            }
        }

        output = log;

        if (TAG instanceof Array) {
            var willShow = true;
            TAG.forEach(function (t) {
                if (ESConsoleExcludedTags.indexOf(t) > -1) {
                    willShow = false;
                }
                if (ESConsoleIncludedTags.indexOf(t) >= 0) {
                    willShow = true;
                }
            });
            if (willShow) {
                console.log(output);
            }
        } else {
            if ((ESConsoleExcludedTags.indexOf(TAG) === -1) || (ESConsoleIncludedTags.indexOf(TAG) >= 0)) {
                console.log(output);
            }
        }

        switch (logLevel) {
            case 0:
                break;
            case 1:
            default:
                ESLog(log, TAG);
                break;
            case 2:
                ESLog(log);
                break;
        }

        // For directly calling in the interactive dev console.
        return output;
    }

    /**
     * Same as the esconsole() function.
     * @name esconsole.log
     * @function
     * @memberOf esconsole
     */
    esconsole.log = function () {
        esconsole.apply(this, arguments);
    };

    /**
     * Explicitly adds developer log messages to the internal log array. Note that ESLog() is also called automatically at esconsole(msg, tag) for certain tags, so developers should usually avoid using this function.
     * @name ESLog
     * @function
     * @param logText {string} A message to be recorded in the log.
     * @param [tag=undefined] {string|array} Used mainly by esconsole() to filter the logging. If not present (or undefined), the input is is always logged.
     * @example
     * ESLog('[CAT] meow!');
     * EarSketch.Interpreter.getCompleteLog();
     * -> [..., .., '[CAT] meow!'];
     */
    function ESLog(logText, tag) {
        var TAG;
        if (tag === undefined) {
            REPORT_LOG.push(logText);
        } else if (typeof(tag) === 'string') {
            TAG = tag.toUpperCase();
            if ((ESLogExcludedTags.indexOf(TAG) === -1) || (ESLogIncludedTags.indexOf(TAG) >= 0)) {
                REPORT_LOG.push(logText);
            }
        } else if (tag instanceof Array) {
            var willLog = true;
            tag.forEach(function (t) {
                TAG = t.toUpperCase();
                if (ESLogExcludedTags.indexOf(TAG) > -1) {
                    willLog = false;
                }
                if (ESLogIncludedTags.indexOf(TAG) >= 0) {
                    willLog = true;
                }
            });
            if (willLog) {
                REPORT_LOG.push(logText);
            }
        }
    }

    /**
     * Sets the esconsole tags to be always included for logging. Included tags override the excluded tags.
     * @name addESTagToLog
     * @function
     * @param tags {string|array} A string or an array of strings.
     * @example
     * addESTagToLog('MISC');
     * addESTagToLog(['this', 'that']);
     */
    function addESTagToLog(tags) {
        if (typeof(tags) === 'string') {
            ESLogIncludedTags.push(tags.toUpperCase());
        } else if (tags instanceof Array) {
            tags.forEach(function (tag) {
                if (typeof(tag) === 'string') {
                    ESLogIncludedTags.push(tag.toUpperCase());
                }
            });
        }

        return esconsole('Setting the tags to be always logged: ' + ESLogIncludedTags, 'meta', 0);
    }

    /**
     * Sets the esconsole tags to be excluded from logging. Note that the excluded tags may still be overridden by the always-included tags.
     * @name addESTagToNotLog
     * @function
     * @param tags {string|array} A string or an array of strings.
     * @example
     * addESTagToNotLog('MISC');
     * addESTagToNotLog(['this', 'that']);
     */
    function addESTagToNotLog(tags) {
        if (typeof(tags) === 'string') {
            ESLogExcludedTags.push(tags.toUpperCase());
        } else if (tags instanceof Array) {
            tags.forEach(function (tag) {
                if (typeof(tag) === 'string') {
                    ESLogExcludedTags.push(tag.toUpperCase());
                }
            });
        }

        return esconsole('Setting the tags to be excluded from loggin: ' + ESLogExcludedTags, 'meta', 0);
    }

    esconsole.getURLParameters = getURLParameters;
    esconsole.setESConsoleTraceLevel = setESConsoleTraceLevel;
    esconsole.addESTagToPrint = addESTagToPrint;
    esconsole.addESTagToNotPrint = addESTagToNotPrint;
    esconsole.ESLog = ESLog;
    esconsole.addESTagToLog = addESTagToLog;
    esconsole.addESTagToNotLog = addESTagToNotLog;

    $window.esconsole = esconsole;

    return esconsole;
}]);
