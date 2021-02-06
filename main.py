import urllib.parse
import requests
import sys
import json
from tests import TESTS
from config import BASE_URL

def print_test(url, method, result, test_name, wanted, status_code, data, text, passed=None, **kwargs):

    if kwargs.get('only_200') == True:
        if passed == True:
            if status_code != 200:
                return
    try:
        text = json.dumps(json.loads(text), indent=4)
    except:
        text = "\tUNIT TEST\n\tEXCEPTION: API Responded with a non-JSON response."

    if kwargs.get('minimal') == True:
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

def print_summary(tests_run, tests_passed, tests_failed, **kwargs):
    if kwargs.get('only_get') == True:
        return
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

def run_method_status(chosen_label, chosen_method, chosen_status, **kwargs):
    
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
               
                    # Check mode
                    mode = kwargs.get('mode')
                    only_get = kwargs.get('only_get')

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

                        if only_get == True:
                            continue
                        # Check mode for 'all' run.
                        if mode == 'ONLY_DELETE':
                            continue

                        response = requests.post(url, data, cookies=cookies)

                    elif method == 'GET':

                        # Check mode for 'all' run.
                        if mode == 'ONLY_DELETE':
                            continue

                        response = requests.get(url, data, cookies=cookies)

                    elif method == 'DELETE':

                        if only_get == True:
                            continue
                        if mode == 'SKIP_DELETE':
                            continue

                        response = requests.delete(url, cookies=cookies)

                    else:
                        raise Exception("Unknown HTTP request method '%s'." % method)

                    status_code = response.status_code
                    text = response.text

                    if str(status_code) == status:
                        print_test(url, method, '\033[92mPASSED\033[0m', test_name,
                                status, status_code, data, text, passed=True,
                                **kwargs)
                        tests_run += 1
                        tests_passed += 1
                    else:
                        print_test(url, method, '\033[91mFAILED\033[0m', test_name,
                                status, status_code, data, text, passed=True,
                                **kwargs)
                        tests_run += 1
                        tests_failed += 1

    # Don't print if we're running multiple tests because
    # the summary will print at the end.
    if kwargs.get('minimal') == False:
        print_summary(tests_run, tests_passed, tests_failed, **kwargs)

    return tests_run, tests_passed, tests_failed

# Run all of the tests with this label (for all specified
# HTTP methods and HTTP status codes). 
def run_label(label, **kwargs):
    tests_run = 0
    tests_failed = 0
    tests_passed = 0
    failed_labels = {}
    tests = list(filter(lambda test:
        test.get('label') == label, TESTS))
    for test in tests:
        for method, val in test.items():
            if method in ['POST','GET','DELETE']:
                for status, test in val.items():
                    _tests_run, _tests_passed, _tests_failed = run_method_status(
                        label, method, status, **kwargs)
                    tests_run += _tests_run
                    tests_passed += _tests_passed
                    tests_failed += _tests_failed
                    if _tests_failed > 0:
                        if label not in failed_labels:
                            failed_labels[label] = []
                        failed_labels[label].append({method: status})
    if kwargs.get('minimal') == False:
        print_summary(tests_run, tests_passed, tests_failed, **kwargs)
    return tests_run, tests_passed, tests_failed, failed_labels

# All the tests I've already done.
DONE_LIST = [
        'cir_pro_tim',
        'cir_pro_tim_page',
        'cir_pro',
        'cir_pro_act_report',
        'cir_pro_act_poke',
        'cir_pro_act_block',
        'cir_pro_act_unfollow',
        'cir_pro_act_follow',
        'cir_pro_act_frn_req',
        'cir_pro_act_unfrn_req',
        'cir_pro_act_frn_req_conf',
        'cir_pro_fr',
        'cir_pro_fing',
        'cir_pro_frs',
        'cir_pro_photos',
        'cir_pro_albums',
        'cir_pro_videos',
        'cir_pro_groups',
        'cir_pro_events',
        'cir_pag',
        'cir_pag_pro_act_like',
        'cir_pag_pro_act_unlike',
        'cir_pag_page',
        'cir_pag_lik_page',
        'cir_pag_man_page',
        'cir_pag_pro',
        'cir_pag_pro_tim',
        'cir_pag_pro_tim_page',
        'cir_pag_pro_photos',
        'cir_pag_pro_videos',
        'cir_grp',
        'cir_grp_pro_act_join',
        'cir_grp_pro_act_unjoin',
        'cir_grp_pro_act_like',
        'cir_grp_pro_act_unlike',
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
        'cir_evt_pro_act_going',
        'cir_evt_pro_act_ungoing',
        'cir_evt_pro_act_interested',
        'cir_evt_pro_act_uninterested',
        'cir_evt_pro_act_like',
        'cir_evt_pro_act_unlike',
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
        'cir_pep_page',
        'cir_pep_frn_req_page',
        'cir_pep_frn_req_snt_page',
        'atr_msg',
        'atr_msg_cnv',
        'atr_msg_cnv_msg',
        'atr_trn',
        'atr_bkm',
        'atr_pro',
        'atr_pro_tim',
        'atr_pro_tim_page',
        'atr_pro_act_report',
        'atr_pro_act_poke',
        'atr_pro_act_block',
        'atr_pro_act_unfollow',
        'atr_pro_act_follow',
        'atr_pro_act_frn_req',
        'atr_pro_act_unfrn_req',
        'atr_pro_act_frn_req_conf',
        'atr_pro_fr',
        'atr_pro_fing',
        'atr_pro_frs',
        'atr_pro_photos',
        'atr_pro_albums',
        'atr_pro_videos',
        'atr_post',
        'atr_post_act',
        'atr_tim',
        'atr_tim_page',
        'atr_sch_pos',
        'atr_sch_hsh',
        'atr_sch_art',
        'atr_sch_usr',
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

def dump_spec():
    # Dump the 200s for the spec.
    spec = {}
    for test in TESTS:
        spec[test['url']] = {}
        if test.get('POST') is not None:
            spec[test['url']]['POST'] = test.get('POST').get('200')
        if test.get('GET') is not None:
            spec[test['url']]['GET'] = test.get('GET').get('200')
        if test.get('DELETE') is not None:
            spec[test['url']]['DELETE'] = test.get('DELETE').get('200')
    string = json.dumps(spec, indent=4)
    with open('spec.json','w') as f:
        f.write(string)
        f.close()

def arg(index):
    if index >= len(sys.argv):
        return None
    return sys.argv[index]

if __name__ == '__main__':

    print(chr(27) + "[2J")

    # Print args
    if len(sys.argv) == 1:
        print_usage()

    # Get the label you want to run. 
    label = sys.argv[1]

    if label == 'dumpspec':
        dump_spec()
        exit()
    if label == 'dumptests':
        # Dump the all the tests.
        print(json.dumps(TESTS, indent=4))
        exit()

    # Run all previously done tests.
    if label == 'all':
        tests_run = 0
        tests_failed = 0
        tests_passed = 0
        failed_labels = []
        run_conf = {
            'only_200': False,
            'only_get': False,
            'minimal': True,
        }

        if arg(2) == 'page_write':
            DONE_LIST = list(filter(lambda lab: lab[0:7] == 'cir_pag', DONE_LIST))

        if arg(2) == 'page_read':
            DONE_LIST = list(filter(lambda lab: lab[0:11] == 'cir_pag_pro', DONE_LIST))
            run_conf = {
                'only_200': True,
                'only_get': True,
                'minimal': False,
            }

        # Run the labels skipping DELETE
        for _label in DONE_LIST:
            _tests_run, _tests_passed, _tests_failed, _failed_labels = run_label(
                    _label, mode='SKIP_DELETE', **run_conf)
            tests_run += _tests_run
            tests_passed += _tests_passed
            tests_failed += _tests_failed
            for _failed_label, methods in _failed_labels.items():
                failed_labels.append({_failed_label: methods})
        # Run the labels for only DELETE
        for _label in DONE_LIST:
            _tests_run, _tests_passed, _tests_failed, _failed_labels = run_label(
                    _label, mode='ONLY_DELETE', **run_conf)
            tests_run += _tests_run
            tests_passed += _tests_passed
            tests_failed += _tests_failed
            for _failed_label, methods in _failed_labels.items():
                failed_labels.append({_failed_label: methods})
        # Summary
        print_summary(tests_run, tests_passed, tests_failed)
        if len(failed_labels) > 0:
            print("Failed Tests:")
            with open('failed_tests.txt','w') as f:
                string = json.dumps(failed_labels, indent=4)
                f.write(string)
                f.close()
                print(string)
        # Dump the spec with the live working variables.
        dump_spec()
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
