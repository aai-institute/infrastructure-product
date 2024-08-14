import time
from pathlib import Path

from jobs import ImageOptions, JobOptions, ResourceOptions, SchedulingOptions, job


@job(
    options=JobOptions(
        labels={"type": "hello-world@dev", "x-jobby.io/key": "value"},
        resources=ResourceOptions(memory="1Gi", cpu="1"),
        scheduling=SchedulingOptions(
            priority_class="background", queue_name="user-queue"
        ),
    ),
    image=ImageOptions(
        spec=Path("example-docker.yaml"),
        name="localhost:5000/hello-world-dev",
        tag="latest",
    ),
)
def hello_world():
    for idx in range(10):
        print(f"Hello, World!, {idx=}")
        time.sleep(2)
