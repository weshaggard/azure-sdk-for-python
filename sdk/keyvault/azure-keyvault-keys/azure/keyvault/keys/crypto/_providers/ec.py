# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import TYPE_CHECKING

from .local_provider import LocalCryptographyProvider
from .._internal import EllipticCurveKey
from ... import KeyOperation, KeyType

if TYPE_CHECKING:
    from .local_provider import Algorithm
    from .._internal import Key
    from ... import JsonWebKey

_PRIVATE_KEY_OPERATIONS = frozenset((KeyOperation.decrypt, KeyOperation.sign, KeyOperation.unwrap_key))


class EllipticCurveCryptographyProvider(LocalCryptographyProvider):
    def _get_internal_key(self, key: "JsonWebKey") -> "Key":
        if key.kty not in (KeyType.ec, KeyType.ec_hsm):  # type: ignore[attr-defined]
            raise ValueError('"key" must be an EC or EC-HSM key')
        return EllipticCurveKey.from_jwk(key)

    def supports(self, operation: KeyOperation, algorithm: "Algorithm") -> bool:
        if operation in _PRIVATE_KEY_OPERATIONS and not self._internal_key.is_private_key():
            return False
        if operation in (KeyOperation.decrypt, KeyOperation.encrypt):
            return algorithm in self._internal_key.supported_encryption_algorithms
        if operation in (KeyOperation.unwrap_key, KeyOperation.wrap_key):
            return algorithm in self._internal_key.supported_key_wrap_algorithms
        if operation in (KeyOperation.sign, KeyOperation.verify):
            return algorithm in self._internal_key.supported_signature_algorithms
        return False
