
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

from dragonclient.common import utils


@utils.arg('id1', metavar='<Workload_policy_id>',
           help='ID of workload policy.')
@utils.arg('--consistent', metavar='<true/false>',
           help='consistent protect of instance and its volumes')
def do_protect(drc, args={}):

    """-  protect a given policy
         :param: [optional parameter] consistent protect (true/ false)
         :param: ID of workload policy
         :rtype: none
    """
    kwargs = {}
    kwargs['body'] = {}
    if args.consistent == 'true':
        kwargs['body']['consistent'] = True
    else:
        kwargs['body']['consistent'] = False

    drc.dr.protect(args.id1, **kwargs)


@utils.arg('id1', metavar='<NAME of container >',
           help='Name of container to recover from .')
def do_recover(drc, args={}):

    """- recover from a given container
         :param : Name of container to recover from
         :rtype: none
    """
    kwargs = {}
    drc.dr.recover(args.id1, **kwargs)


def do_list_resources(drc, args={}):

    """- list all resources
          :param: none
          :rtype:  list of resources  (instances, volumes etc.)
    """

    kwargs = {}
    resources = drc.dr.list_resources(**kwargs)

    fields = ['id', 'name', 'resource_type_id', 'tenant_id', 'created_at']
    local_print(resources, fields)


@utils.arg('id1', metavar='<resource_type_id >',
           help='ID of resource type.')
def do_list_actions(drc, args):
    """- list_actions for  a given resource type
          param:  ID of resource type
         :rtype:  list of defined actions details  per resource type
    """

    kwargs = {}
    actions = drc.dr.list_actions(args.id1, **kwargs)
    fields = ['id', 'name', 'class_name', 'resource_type_id', 'created_at']
    local_print(actions, fields)


@utils.arg('id1', metavar='<Name of policy >', help='Name of policy.')
@utils.arg('id2', metavar='<ID of tenant  >', help='tenant ID ')
def do_create_workload_policy(drc, args={}):
    """- create workload policy
          param:  Name of policy
          param:  tenant ID
         :rtype:  None
    """

    kwargs = {}
    drc.dr.create_workload_policy(args.id1, args.id2, **kwargs)


def do_list_workload_policies(drc, args={}):
    # per tenant : tenant id comes later from context (hopefully)
    """- list all workload  policies of current tenant
          param:  none
         :rtype:  All workload policies information
    """

    kwargs = {}
    policies = drc.dr.list_workload_policies(**kwargs)

    fields = ['id', 'name', 'tenant_id', 'created_at']
    local_print(policies, fields)


@utils.arg('id1', metavar='< workload_policy_id >',
           help=' ID of workload policy')
def do_get_workload_policy(drc, args={}):

    """- get policy per given workload policy id
          param:  ID of workload policy
         :rtype:   specified workload policy info
    """
    kwargs = {}
    policy = drc.dr.get_workload_policy(args.id1, **kwargs)
    fields = ['id', 'name', 'tenant_id', 'created_at']
    local_print(policy, fields)


@utils.arg('id1', metavar='<workload_policy_id >',
           help='ID of workload policy')
def do_delete_workload_policy(drc, args={}):

    """- per given workload policy id
          param:  ID of workload policy
         :rtype: none
    """

    kwargs = {}
    drc.dr.delete_workload_policy(args.id1, **kwargs)


@utils.arg('id1', metavar='<resource_id >',
           help='ID of resource (running number)')
@utils.arg('id2', metavar='<resource_name >', help='resource name ')
@utils.arg('id3', metavar='<resource_type_id >', help='resource type id ')
def do_create_resource(drc, args={}):
    """- create for a given  triple : resource_id,  resource_name, \
            resource_type_id
          param:  ID of resource
          param:  Name of resource
          param:  ID of type of resource
         :rtype: none
    """

    kwargs = {}
    drc.dr.create_resource(args.id1, args.id2, args.id3, **kwargs)


@utils.arg('id1', metavar='<resource_id >', help='ID of resource ')
def do_get_resource(drc, args={}):
    """- get  resource info for a given resource_id:
          param:  ID of resource
         :rtype: resource info: id, type, name
    """

    kwargs = {}
    resource_info = drc.dr.get_resource(args.id1, **kwargs)

    fields = ['id', 'name', 'resource_type_id', 'created_at']
    local_print(resource_info, fields)


@utils.arg('id1', metavar='<resource_id >', help='ID of resource ')
@utils.arg('id2', metavar='<action_id >', help='ID of action')
@utils.arg('id3', metavar='<workload_policy_id >',
           help='ID of workload policy')
def do_create_resource_action(drc, args={}):

    """- create for a given  triple: resource_id,  action_id,\
                  workload_policy_id
          param:  ID of resource
          param:  ID of action
          param:  ID of workload policy
         :rtype: none
    """
    kwargs = {}
    drc.dr.create_resource_action(args.id1, args.id2, args.id3, **kwargs)


@utils.arg('id1', metavar='<resource_action_id >',
           help='ID of resource_action')
def do_delete_resource_action(drc, args={}):

    """-  Delete a given  resource_action
          :param:  ID of resource_action
          :rtype: none
    """

    kwargs = {}
    drc.dr.delete_resource_action(args.id1, **kwargs)


@utils.arg('id1', metavar='<Workload_policy_id >',
           help='ID of workload policy')
def do_get_resource_actions(drc, args={}):

    """-  for a given workload_policy_id - get all defined actions
          :param:  ID of resource
          :rtype: defined actions information per given workload

    """

    kwargs = {}
    resource_actions = drc.dr.get_policy_resource_actions(args.id1, **kwargs)

    fields = ['id', 'resource_id', 'action_id', 'workload_policy_id',
              'created_at']
    local_print(resource_actions, fields)


@utils.arg('id1', metavar='<workload policy id  >',
           help='ID of workload policy')
def do_list_policy_executions(drc, args={}):

    """-  for a given workload policy
          :param:  ID of workload policy
          :rtype: defined policy workload id information of policy executions

    """

    kwargs = {}
    policy = drc.dr.list_policy_executions(args.id1, **kwargs)
    fields = ['id', 'created_at', 'workload_policy_id']
    local_print(policy, fields)


@utils.arg('id1', metavar='<policy_execution_id >',
           help='ID of policy execution')
def do_get_policy_executions(drc, args={}):

    """-   policy executions of  policy_execution_id
          :param:  ID of workload policy
          :rtype: defined policy execution information of policy execution id

    """

    kwargs = {}
    policy = drc.dr.get_policy_executions(args.id1, **kwargs)
    fields = ['id', 'status', 'workload_policy_id']
    local_print(policy, fields)


def do_recovery_list_policies(drc, args={}):

    """-  Recovery_list_policies
          :rtype: recovery container names

    """

    kwargs = {}
    recovery_con = drc.dr.recovery_list_policies(**kwargs)
    fields = ['id', 'name', 'timestamp']
    local_print(recovery_con, fields)


@utils.arg('id1', metavar='<policy_name >',
           help='Policy name')
def do_recovery_list_policy_executions(drc, args={}):

    """-  Recovery_list_policies
          :rtype: recovery container names

    """

    kwargs = {}
    recovery_con = drc.dr.recovery_list_policy_executions(args.id1, **kwargs)
    fields = ['id', 'name', 'timestamp']
    local_print(recovery_con, fields)


def local_print(obj, fields):
    if obj is None or obj == [] or obj == {}:
        print ("_____________")
        print ("no data")
    elif obj is not None:
        print ("__________")

        if type(obj) is list:
            for i in range(0, len(obj)):

                for field in fields:
                    f = unicode(field)
                    print (f, ':', obj[i][f])
                print ('__________')

        elif type(obj) is dict:
            for field in fields:
                f = unicode(field)
                print (f, ':', obj[f])
