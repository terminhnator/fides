"""
Contains all of the options/arguments used by the CLI commands.
"""

from typing import Callable

import click

from fideslang import model_list


def resource_type_argument(command: Callable) -> Callable:
    "Add the resource_type option."
    command = click.argument(
        "resource_type",
        type=click.Choice(model_list, case_sensitive=False),
    )(command)
    return command


def fides_key_argument(command: Callable) -> Callable:
    "Add the fides_key argument."
    command = click.argument(
        "fides_key",
        type=str,
    )(command)
    return command


def fides_key_option(command: Callable) -> Callable:
    "Add the fides_key option."
    command = click.option(
        "-k",
        "--fides-key",
        default="",
        help="The fides_key of the single policy that you wish to evaluate.",
    )(command)
    return command


def manifests_dir_argument(command: Callable) -> Callable:
    "Add the manifests_dir argument."
    command = click.argument(
        "manifests_dir",
        default=".fides/",
        type=click.Path(exists=True),
    )(command)
    return command


def dry_flag(command: Callable) -> Callable:
    "Add a flag that prevents side-effects."
    command = click.option(
        "--dry", is_flag=True, help="Does not send changes to the server."
    )(command)
    return command


def yes_flag(command: Callable) -> Callable:
    "Add a flag that assumes yes."
    command = click.option(
        "--yes",
        "-y",
        is_flag=True,
        help="Automatically responds 'yes' to any prompts.",
    )(command)
    return command


def verbose_flag(command: Callable) -> Callable:
    "Turns on verbose output."
    command = click.option(
        "--verbose",
        "-v",
        is_flag=True,
        help="Enable verbose output.",
    )(command)
    return command


def include_null_flag(command: Callable) -> Callable:
    "Include null attributes in resource output."
    command = click.option(
        "--include-null",
        is_flag=True,
        help="Includes attributes that would otherwise be null.",
    )(command)
    return command
