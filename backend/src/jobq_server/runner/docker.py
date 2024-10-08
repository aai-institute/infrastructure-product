import logging
import textwrap

import docker
from jobq import Image, Job
from jobq.job import DockerResourceOptions

from jobq_server.models import ExecutionMode, SubmissionContext
from jobq_server.runner.base import Runner, _make_executor_command
from jobq_server.utils.helpers import remove_none_values


class DockerRunner(Runner):
    def __init__(self, **kwargs):
        super().__init__()
        self._client = docker.from_env()

    def run(self, job: Job, image: Image, context: SubmissionContext) -> None:
        command = _make_executor_command(job)

        resource_kwargs: DockerResourceOptions = {
            "mem_limit": None,
            "nano_cpus": None,
            "device_requests": None,
        }
        if job.options and (res := job.options.resources):
            resource_kwargs = res.to_docker()

        container: docker.api.client.ContainerApiMixin = self._client.containers.run(
            image=image.tag,
            command=command,
            detach=True,
            **remove_none_values(resource_kwargs),
        )

        exit_code = container.wait()

        logging.debug(
            f"Container exited with code {exit_code.get('StatusCode')}, output:\n%s",
            textwrap.indent(container.logs().decode(encoding="utf-8"), " " * 4),
        )


Runner.register_implementation(DockerRunner, ExecutionMode.DOCKER)
