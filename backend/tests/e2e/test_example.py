import time
from pprint import pp

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from jobs import JobOptions, SchedulingOptions
from testcontainers.core.image import DockerImage

from jobs_server.models import CreateJobModel, JobStatus, WorkloadIdentifier


def test_create_job(client: TestClient, job_image: DockerImage):
    body = CreateJobModel(
        image_ref=str(job_image),
        name="test-job",
        file="test_example.py",
        mode="kueue",
        options=JobOptions(
            scheduling=SchedulingOptions(
                queue_name="user-queue",
            )
        ),
    )
    response = client.post("/jobs", json=jsonable_encoder(body))
    workload_id = WorkloadIdentifier.model_validate_json(response.text)

    time.sleep(0.5)

    # Check workload status
    status: JobStatus = None
    while True:
        response = client.get(f"/jobs/{workload_id.uid}/status")
        assert response.status_code == 200

        status = JobStatus(response.json())
        assert status != JobStatus.FAILED

        if status != JobStatus.PENDING:
            break

        time.sleep(1)

    pp(status)

    # Check workload logs (retry if pod is not ready yet)
    while True:
        response = client.get(f"/jobs/{workload_id.uid}/logs")
        assert response.status_code in [200, 400]

        if response.status_code == 200:
            break
        elif response.status_code == 400:
            assert response.json().get("detail") == "pod not ready"

    # Terminate the workload
    response = client.post(f"/jobs/{workload_id.uid}/stop")
    assert response.status_code == 204
