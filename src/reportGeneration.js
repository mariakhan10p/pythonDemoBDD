var reporter = require('cucumber-html-reporter');

var date = new Date().getTime()

var options = {
        theme: 'bootstrap',
        jsonFile: __dirname + '\\reports\\JsonReport.json',
        output: __dirname + '\\reports\\htmlReport\\'+ date +'\\report.html',
        reportSuiteAsScenarios: true,
        scenarioTimestamp: true,
        launchReport: true,
        metadata: {
            "Test Environment": "Local"
        },
        name : "tests"
    };

    reporter.generate(options);