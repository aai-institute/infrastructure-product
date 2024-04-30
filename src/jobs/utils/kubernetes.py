from __future__ import annotations

import kubernetes


def sanitize_rfc1123_domain_name(s: str) -> str:
    """Sanitize a string to be compliant with RFC 1123 domain name

    Note: Any invalid characters are replaced with dashes."""

    # TODO: This is obviously wildly incomplete
    return s.replace("_", "-")


class KubernetesNamespaceMixin:
    """Determine the desired or current Kubernetes namespace."""

    def __init__(self, **kwargs):
        kubernetes.config.load_config()
        self._namespace: str | None = kwargs.get("namespace")

    @property
    def namespace(self) -> str:
        _, active_context = kubernetes.config.list_kube_config_contexts()
        current_namespace = active_context["context"].get("namespace")
        return self._namespace or current_namespace
