import argparse
from pprint import pp
from typing import Any

import openapi_client

from .util import _make_api_client, handle_api_exception


def logs(args: argparse.Namespace) -> None:
    with _make_api_client() as api:
        client = openapi_client.JobManagementApi(api)
        try:
            params = {
                k: v
                for k, v in {
                    "uid": args.uid,
                    "namespace": args.namespace,
                    "stream": args.stream,
                    "tail": args.tail,
                }.items()
                if v is not None
            }
            resp = client.logs_jobs_uid_logs_get(**params)
            if args.output:
                with open(args.output, "w") as f:
                    f.write(str(resp))
                print(f"Logs written to {args.output}")
            else:
                pp(resp)
        except openapi_client.ApiException as e:
            handle_api_exception(e, "fetching logs")


def add_parser(subparsers: Any, parent: argparse.ArgumentParser) -> None:
    # jobby logs, command to fetch logs for workload
    parser = subparsers.add_parser("logs", description="Get logs for specified job.")
    parser.add_argument(
        "--namespace",
        help="Kubernetes namespace the job was created in, "
        "defaults to currently active namespace.",
    )
    parser.add_argument("uid", metavar="<ID>")
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Whether to stream logs",
    )
    parser.add_argument(
        "--tail",
        type=int,
        help="Fetch N most recent log entries",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        help="Dump logs to file instead of stdout",
    )
    parser.set_defaults(func=logs)
