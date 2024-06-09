from collections.abc import Sequence
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from typing import Any

from django.core.management.color import Style
from django.db import DefaultConnectionProxy
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.utils import CursorWrapper
from django.db.models.base import Model
from django.db.models.expressions import Case, Expression
from django.db.models.fields import Field
from django.db.models.sql.compiler import SQLCompiler

_Connection = DefaultConnectionProxy | BaseDatabaseWrapper

class BaseDatabaseOperations:
    compiler_module: str = ...
    integer_field_ranges: Any = ...
    set_operators: Any = ...
    cast_data_types: Any = ...
    cast_char_field_without_max_length: Any = ...
    PRECEDING: str = ...
    FOLLOWING: str = ...
    UNBOUNDED_PRECEDING: Any = ...
    UNBOUNDED_FOLLOWING: Any = ...
    CURRENT_ROW: str = ...
    explain_prefix: Any = ...
    connection: _Connection = ...
    def __init__(self, connection: _Connection | None) -> None: ...
    def autoinc_sql(self, table: str, column: str) -> None: ...
    def bulk_batch_size(self, fields: Any, objs: Any) -> Any: ...
    def cache_key_culling_sql(self) -> str: ...
    def unification_cast_sql(self, output_field: Field[Any, Any]) -> str: ...
    def date_extract_sql(self, lookup_type: None, field_name: None) -> Any: ...
    def date_interval_sql(self, timedelta: None) -> Any: ...
    def date_trunc_sql(self, lookup_type: None, field_name: None) -> Any: ...
    def datetime_cast_date_sql(self, field_name: None, tzname: None) -> Any: ...
    def datetime_cast_time_sql(self, field_name: None, tzname: None) -> Any: ...
    def datetime_extract_sql(
        self, lookup_type: None, field_name: None, tzname: None
    ) -> Any: ...
    def datetime_trunc_sql(
        self, lookup_type: None, field_name: None, tzname: None
    ) -> Any: ...
    def time_trunc_sql(self, lookup_type: None, field_name: None) -> Any: ...
    def time_extract_sql(self, lookup_type: None, field_name: None) -> Any: ...
    def deferrable_sql(self) -> str: ...
    def distinct_sql(
        self, fields: list[str], params: list[Any] | None
    ) -> tuple[list[str], list[Any]]: ...
    def fetch_returned_insert_id(self, cursor: Any) -> Any: ...
    def field_cast_sql(self, db_type: str | None, internal_type: str) -> str: ...
    def force_no_ordering(self) -> list[Any]: ...
    def for_update_sql(
        self, nowait: bool = ..., skip_locked: bool = ..., of: Any = ...
    ) -> Any: ...
    def limit_offset_sql(self, low_mark: int, high_mark: int | None) -> str: ...
    def last_executed_query(self, cursor: Any, sql: Any, params: Any) -> Any: ...
    def last_insert_id(
        self, cursor: CursorWrapper, table_name: str, pk_name: str
    ) -> int: ...
    def lookup_cast(self, lookup_type: str, internal_type: str = ...) -> str: ...
    def max_in_list_size(self) -> None: ...
    def max_name_length(self) -> None: ...
    def no_limit_value(self) -> Any: ...
    def pk_default_value(self) -> str: ...
    def prepare_sql_script(self, sql: Any) -> Any: ...
    def process_clob(self, value: str) -> str: ...
    def return_insert_id(self) -> None: ...
    def compiler(self, compiler_name: str) -> type[SQLCompiler]: ...
    def quote_name(self, name: str) -> Any: ...
    def random_function_sql(self) -> Any: ...
    def regex_lookup(self, lookup_type: str) -> Any: ...
    def savepoint_create_sql(self, sid: str) -> str: ...
    def savepoint_commit_sql(self, sid: str) -> str: ...
    def savepoint_rollback_sql(self, sid: str) -> str: ...
    def set_time_zone_sql(self) -> str: ...
    def sql_flush(
        self, style: None, tables: None, sequences: None, allow_cascade: bool = ...
    ) -> Any: ...
    def execute_sql_flush(self, using: str, sql_list: list[str]) -> None: ...
    def sequence_reset_by_name_sql(
        self, style: None, sequences: list[Any]
    ) -> list[Any]: ...
    def sequence_reset_sql(
        self, style: Style, model_list: Sequence[type[Model]]
    ) -> list[Any]: ...
    def start_transaction_sql(self) -> str: ...
    def end_transaction_sql(self, success: bool = ...) -> str: ...
    def tablespace_sql(self, tablespace: str | None, inline: bool = ...) -> str: ...
    def prep_for_like_query(self, x: str) -> str: ...
    prep_for_iexact_query: Any = ...
    def validate_autopk_value(self, value: int) -> int: ...
    def adapt_unknown_value(self, value: Any) -> Any: ...
    def adapt_datefield_value(self, value: date | None) -> str | None: ...
    def adapt_datetimefield_value(self, value: datetime | None) -> str | None: ...
    def adapt_timefield_value(self, value: datetime | time | None) -> str | None: ...
    def adapt_decimalfield_value(
        self,
        value: Decimal | None,
        max_digits: int | None = ...,
        decimal_places: int | None = ...,
    ) -> str | None: ...
    def adapt_ipaddressfield_value(self, value: str | None) -> str | None: ...
    def year_lookup_bounds_for_date_field(self, value: int) -> list[str]: ...
    def year_lookup_bounds_for_datetime_field(self, value: int) -> list[str]: ...
    def get_db_converters(self, expression: Expression) -> list[Any]: ...
    def convert_durationfield_value(
        self, value: float | None, expression: Expression, connection: _Connection
    ) -> timedelta | None: ...
    def check_expression_support(self, expression: Any) -> None: ...
    def combine_expression(self, connector: str, sub_expressions: list[str]) -> str: ...
    def combine_duration_expression(
        self, connector: Any, sub_expressions: Any
    ) -> Any: ...
    def binary_placeholder_sql(self, value: Case | None) -> str: ...
    def modify_insert_params(self, placeholder: str, params: Any) -> Any: ...
    def integer_field_range(self, internal_type: Any) -> Any: ...
    def subtract_temporals(self, internal_type: Any, lhs: Any, rhs: Any) -> Any: ...
    def window_frame_start(self, start: Any) -> Any: ...
    def window_frame_end(self, end: Any) -> Any: ...
    def window_frame_rows_start_end(
        self, start: int | None = ..., end: int | None = ...
    ) -> Any: ...
    def window_frame_range_start_end(
        self, start: int | None = ..., end: int | None = ...
    ) -> Any: ...
    def explain_query_prefix(self, format: str | None = ..., **options: Any) -> str: ...
