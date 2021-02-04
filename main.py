import urllib.parse
import requests
import sys
import json
from tests import TESTS
from config import BASE_URL

def print_test(url, method, result, test_name, wanted, status_code, data, text, minimal=False):
    try:
        text = json.dumps(json.loads(text), indent=4)
    except:
        text = "\tUNIT TEST\n\tEXCEPTION: API Responded with a non-JSON response."

    if minimal == True:
        print('--------------------------------------------------------------------------------')
        print('test:   ' + test_name)
        print('url:    ' + url)
        print('method: ' + method)
        print('wanted: ' + str(wanted))
        print('result: ' + result)
    else:
        print('--------------------------------------------------------------------------------')
        print('test:   ' + test_name)
        print('method: ' + method)
        print('url:    ' + url)
        print('')
        print('wanted: ' + str(wanted))
        print('got:    ' + str(status_code))
        print('result: ' + result)
        print('--------------------------------------------------------------------------------')
        print('')
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('method:   ' + method)
        print('status:   ' + str(status_code))
        print('request:  ' + test_name)
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('')
        print(json.dumps(data, indent=4))
        print('')
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('status:    ' + str(status_code))
        print('response:')
        print('- - - - - - - - - - - - - - - - - - - - - - ')
        print('')
        print(text)
        print('')
    with open('runs.txt', 'a') as f:
        f.write('%s: %s %s %s\n' % (result, label, method, status_code))
        f.close()

def print_summary(tests_run, tests_passed, tests_failed):
    print('--------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------')
    if tests_run == 0:
        print('\033[91mno matching tests found\033[0m')
    elif tests_failed == 0:
        print("""Finshed
    tests ran:      %s
    \033[92mPASSED\033[0m          %s
    FAILED:         0""" % (tests_run, tests_passed))
        print('\033[92mAll tests PASSED\033[0m')
    else:
        print("""Finshed
    tests ran:      %s
    PASSED:         %s
    \033[91mFAILED:         %s \033[0m
        """ % (tests_run, tests_passed, tests_failed))

def run_method_status(chosen_label, chosen_method, chosen_status, minimal=True):
    
    # Count tests run.
    tests_run = 0
    tests_failed = 0
    tests_passed = 0

    # You need to choose a test label.
    if chosen_label is None:
        print('No label specified. Aborting.')
        return

    # Filiter all tests with matching label.
    tests = list(filter(lambda test:
        test.get('label') == chosen_label, TESTS))
    if len(tests) == 0:
        print('no tests with that label')
        return

    # For all tests...
    for test in tests:
        URL = BASE_URL + test['url']
        method = chosen_method.upper()
        if len(method) == 1:
            if method == 'G':
                method = 'GET'
            if method == 'P':
                method = 'POST'
            if method == 'D':
                method = 'DELETE'
        METHOD = test.get(method)

        if METHOD is not None:
            status = chosen_status
            if len(status) == 1:
                status += '00'
            METHOD_STATUSs = METHOD.get(status)

            if METHOD_STATUSs is not None:

                for test_name, METHOD_STATUS in METHOD_STATUSs.items():
                
                    url = URL
                    path_vars = METHOD_STATUS.get('path')
                    if path_vars is not None:
                        for key, val in path_vars.items():
                            url = url.replace(key,val)

                    data = METHOD_STATUS.get('data')
                    if method == 'GET': 
                        if data is not None:
                            query = urllib.parse.urlencode(
                                METHOD_STATUS.get('data'))
                            url += '?' + query
                    cookies = METHOD_STATUS.get('cookies')
                    status_code = None
                    text = None

                    if method == 'POST':
                        response = requests.post(url, data, cookies=cookies)
                    elif method == 'GET':
                        response = requests.get(url, data, cookies=cookies)
                    elif method == 'DELETE':
                        response = requests.delete(url, cookies=cookies)
                    else:
                        raise Exception("Unknown HTTP request method '%s'." % method)

                    status_code = response.status_code
                    text = response.text

                    if str(status_code) == status:
                        print_test(url, method, '\033[92mPASSED\033[0m', test_name, status, status_code, data, text,
                                minimal=minimal)
                        tests_run += 1
                        tests_passed += 1
                    else:
                        print_test(url, method, '\033[91mFAILED\033[0m', test_name, status, status_code, data, text,
                                minimal=minimal)
                        tests_run += 1
                        tests_failed += 1

    # Don't print if we're running multiple tests because
    # the summary will print at the end.
    if minimal == False:
        print_summary(tests_run, tests_passed, tests_failed)

    return tests_run, tests_passed, tests_failed

# Run all of the tests with this label (for all specified
# HTTP methods and HTTP status codes). 
def run_label(label, minimal=True):
    tests_run = 0
    tests_failed = 0
    tests_passed = 0
    tests = list(filter(lambda test:
        test.get('label') == label, TESTS))
    for test in tests:
        for method, val in test.items():
            if method in ['POST','GET','DELETE']:
                for status, test in val.items():
                    _tests_run, _tests_passed, _tests_failed = run_method_status(
                        label, method, status, minimal=True)
                    tests_run += _tests_run
                    tests_passed += _tests_passed
                    tests_failed += _tests_failed
    if minimal == False:
        print_summary(tests_run, tests_passed, tests_failed)
    return tests_run, tests_passed, tests_failed

# All the tests I've already done.
DONE_LIST = ['cir_pro_tim','cir_pro','cir_pro_tim_page',
        'cir_pro_fr',
        'cir_pro_fing',
        'cir_pro_frs',
        'cir_pro_photos',
        'cir_pro_albums',
        'cir_pro_videos',
        'cir_pro_groups',
        'cir_pro_events',
        'cir_pag',
        'cir_pag_page',
        'cir_pag_lik_page',
        'cir_pag_man_page',
        'cir_pag_pro',
        'cir_pag_pro_tim',
        'cir_pag_pro_photos',
        'cir_pag_pro_videos',
        'cir_grp',
        'cir_grp_pro_tim', 
        'cir_grp_pro',
        'cir_grp_man_page',
        'cir_grp_jnd_page',
        'cir_grp_page',
        'cir_grp_pro_videos',
        'cir_grp_pro_albums',
        'cir_grp_pro_photos',
        'cir_grp_pro_mbr_page',
        'cir_grp_pro_tim_page',
        'cir_evt',
        'cir_evt_page',
        'cir_evt_ivt_page',
        'cir_evt_int_page',
        'cir_evt_gng_page',
        'cir_evt_man_page',
        'cir_evt_pro',
        'cir_evt_pro_tim', 
        'cir_evt_pro_tim_page',
        'cir_evt_pro_int_page',
        'cir_evt_pro_inv_page',
        'cir_evt_pro_gng_page',
        'cir_evt_pro_videos',
        'cir_evt_pro_albums',
        'cir_evt_pro_photos',
        'cir_post',
        'cir_tim',
        'cir_tim_page',
        'cir_tim_pop_page',
        'cir_tim_svd_page',
        'cir_tim_prd_page',
        'cir_tim_art_page',
        'cir_msg',
        'cir_msg_cnv',
        'cir_msg_cnv_msg',
        'cor_set',
        'cor_set_pro_bas',
        'cor_set_pro_wrk',
        'cor_set_pro_loc',
        'cor_set_pro_edu',
        'cor_set_pro_soc',
        'cor_set_sec_pas',
        'cor_set_sec_ses',
        'cor_set_pri',
        'cor_set_not',
        'cor_set_ver',
        'cor_set_del',
        'cir_sch_pos',
        'cir_sch_hsh',
        'cir_sch_art',
        'cir_sch_usr',
        'cir_sch_pag',
        'cir_sch_grp',
        'cir_sch_evt',
        'cor_signup',
        'cor_signin',
        ]

def print_usage():
    print("""Usage:
      $ python3 main.py [label] +| ([method|status] [status|method])")
Examples:
    Dump the current spec:
      $ python3 main.py dumpspec > spec.json
    Run all tests in the 'donelist':
      $ python3 main.py donelist
    Run a single test for a label, method, and status:
      $ python3 main.py [label] [method] [status]
    Run all tests for a label:
      $ python3 main.py [label]""")
    exit()

if __name__ == '__main__':

    print(chr(27) + "[2J")

    # Print args
    if len(sys.argv) == 1:
        print_usage()

    # Get the label you want to run. 
    label = sys.argv[1]

    if label == 'dumpspec':
        print(json.dumps(TESTS, indent=4))
        exit()

    # Run all previously done tests.
    if label == 'donelist':
        tests_run = 0
        tests_failed = 0
        tests_passed = 0
        for _label in DONE_LIST:
            _tests_run, _tests_passed, _tests_failed = run_label(_label)
            tests_run += _tests_run
            tests_passed += _tests_passed
            tests_failed += _tests_failed
        print_summary(tests_run, tests_passed, tests_failed)
        exit()
    # Not specifying an HTTP method or status will run all tests with that label.
    if len(sys.argv) == 2:
        run_label(label)
        exit()

    # Print args again if missuse.
    if len(sys.argv) < 4:
        print_usage()

    # Parse the next args, but let them swap order. Allow the arguments
    # 2 and 4 to be short for the common 200 and 400 http codes.
    # For example:
    #
    #       $test label POST 200
    #
    # can also be run as:
    #
    #       $test label p 2
    #       $test label 2 p
    # 
    # Anything more specific must specify either 'post','get','delete' and
    # the exact HTTP status code, i.e. 405, 401, etc. Other HTTP methods
    # are not supported.
    one = sys.argv[2]
    two = sys.argv[3]
    if one[0] in ['2','4']:
        status = one
        method = two
    else:
        method  = one
        status = two

    # Run the tests.
    run_method_status(label, method, status, minimal=False)
