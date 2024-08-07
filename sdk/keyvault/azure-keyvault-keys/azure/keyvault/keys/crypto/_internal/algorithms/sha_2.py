# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import Union, Type

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from ..algorithm import HashAlgorithm
from ..transform import DigestTransform


class _Sha2DigestTransform(DigestTransform):
    def __init__(self, algorithm):
        super(_Sha2DigestTransform, self).__init__()
        self._digest = hashes.Hash(algorithm=algorithm, backend=default_backend())

    def update(self, data):
        return self._digest.update(data)

    def finalize(self, data):
        return self._digest.finalize()


class _Sha2HashAlgorithm(HashAlgorithm):

    _algorithm_cls: Union[Type[hashes.SHA256], Type[hashes.SHA384], Type[hashes.SHA512], None] = None

    def create_digest(self):
        return _Sha2DigestTransform(self._algorithm_cls())  # pylint:disable=not-callable


class Sha256(_Sha2HashAlgorithm):
    _algorithm_cls = hashes.SHA256
    _name = "SHA256"


class Sha384(_Sha2HashAlgorithm):
    _algorithm_cls = hashes.SHA384
    _name = "SHA384"


class Sha512(_Sha2HashAlgorithm):
    _algorithm_cls = hashes.SHA512
    _name = "SHA512"


Sha256.register()

Sha384.register()

Sha512.register()
