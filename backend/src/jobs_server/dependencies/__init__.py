from typing import Annotated

from fastapi import Depends, HTTPException

from jobs_server.models import JobId
from jobs_server.services.k8s import KubernetesService
from jobs_server.utils.kueue import KueueWorkload


def k8s_service() -> KubernetesService:
    return KubernetesService()


def managed_workload(
    k8s: Annotated[KubernetesService, Depends(k8s_service)],
    uid: JobId,
    namespace: str = "default",
) -> KueueWorkload:
    wl = k8s.workload_for_managed_resource(uid, namespace)
    if wl is None:
        raise HTTPException(404, "workload not found")
    return wl
