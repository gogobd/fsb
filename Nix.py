class Nix(object):
    """Nix with infinite attributes"""
    def __getattr__(self, *args, **kwargs):
        return self

Nix = Nix()
