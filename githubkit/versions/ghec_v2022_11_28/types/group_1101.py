"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Any
from typing_extensions import NotRequired, TypeAlias, TypedDict


class ReposOwnerRepoAttestationsPostBodyType(TypedDict):
    """ReposOwnerRepoAttestationsPostBody"""

    bundle: ReposOwnerRepoAttestationsPostBodyPropBundleType


class ReposOwnerRepoAttestationsPostBodyPropBundleType(TypedDict):
    """ReposOwnerRepoAttestationsPostBodyPropBundle

    The attestation's Sigstore Bundle.
    Refer to the [Sigstore Bundle
    Specification](https://github.com/sigstore/protobuf-
    specs/blob/main/protos/sigstore_bundle.proto) for more information.
    """

    media_type: NotRequired[str]
    verification_material: NotRequired[
        ReposOwnerRepoAttestationsPostBodyPropBundlePropVerificationMaterialType
    ]
    dsse_envelope: NotRequired[
        ReposOwnerRepoAttestationsPostBodyPropBundlePropDsseEnvelopeType
    ]


ReposOwnerRepoAttestationsPostBodyPropBundlePropVerificationMaterialType: TypeAlias = (
    dict[str, Any]
)
"""ReposOwnerRepoAttestationsPostBodyPropBundlePropVerificationMaterial
"""


ReposOwnerRepoAttestationsPostBodyPropBundlePropDsseEnvelopeType: TypeAlias = dict[
    str, Any
]
"""ReposOwnerRepoAttestationsPostBodyPropBundlePropDsseEnvelope
"""


__all__ = (
    "ReposOwnerRepoAttestationsPostBodyPropBundlePropDsseEnvelopeType",
    "ReposOwnerRepoAttestationsPostBodyPropBundlePropVerificationMaterialType",
    "ReposOwnerRepoAttestationsPostBodyPropBundleType",
    "ReposOwnerRepoAttestationsPostBodyType",
)
