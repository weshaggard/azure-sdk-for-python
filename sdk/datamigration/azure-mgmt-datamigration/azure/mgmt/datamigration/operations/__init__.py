# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._database_migrations_sql_db_operations import DatabaseMigrationsSqlDbOperations
from ._database_migrations_sql_mi_operations import DatabaseMigrationsSqlMiOperations
from ._database_migrations_sql_vm_operations import DatabaseMigrationsSqlVmOperations
from ._operations import Operations
from ._sql_migration_services_operations import SqlMigrationServicesOperations
from ._resource_skus_operations import ResourceSkusOperations
from ._services_operations import ServicesOperations
from ._tasks_operations import TasksOperations
from ._service_tasks_operations import ServiceTasksOperations
from ._projects_operations import ProjectsOperations
from ._usages_operations import UsagesOperations
from ._files_operations import FilesOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DatabaseMigrationsSqlDbOperations",
    "DatabaseMigrationsSqlMiOperations",
    "DatabaseMigrationsSqlVmOperations",
    "Operations",
    "SqlMigrationServicesOperations",
    "ResourceSkusOperations",
    "ServicesOperations",
    "TasksOperations",
    "ServiceTasksOperations",
    "ProjectsOperations",
    "UsagesOperations",
    "FilesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
