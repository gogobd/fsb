class NONE(object):
    """NONE with infinite attributes"""
    def __getattr__(self, *args, **kwargs):
        return self

NONE = NONE()
