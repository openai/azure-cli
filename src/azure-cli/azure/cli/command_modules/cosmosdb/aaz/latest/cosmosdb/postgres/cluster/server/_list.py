# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "cosmosdb postgres cluster server list",
)
class List(AAZCommand):
    """List nodes of a cluster.

    :example: List servers of the cluster
        az cosmosdb postgres cluster server list --cluster-name "test-cluster" -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff"
    """

    _aaz_info = {
        "version": "2022-11-08",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dbforpostgresql/servergroupsv2/{}/servers", "2022-11-08"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="The name of the cluster.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^(?![0-9]+$)(?!-)[a-z0-9-]{3,40}(?<!-)$",
                max_length=40,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ServersListByCluster(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        return result

    class ServersListByCluster(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}/servers",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-08",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.administrator_login = AAZStrType(
                serialized_name="administratorLogin",
                flags={"read_only": True},
            )
            properties.availability_zone = AAZStrType(
                serialized_name="availabilityZone",
            )
            properties.citus_version = AAZStrType(
                serialized_name="citusVersion",
            )
            properties.enable_ha = AAZBoolType(
                serialized_name="enableHa",
            )
            properties.enable_public_ip_access = AAZBoolType(
                serialized_name="enablePublicIpAccess",
                flags={"read_only": True},
            )
            properties.fully_qualified_domain_name = AAZStrType(
                serialized_name="fullyQualifiedDomainName",
                flags={"read_only": True},
            )
            properties.ha_state = AAZStrType(
                serialized_name="haState",
                flags={"read_only": True},
            )
            properties.is_read_only = AAZBoolType(
                serialized_name="isReadOnly",
                flags={"read_only": True},
            )
            properties.postgresql_version = AAZStrType(
                serialized_name="postgresqlVersion",
            )
            properties.role = AAZStrType()
            properties.server_edition = AAZStrType(
                serialized_name="serverEdition",
            )
            properties.state = AAZStrType(
                flags={"read_only": True},
            )
            properties.storage_quota_in_mb = AAZIntType(
                serialized_name="storageQuotaInMb",
            )
            properties.v_cores = AAZIntType(
                serialized_name="vCores",
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
