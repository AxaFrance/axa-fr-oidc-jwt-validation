import unittest

from src.oidc_jwt_validation import authentication

VALID_SCOPE = "test_scope"
ARRAY_OF_VALID_SCOPES = "scope1 test_scope scope2"
INVALID_SCOPE = "test_scope_invalid"
ARRAY_OF_INVALID_SCOPES = "scope1 test_scope_invalid scope3"


class AuthenticationTestCase(unittest.TestCase):
    def test_scope_validation_with_valid_scope_returns_true(self):
        payload = {
            "scope": VALID_SCOPE
        }
        self.assertEqual(authentication.is_scope_valid(payload, VALID_SCOPE), True)

    def test_scope_validation_with_valid_scope_in_array_of_scopes_returns_true(self):
        payload = {
            "scope": ARRAY_OF_VALID_SCOPES
        }
        self.assertEqual(authentication.is_scope_valid(payload, VALID_SCOPE), True)

    def test_scope_validation_with_invalid_scope_returns_false(self):
        payload = {
            "scope": INVALID_SCOPE
        }
        self.assertEqual(authentication.is_scope_valid(payload, VALID_SCOPE), False)

    def test_scope_validation_with_invalid_scope_in_array_of_invalid_scopes_returns_false(self):
        payload = {
            "scope": ARRAY_OF_INVALID_SCOPES
        }
        self.assertEqual(authentication.is_scope_valid(payload, VALID_SCOPE), False)

    def test_scope_validation_with_null_scope_in_payload_returns_false(self):
        payload = {
            "scope": None
        }
        self.assertEqual(authentication.is_scope_valid(payload, VALID_SCOPE), False)

    def test_scope_validation_with_no_scope_in_payload_returns_false(self):
        payload = {

        }
        self.assertEqual(authentication.is_scope_valid(payload, VALID_SCOPE), False)
