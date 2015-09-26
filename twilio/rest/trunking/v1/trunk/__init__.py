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
from twilio.rest.trunking.v1.trunk.credential_list import CredentialListList
from twilio.rest.trunking.v1.trunk.ip_access_control_list import IpAccessControlListList
from twilio.rest.trunking.v1.trunk.origination_url import OriginationUrlList
from twilio.rest.trunking.v1.trunk.phone_number import PhoneNumberList


class TrunkList(ListResource):

    def __init__(self, version):
        """
        Initialize the TrunkList
        
        :param Version version: Version that contains the resource
        
        :returns: TrunkList
        :rtype: TrunkList
        """
        super(TrunkList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Trunks'.format(**self._kwargs)

    def create(self, friendly_name=values.unset, domain_name=values.unset,
               disaster_recovery_url=values.unset,
               disaster_recovery_method=values.unset, recording=values.unset,
               secure=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'DomainName': domain_name,
            'DisasterRecoveryUrl': disaster_recovery_url,
            'DisasterRecoveryMethod': disaster_recovery_method,
            'Recording': recording,
            'Secure': secure,
        })
        
        return self._version.create(
            TrunkInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            TrunkInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            TrunkInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a TrunkContext
        
        :param sid: Contextual sid
        
        :returns: TrunkContext
        :rtype: TrunkContext
        """
        return TrunkContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.TrunkList>'


class TrunkContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the TrunkContext
        
        :param Version version
        :param sid: Contextual sid
        
        :returns: TrunkContext
        :rtype: TrunkContext
        """
        super(TrunkContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Trunks/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._origination_urls = None
        self._credentials_lists = None
        self._ip_access_control_lists = None
        self._phone_numbers = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            TrunkInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    def update(self, friendly_name=values.unset, domain_name=values.unset,
               disaster_recovery_url=values.unset,
               disaster_recovery_method=values.unset, recording=values.unset,
               secure=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'DomainName': domain_name,
            'DisasterRecoveryUrl': disaster_recovery_url,
            'DisasterRecoveryMethod': disaster_recovery_method,
            'Recording': recording,
            'Secure': secure,
        })
        
        return self._version.update(
            TrunkInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def origination_urls(self):
        """
        Access the origination_urls
        
        :returns: OriginationUrlList
        :rtype: OriginationUrlList
        """
        if self._origination_urls is None:
            self._origination_urls = OriginationUrlList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._origination_urls

    @property
    def credentials_lists(self):
        """
        Access the credentials_lists
        
        :returns: CredentialListList
        :rtype: CredentialListList
        """
        if self._credentials_lists is None:
            self._credentials_lists = CredentialListList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._credentials_lists

    @property
    def ip_access_control_lists(self):
        """
        Access the ip_access_control_lists
        
        :returns: IpAccessControlListList
        :rtype: IpAccessControlListList
        """
        if self._ip_access_control_lists is None:
            self._ip_access_control_lists = IpAccessControlListList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._ip_access_control_lists

    @property
    def phone_numbers(self):
        """
        Access the phone_numbers
        
        :returns: PhoneNumberList
        :rtype: PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Trunking.V1.TrunkContext {}>'.format(context)


class TrunkInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the TrunkInstance
        
        :returns: TrunkInstance
        :rtype: TrunkInstance
        """
        super(TrunkInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'domain_name': payload['domain_name'],
            'disaster_recovery_method': payload['disaster_recovery_method'],
            'disaster_recovery_url': payload['disaster_recovery_url'],
            'friendly_name': payload['friendly_name'],
            'secure': payload['secure'],
            'recording': payload['recording'],
            'auth_type': payload['auth_type'],
            'auth_type_set': payload['auth_type_set'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'sid': payload['sid'],
            'url': payload['url'],
            'links': payload['links'],
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
        
        :returns: TrunkContext for this TrunkInstance
        :rtype: TrunkContext
        """
        if self._instance_context is None:
            self._instance_context = TrunkContext(
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
    def domain_name(self):
        """
        :returns: The domain_name
        :rtype: str
        """
        return self._properties['domain_name']

    @property
    def disaster_recovery_method(self):
        """
        :returns: The disaster_recovery_method
        :rtype: str
        """
        return self._properties['disaster_recovery_method']

    @property
    def disaster_recovery_url(self):
        """
        :returns: The disaster_recovery_url
        :rtype: str
        """
        return self._properties['disaster_recovery_url']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def secure(self):
        """
        :returns: The secure
        :rtype: bool
        """
        return self._properties['secure']

    @property
    def recording(self):
        """
        :returns: The recording
        :rtype: str
        """
        return self._properties['recording']

    @property
    def auth_type(self):
        """
        :returns: The auth_type
        :rtype: str
        """
        return self._properties['auth_type']

    @property
    def auth_type_set(self):
        """
        :returns: The auth_type_set
        :rtype: str
        """
        return self._properties['auth_type_set']

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
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: str
        """
        return self._properties['links']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()

    def update(self, friendly_name=values.unset, domain_name=values.unset,
               disaster_recovery_url=values.unset,
               disaster_recovery_method=values.unset, recording=values.unset,
               secure=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            domain_name=domain_name,
            disaster_recovery_url=disaster_recovery_url,
            disaster_recovery_method=disaster_recovery_method,
            recording=recording,
            secure=secure,
        )

    @property
    def origination_urls(self):
        """
        Access the origination_urls
        
        :returns: origination_urls
        :rtype: origination_urls
        """
        return self._context.origination_urls

    @property
    def credentials_lists(self):
        """
        Access the credentials_lists
        
        :returns: credentials_lists
        :rtype: credentials_lists
        """
        return self._context.credentials_lists

    @property
    def ip_access_control_lists(self):
        """
        Access the ip_access_control_lists
        
        :returns: ip_access_control_lists
        :rtype: ip_access_control_lists
        """
        return self._context.ip_access_control_lists

    @property
    def phone_numbers(self):
        """
        Access the phone_numbers
        
        :returns: phone_numbers
        :rtype: phone_numbers
        """
        return self._context.phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Trunking.V1.TrunkInstance {}>'.format(context)
