Identifiers in the API are opaque strings. A `<network_id>`, for example, might be the string “126043”, whereas an `<order_id>` might contain characters, such as “4S1234567”. Client applications must not try to parse them as numbers. Even identifiers that look like numbers might be too long to encode without loss of precision in Javascript, where the only numeric type is IEEE 754 floating point.

Verbs in the API follow the usual REST conventions: 

`GET` returns the value of a resource or a list of resources, depending on whether an identifier is specified. For example, a `GET` of `/v0/organizations` returns a list of organizations, whereas a `GET` of `/v0/organizations/<org_id>` returns a particular organization. 

`POST` adds a new resource, as in a `POST` to `/v0/organizations/<org_id>/admins`, or performs some other non-idempotent change.

 `PUT` updates a resource. `PUTs` are idempotent; they update a resource, creating it first if it does not already exist. A `PUT` should specify all the fields of a resource; the API will revert omitted fields to their default value. 

`DELETE` removes a resource. Call volume is limited to 5 calls per second (per organization).