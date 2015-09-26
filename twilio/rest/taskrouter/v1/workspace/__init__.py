# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.taskrouter.v1.workspace.activity import ActivityList
from twilio.rest.taskrouter.v1.workspace.event import EventList
from twilio.rest.taskrouter.v1.workspace.statistics import StatisticsContext
from twilio.rest.taskrouter.v1.workspace.task import TaskList
from twilio.rest.taskrouter.v1.workspace.task_queue import TaskQueueList
from twilio.rest.taskrouter.v1.workspace.worker import WorkerList
from twilio.rest.taskrouter.v1.workspace.workflow import WorkflowList


class WorkspaceList(ListResource):

    def __init__(self, version):
        """
        Initialize the WorkspaceList
        
        :param Version version: Version that contains the resource
        
        :returns: WorkspaceList
        :rtype: WorkspaceList
        """
        super(WorkspaceList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Workspaces'.format(**self._kwargs)

    def read(self, friendly_name=values.unset, limit=None, page_size=None,
             **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'FriendlyName': friendly_name,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, event_callback_url=values.unset,
               template=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'EventCallbackUrl': event_callback_url,
            'Template': template,
        })
        
        return self._version.create(
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a WorkspaceContext
        
        :param sid: Contextual sid
        
        :returns: WorkspaceContext
        :rtype: WorkspaceContext
        """
        return WorkspaceContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceList>'


class WorkspaceContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the WorkspaceContext
        
        :param Version version
        :param sid: Contextual sid
        
        :returns: WorkspaceContext
        :rtype: WorkspaceContext
        """
        super(WorkspaceContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Workspaces/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._activities = None
        self._events = None
        self._tasks = None
        self._task_queues = None
        self._workers = None
        self._workflows = None
        self._statistics = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            WorkspaceInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, friendly_name=values.unset,
               timeout_activity_sid=values.unset):
        data = values.of({
            'DefaultActivitySid': default_activity_sid,
            'EventCallbackUrl': event_callback_url,
            'FriendlyName': friendly_name,
            'TimeoutActivitySid': timeout_activity_sid,
        })
        
        return self._version.update(
            WorkspaceInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    @property
    def activities(self):
        """
        Access the activities
        
        :returns: ActivityList
        :rtype: ActivityList
        """
        if self._activities is None:
            self._activities = ActivityList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._activities

    @property
    def events(self):
        """
        Access the events
        
        :returns: EventList
        :rtype: EventList
        """
        if self._events is None:
            self._events = EventList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._events

    @property
    def tasks(self):
        """
        Access the tasks
        
        :returns: TaskList
        :rtype: TaskList
        """
        if self._tasks is None:
            self._tasks = TaskList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._tasks

    @property
    def task_queues(self):
        """
        Access the task_queues
        
        :returns: TaskQueueList
        :rtype: TaskQueueList
        """
        if self._task_queues is None:
            self._task_queues = TaskQueueList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._task_queues

    @property
    def workers(self):
        """
        Access the workers
        
        :returns: WorkerList
        :rtype: WorkerList
        """
        if self._workers is None:
            self._workers = WorkerList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._workers

    @property
    def workflows(self):
        """
        Access the workflows
        
        :returns: WorkflowList
        :rtype: WorkflowList
        """
        if self._workflows is None:
            self._workflows = WorkflowList(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._workflows

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: StatisticsContext
        :rtype: StatisticsContext
        """
        if self._statistics is None:
            self._statistics = StatisticsContext(
                self._version,
                workspace_sid=self._kwargs['sid'],
            )
        return self._statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.WorkspaceContext {}>'.format(context)


class WorkspaceInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the WorkspaceInstance
        
        :returns: WorkspaceInstance
        :rtype: WorkspaceInstance
        """
        super(WorkspaceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'default_activity_name': payload['default_activity_name'],
            'default_activity_sid': payload['default_activity_sid'],
            'event_callback_url': payload['event_callback_url'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'timeout_activity_name': payload['timeout_activity_name'],
            'timeout_activity_sid': payload['timeout_activity_sid'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: WorkspaceContext for this WorkspaceInstance
        :rtype: WorkspaceContext
        """
        if self._instance_context is None:
            self._instance_context = WorkspaceContext(
                self._version,
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def default_activity_name(self):
        """
        :returns: The default_activity_name
        :rtype: str
        """
        return self._properties['default_activity_name']

    @property
    def default_activity_sid(self):
        """
        :returns: The default_activity_sid
        :rtype: str
        """
        return self._properties['default_activity_sid']

    @property
    def event_callback_url(self):
        """
        :returns: The event_callback_url
        :rtype: str
        """
        return self._properties['event_callback_url']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def timeout_activity_name(self):
        """
        :returns: The timeout_activity_name
        :rtype: str
        """
        return self._properties['timeout_activity_name']

    @property
    def timeout_activity_sid(self):
        """
        :returns: The timeout_activity_sid
        :rtype: str
        """
        return self._properties['timeout_activity_sid']

    def fetch(self):
        self._context.fetch()

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, friendly_name=values.unset,
               timeout_activity_sid=values.unset):
        self._context.update(
            default_activity_sid=default_activity_sid,
            event_callback_url=event_callback_url,
            friendly_name=friendly_name,
            timeout_activity_sid=timeout_activity_sid,
        )

    def delete(self):
        self._context.delete()

    @property
    def activities(self):
        """
        Access the activities
        
        :returns: activities
        :rtype: activities
        """
        return self._context.activities

    @property
    def events(self):
        """
        Access the events
        
        :returns: events
        :rtype: events
        """
        return self._context.events

    @property
    def tasks(self):
        """
        Access the tasks
        
        :returns: tasks
        :rtype: tasks
        """
        return self._context.tasks

    @property
    def task_queues(self):
        """
        Access the task_queues
        
        :returns: task_queues
        :rtype: task_queues
        """
        return self._context.task_queues

    @property
    def workers(self):
        """
        Access the workers
        
        :returns: workers
        :rtype: workers
        """
        return self._context.workers

    @property
    def workflows(self):
        """
        Access the workflows
        
        :returns: workflows
        :rtype: workflows
        """
        return self._context.workflows

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: statistics
        :rtype: statistics
        """
        return self._context.statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.WorkspaceInstance {}>'.format(context)
