
# Fullctl / Prefixctl

Prefix meta s a plugin for prefixctl and requires a working fullctl environment that is running prefixctl

Setup documentation can be found [here](https://github.com/fullctl/prefixctl/blob/main/docs/quickstart.md).

## IP2Location options

To be set in your PrefixCtl `Ctl/{env}/.env` file.

- `IP2LOCATION_API_KEY`
- `IP2LOCATION_PACKAGE` (default=WS25) - which package to query
- `IP2LOCATION_CACHE_EXPIRY` (default=30 days, value is in seconds) - how long is location cache valid

# AAACTL Permissions (for non-standalone instances of PrefixCtl)

This is only relevant if you are using AAACTL to manage users and permissions. If you are running a standalone instance of PrefixCtl, you can ignore this section.

To give users access to this plugin they need to be granted permissions to the following namespaces

- `meta.prefix.location.{org_id}`
- `prefix_set.{org_id}`

`{org_id}` should be the id of their organization