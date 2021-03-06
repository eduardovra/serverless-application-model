from unittest import TestCase
import pytest

from samtranslator.model import InvalidResourceException
from samtranslator.model.apigatewayv2 import ApiGatewayV2Authorizer, ApiGatewayV2HttpApi, ApiGatewayV2Stage


class TestApiGatewayV2Authorizer(TestCase):

    def test_create_oauth2_auth(self):
        auth = ApiGatewayV2Authorizer(api_logical_id="logicalId", name="authName",
                                      jwt_configuration={"config": "value"}, id_source="https://example.com")
        self.assertEquals(auth.auth_type, "oauth2")

    def test_create_oidc_auth(self):
        auth = ApiGatewayV2Authorizer(api_logical_id="logicalId", name="authName", open_id_connect_url="https://example.com",
                                      jwt_configuration={"config": "value"}, id_source="https://example.com")
        self.assertEquals(auth.auth_type, "openIdConnect")

    def test_create_authorizer_no_id_source(self):
        with pytest.raises(InvalidResourceException):
            auth = ApiGatewayV2Authorizer(api_logical_id="logicalId", name="authName", jwt_configuration={"config": "value"})

    def test_create_authorizer_no_jwt_config(self):
        with pytest.raises(InvalidResourceException):
            auth = ApiGatewayV2Authorizer(api_logical_id="logicalId", name="authName", id_source="https://example.com")
