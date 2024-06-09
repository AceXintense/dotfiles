from _typeshed import Incomplete

from influxdb_client.domain.authorization_update_request import AuthorizationUpdateRequest

class Authorization(AuthorizationUpdateRequest):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        org_id: Incomplete | None = None,
        permissions: Incomplete | None = None,
        id: Incomplete | None = None,
        token: Incomplete | None = None,
        user_id: Incomplete | None = None,
        user: Incomplete | None = None,
        org: Incomplete | None = None,
        links: Incomplete | None = None,
        status: str = "active",
        description: Incomplete | None = None,
    ) -> None: ...
    @property
    def created_at(self): ...
    @created_at.setter
    def created_at(self, created_at) -> None: ...
    @property
    def updated_at(self): ...
    @updated_at.setter
    def updated_at(self, updated_at) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def permissions(self): ...
    @permissions.setter
    def permissions(self, permissions) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def token(self): ...
    @token.setter
    def token(self, token) -> None: ...
    @property
    def user_id(self): ...
    @user_id.setter
    def user_id(self, user_id) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user) -> None: ...
    @property
    def org(self): ...
    @org.setter
    def org(self, org) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...