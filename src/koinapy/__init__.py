class Koina:
    """Stub Koina client used to disable Prosit integration in the harness."""

    def __init__(self, *args, **kwargs):
        pass

    def predict(self, *args, **kwargs):
        raise RuntimeError(
            "Koina (Prosit) predictions are not available in this harness. "
            "Install koinapy with gRPC support and remove the stub module if Prosit support is required."
        )
