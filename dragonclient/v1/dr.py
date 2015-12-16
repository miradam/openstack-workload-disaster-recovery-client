
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

from dragonclient.common import base


DEFAULT_PAGE_SIZE = 20


class DR(base.Resource):
    def __repr__(self):
        return "<DR %s>" % self._info

    def update(self, **fields):
        self.manager.update(self, **fields)

    def delete(self):
        return self.manager.delete(self)

    def data(self, **kwargs):
        return self.manager.data(self, **kwargs)


class DRManager(base.Manager):
    resource_class = DR

    def protect(self, workload_policy_id, **kwargs):

        if 'body' not in kwargs:
            body = {}
            body['consistent'] = False
        else:
            body = kwargs['body']

        resp, body = self.api.json_request(
            'POST', '%s/protect/%s'
            % (self.api.project, workload_policy_id), body=body)
        return resp

    def recover(self, container_name, **kwargs):

        if 'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']
        body['container_name'] = container_name

        resp, body = self.api.json_request(
            'POST', '%s/recover' % (self.api.project), body=body)
        return resp

    def list_actions(self, resource_type, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/actions/%s'
            % (self.api.project, resource_type))

        return body

    def list_resources(self, **kwargs):

        if'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']

        resp, body = self.api.json_request(
            'GET', '%s/resources' % self.api.project, body=body)

        return body

    def create_workload_policy(self, policy_name, tenant_id, **kwargs):

        if 'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']

        body['name'] = policy_name
        body['tenant_id'] = tenant_id

        resp, body = self.api.json_request(
            'POST', '%s/workload_policies'
            % self.api.project, body=body)

        return body

    def list_workload_policies(self, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/workload_policies' % self.api.project)

        return body

    def get_workload_policy(self, workload_policy_id, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/workload_policies/%s'
            % (self.api.project, workload_policy_id))

        return body

    def delete_workload_policy(self, workload_policy_id, **kwargs):

        resp, body = self.api.json_request(
            'DELETE', '%s/workload_policies/%s'
            % (self.api.project, workload_policy_id))

        return resp

    def create_resource(self, resource_id, resource_name,
                        resource_type_id, **kwargs):

        if 'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']

        body['resource_id'] = resource_id
        body['resource_name'] = resource_name
        body['resource_type_id'] = resource_type_id
        body['tenant_id'] = self.api.project

        resp, body = self.api.json_request(
            'POST', '%s/resources' % (self.api.project), body=body)
        return resp

    def get_default_action_for_resource_type(self, resource_type_id, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/get_default_action_for_resource_type/%s'
            % (self.api.project, resource_type_id))

        return body

    def get_resource(self, resource_id, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/resources/%s' % (self.api.project, resource_id))

        return body

    def get_policy_resource_action(self, workload_policy_id,
                                   resource_id, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/workload_policies/%s/resources/%s/action'
            % (self.api.project, workload_policy_id, resource_id))

        return body

    def create_resource_action(
            self, resource_id, action_id,
            workload_policy_id, **kwargs):

        if 'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']

        body['action_id'] = action_id
        body['workload_policy_id'] = workload_policy_id

        resp, body = self.api.json_request(
            'POST', '%s/resource_action/%s'
            % (self.api.project, resource_id), body=body)
        return resp

    def update_resource_action(self, workload_policy_id, resource_id,
                               tuple_id, action_id, **kwargs):

        if 'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']

        body['tuple_id'] = tuple_id
        body['action_id'] = action_id
        body['workload_policy_id'] = workload_policy_id
        body['resource_id'] = resource_id

        resp, body = self.api.json_request(
            'PUT', '%s/policy/%s/resource/%s/resource_action/%s'
            % (self.api.project, workload_policy_id, resource_id,
               tuple_id), body=body)
        return resp

    def delete_resource_action(self, tuple_id, **kwargs):

        if 'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']

        resp, body = self.api.json_request(
            'DELETE', '%s/resource_action/%s'
            % (self.api.project, tuple_id), body=body)

        return resp

    def get_policy_resource_actions(self, workload_policy_id,
                                    **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/workload_policies/%s/resource_actions'
            % (self.api.project, workload_policy_id))

        return body

    def set_policy_executions(self, workload_policy_id, **kwargs):

        if 'body' not in kwargs:
            body = {}
        else:
            body = kwargs['body']

        body['workload_policy_id'] = workload_policy_id

        resp, body = self.api.json_request(
            'GET', '%s/set_policy_executions%s'
            % (self.api.project, workload_policy_id), body=body)

        return resp

    def list_policy_executions(self, workload_policy_id, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/workload_policies/%s/executions'
            % (self.api.project, workload_policy_id))

        return body

    def get_policy_executions(self, policy_execution_id, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/policy_executions/%s'
            % (self.api.project, policy_execution_id))

        return body

    def get_policy_execution_actions(self, policy_execution_id, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/policy_executions/%s/actions'
            % (self.api.project, policy_execution_id))

        return body

    def recovery_list_policies(self, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/recovery/policies' % (self.api.project))
        return body

    def recovery_list_policy_executions(self, policy_name, **kwargs):

        resp, body = self.api.json_request(
            'GET', '%s/recovery/policies/%s/executions'
            % (self.api.project, policy_name))
        return body
