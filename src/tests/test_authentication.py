import unittest

from src.oidc_jwt_validation import authentication

VALID_SCOPE = "test_scope"
INVALID_SCOPE = "test_invalid_scope"


class AuthenticationTestCase(unittest.TestCase):
    def test_scope_validation_with_valid_scope_returns_true(self):
        payload = {
            "scope": VALID_SCOPE
        }
        self.assertEqual(authentication.is_scope_valid(payload, VALID_SCOPE), True)

    def test_scope_validation_with_invalid_scope_returns_false(self):
        payload = {
            "scope": INVALID_SCOPE
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
