
'''-------------------------------------------------------------------------
Copyright IBM Corp. 2015, 2015 All Rights Reserved
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
Limitations under the License.
-------------------------------------------------------------------------'''

import unittest
import mock
import re

from dragonclient.v1 import dr

DONE = 200


class api(object):

    def __init__(self):

        self.project = 'admin'

    def json_request(self, method, url, **kwargs):

        # if (method == 'GET' and url.startswith('admin/resources/2f3b9a41-7bc'
        #                                         'b-46fb-82dc-1a5929e5a026')):
        #    if kwargs != {}:
        #        return DONE, {'dummy': 'dumm'}

        if (method == 'GET' and
            url.startswith('admin/resources/'
                           '2f3b9a41-7bcb-46fb-82dc-1a5929e5a026')):
            body_resp = {'id': 1,
                         'name': 'instance1',
                         'created_at': '2014-10-29-17.57',
                         'resource_type_id': 1}
            return DONE, body_resp

        elif (method == 'GET' and url == 'admin/resources'):
            body_resp = {'id': 'f76422ba-a421-4520-aa4f-7fd0ea7d86ed',
                         'name': 'my_vol',
                         'resource_type_id': 2,
                         'tenant_id': 'c9a54702410e4573bd45909d90ada12c',
                         'created_at': '2014-08-23T14:26:28.794125'}
            return DONE, body_resp

        elif (method == 'GET' and url.startswith('admin/actions')):
            body_resp = {'id': 2, 'name': 'Image Snap', 'resource_type_id': 1,
                         'class_name': 'dragon.workload_policy.actions.plugins\
                         .instance_snapshot_action.InstanceSnapshotActionc',
                         'created_at': '2014-08-23T14:26:28.794125'}
            return DONE, body_resp

        elif (method == 'POST' and
              url.startswith('admin/workload_policies')):
            body_resp = {'id': 'c9a54702410e4573bd45909d90ada12c',
                         'name': 'policy_name',
                         'tenant_id': 'c9a54702410e4573bd45909d90ada12c',
                         'created_at': '2014-08-23T14:26:28.794125'}
            return DONE, body_resp

        elif (method == 'POST' and url.startswith('admin/protect')):
            return DONE, {'dummy': 'dumm'}

        elif (method == 'POST' and url.startswith('admin/recover')):
            if kwargs != {} and 'body' in kwargs:
                if kwargs['body']['container_name'] == 'container_name':
                    return DONE, {'dummy': 'dumm'}
                else:
                    return None
            else:
                return None

        elif (method == 'DELETE' and
              url.startswith('admin/workload_policies')):
            return DONE, {'dummy': 'dumm'}

        elif (method == 'POST' and url.startswith('admin/resources')):
            if kwargs != {}:
                return DONE, {'dummy': 'dumm'}
            else:
                return None

        elif (method == 'POST' and
              url.startswith('admin/resource_action')):
            return DONE, {'dummy': 'dumm'}

        elif (method == 'PUT' and
              url.startswith('admin/policy')):
            return DONE, {'dummy': 'dumm'}

        elif (method == 'DELETE' and
              url.startswith('admin/resource_action')):
            return DONE, {'dummy': 'dumm'}

        elif (method == 'GET' and
              url.startswith('admin/workload_policies/workload_policy_id/'
                             'resource_actions')):
            body_resp = {'id': 1,
                         'resource_id': '2f3b9a41-7bcb-46fb-82dc'
                         '-1a5929e5a026',
                         'action_id': 1,
                         'workload_policy_id': 'workload_policy_id',
                         'created_at': '2014-10-29-17.57'}
            return DONE, body_resp

        elif (method == 'GET' and
              url.startswith('admin/workload_policies/'
              'workload_policy_id/executions')):
            body_resp = {'id': 1,
                         'created_at': '2014-10-29-17.57',
                         'workload_policy_id': 'workload_policy_id'}
            return DONE, body_resp

        elif (method == 'GET' and
              url.startswith('admin/workload_policies/workload_policy_id')):
            body_resp = {'id': 'workload_policy_id',
                         'name': 'vol_only',
                         'tenant_id': 'c9a54702410e4573bd45909d90ada12c',
                         'created_at': '2014-08-23T14:26:28.794125'}
            return DONE, body_resp

        elif (method == 'GET' and
              url.startswith('admin/workload_policies')):
            body_resp = {'id': '5c8446a5-4356-4d24-9946-75c2529ce096',
                         'name': 'policy_name',
                         'tenant_id': 'c9a54702410e4573bd45909d90ada12c',
                         'created_at': '2014-08-23T14:26:28.794125'}
            return DONE, body_resp

        elif (method == 'GET' and
              url.startswith('admin/policy_executions/policy_execution_id')):
            body_resp = {'id': 1,
                         'status': 'CREATED',
                         'workload_policy_id': 'workload_policy_id'}
            return DONE, body_resp

        elif (method == 'GET' and
              url.startswith('admin/policy_executions')):
            body_resp = {'id': 1,
                         'created_at': '2014-10-29-17.57',
                         'workload_policy_id': 'workload_policy_id'}
            return DONE, body_resp


class FakeManager(object):

    def __init__(self, api):
        self.api = api


class TestApi(unittest.TestCase):

    @mock.patch("dragonclient.common.base.Manager")
    def setUp(self, _manager_replace):
        a = api()
        _manager_replace.return_value = FakeManager(a)

    def assertRegexpMatches(self, text, expected_regexp, msg=None):
        """Fail the test unless the text matches the regular expression."""
        if isinstance(expected_regexp, basestring):
            expected_regexp = re.compile(expected_regexp)
        if not expected_regexp.search(text):
            msg = msg or "Regexp didn't match"
            msg = '%s: %r not found in %r' % (msg, expected_regexp.pattern,
                                              text)
            raise self.failureException(msg)

    def test_list_resources(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}
        body = self.dr.list_resources(**kwargs)

        fields = ['id', 'name', 'resource_type_id', 'tenant_id', 'created_at']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_list_actions(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}
        body = self.dr.list_actions('1', **kwargs)

        fields = ['id', 'name', 'class_name', 'resource_type_id', 'created_at']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_create_policy(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        body =\
            self.dr.create_workload_policy('policy_name',
                                           'c9a54702410e4573bd45909d90ada12c',
                                           **kwargs)

        # self.assertTrue(body["id"] == 'c9a54702410e4573bd45909d90ada12c')
        fields = ['id', 'name', 'tenant_id', 'created_at']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_list_workload_policies(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        body = self.dr.list_workload_policies(**kwargs)

        fields = ['id', 'name', 'tenant_id', 'created_at']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_get_workload_policy(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        body = self.dr.get_workload_policy('workload_policy_id', **kwargs)

        fields = ['id', 'name', 'tenant_id', 'created_at']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_delete_workload_policy(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        resp = self.dr.delete_workload_policy('workload_policy_id', **kwargs)

        self.assertTrue(resp == DONE)

    def test_protect(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}
        kwargs['body'] = {}
        kwargs['body']['consistent'] = True

        resp = self.dr.protect('workload_policy_id', **kwargs)

        self.assertTrue(resp == DONE)

    def test_recover(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        resp = self.dr.recover('container_name', **kwargs)

        self.assertTrue(resp == DONE)

    def test_create_resource(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        resp = self.dr.create_resource('2f3b9a41-7bcb-46fb-82dc-1a5929e5a026',
                                       "test1", 2, **kwargs)

        self.assertTrue(resp == DONE)

    def test_get_resource(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        body = self.dr.get_resource('2f3b9a41-7bcb-46fb-82dc-1a5929e5a026',
                                    **kwargs)

        fields = ['id', 'name', 'resource_type_id', 'created_at']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_create_resource_action(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        resp = self.dr.create_resource_action(
            '2f3b9a41-7bcb-46fb-82dc-1a5929e5a026',
            2, 'workload_policy_id', **kwargs)

        self.assertTrue(resp == DONE)

    def test_update_resource_action(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}
        resp = self.dr.update_resource_action(
            'workload_policy_id',
            '2f3b9a41-7bcb-46fb-82dc-1a5929e5a026', 1, 2, **kwargs)

        self.assertTrue(resp == DONE)

    def test_delete_resource_action(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        tuple_id = 1
        resp = self.dr.delete_resource_action(tuple_id, **kwargs)

        self.assertTrue(resp == DONE)

    def test_get_policy_resource_actions(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        body = self.dr.get_policy_resource_actions('workload_policy_id',
                                                   **kwargs)

        fields = ['id', 'resource_id', 'action_id', 'workload_policy_id',
                  'created_at']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_list_policy_executions(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        body = self.dr.list_policy_executions('workload_policy_id', **kwargs)

        fields = ['id', 'created_at', 'workload_policy_id']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)

    def test_get_policy_executions(self):

        self.api = api()
        self.dr = dr.DRManager(self.api)
        kwargs = {}

        body = self.dr.get_policy_executions('policy_execution_id', **kwargs)

        fields = ['id', 'status', 'workload_policy_id']
        key_list = body.keys()
        key_string = ''
        key_string = key_string.join(key_list)
        for r in fields:
            self.assertRegexpMatches(key_string, r)
