import sys
import json


def fillTests(tests, testResults):
    for test in tests:
        testResult = getResultForTest(test['id'], testResults)
        if 'value' in test.keys():
            test.update({'value': testResult})
        childrenTests = test.get('values', [])
        if childrenTests:
            fillTests(childrenTests, testResults)


def getResultForTest(testId, testResults):
    for res in testResults:
        if res['id'] == testId:
            return res.get('value', '')
    return ''


def main():
    with open(sys.argv[2]) as jsonFile:
        valuesData = json.load(jsonFile)
        testResults = valuesData.get('values', [])

    with open(sys.argv[1]) as jsonFile:
        valuesData = json.load(jsonFile)
        tests = valuesData.get('tests', [])

        fillTests(tests, testResults)
        resultDict = {'tests': tests}

    with open('report.json', 'w') as jsonFile:
        json.dump(resultDict, jsonFile, indent=1)


if __name__ == '__main__':
    main()
