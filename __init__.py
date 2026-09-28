NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

def _register_module(module):
    NODE_CLASS_MAPPINGS.update(getattr(module, "NODE_CLASS_MAPPINGS", {}))
    NODE_DISPLAY_NAME_MAPPINGS.update(getattr(module, "NODE_DISPLAY_NAME_MAPPINGS", {}))

try:
    from . import PainterVideoCombine
    _register_module(PainterVideoCombine)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterVideoCombine: {e}")

try:
    from . import PainterVideoCombine2
    _register_module(PainterVideoCombine2)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterVideoCombine2: {e}")

try:
    from . import PainterSizeSettings
    _register_module(PainterSizeSettings)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterSizeSettings: {e}")

try:
    from . import PainterVRAM
    _register_module(PainterVRAM)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterVRAM: {e}")

try:
    from . import PainterQwenImage21
    _register_module(PainterQwenImage21)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterQwenImage21: {e}")

try:
    from . import PainterFLF2V
    _register_module(PainterFLF2V)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterFLF2V: {e}")

try:
    from . import PainterMiniMaxRefToVideo
    _register_module(PainterMiniMaxRefToVideo)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterMiniMaxRefToVideo: {e}")

try:
    from . import PainterMiniMaxRefToVideo2
    _register_module(PainterMiniMaxRefToVideo2)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterMiniMaxRefToVideo2: {e}")

try:
    from . import PainterMiniMaxRefToVideo3
    _register_module(PainterMiniMaxRefToVideo3)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterMiniMaxRefToVideo3: {e}")

try:
    from . import PainterMiniMaxRefToVideo6
    _register_module(PainterMiniMaxRefToVideo6)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterMiniMaxRefToVideo6: {e}")

try:
    from . import PainterMinimaxH3LatentUpscaler
    _register_module(PainterMinimaxH3LatentUpscaler)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterMinimaxH3LatentUpscaler: {e}")

try:
    from . import PainterSigmasGraph
    _register_module(PainterSigmasGraph)
except Exception as e:
    print(f"[PainterNodes] Failed to import PainterSigmasGraph: {e}")

print(f"\033[92m[PainterNodes] Loaded {len(NODE_CLASS_MAPPINGS)} nodes successfully!\033[0m")

__version__ = "1.4.5"
WEB_DIRECTORY = "./web/js"

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
    "__version__",
]
