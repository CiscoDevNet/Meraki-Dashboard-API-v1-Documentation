# Deprecation

## Overview

As necessary, Meraki may deprecate API versions or operations over time. After an announced deprecation period, the versions or operations marked as deprecated will be sunset.

This means that Meraki may offer newer, more performant alternatives over time to satisfy developer use cases currently met in whole or in part by existing operations and/or versions. When this happens, Meraki will:

1. Mark the deprecated operation or version as deprecated in the OAS.
2. Provide documented alternatives to the operation or version.

We encourage developers to take advantage of the improvements and migrate their applications to the latest offerings. In any case, it is the developer's responsibility to migrate their applications to non-deprecated offerings prior to the sunset date for that offering.

## Definitions

### Version vs. revision

An API version, also known as a _major_ version, identifies a grouped set of API resources and operations. At Meraki, we use simple integers for versions, e.g. "v1". Today, these are released infrequently, and Meraki only has "v1".

An API revision, also known as a _minor_ version, identifies non-breaking improvements to an API, such as the addition of new attributes or capabilities to extend existing operations within a major version. In most if not all cases, changes between revisions within a single version are additive and otherwise transparent to clients built on older revisions of that version. Today, Meraki names a new revision every month, summarizing all the changes that have been released since the last named revision. A Meraki API revision name takes the format of "1.50.0", where "1" is the version, "50" is the ID of the "minor version", and "0" is the patch version. Note that the terms 'major' and 'minor' versions are commonly used in the industry in the context of semantic versioning; for our purposes, this guide will refer to major versions as versions and minor versions as revisions.

### Deprecation vs. sunsetting

#### Deprecation

Deprecation is a standard step in an API’s lifecycle. It can apply to an entire API version or a part of it, like a single operation. Deprecation signals a better alternative is available, such as a newer version or operation. Deprecation is _not_ a breaking change.

When an API version is deprecated, a sunset announcement with timelines will follow when appropriate. Migration efforts can vary, so start planning a switch to a replacement as soon as possible. Using a deprecated API version is against best practice; it’s advisable to review your needs and consider available replacements.

> NB: Meraki dashboard API only has version 1, which is not deprecated.

When an API operation is deprecated, indicating superior operations are available, it will be sunset with its API version. Migrating to new operations is advantageous, especially for large environments or specific use cases. Using a deprecated API operation is against best practice and discouraged. It’s advisable to review your needs and consider available replacements, even without a sunset date.

#### Sunsetting

Sunsetting is the act of removing support for a single API operation or a whole version, after the deprecation period has elapsed. An operation or version is sunset after the deprecation period has elapsed. Sunsetting _is_ a breaking change.

## Deprecated operations

Beyond the OAS, deprecated operations are documented [here](deprecated-operations.md).
