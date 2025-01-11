def invalidates_cache(f):
    def wrapper(self, *args, **kwargs):
        if self._data:
            self._data = None
        return f(self, *args, **kwargs)
    return wrapper


def fetchy(f):
    async def wrapper(self, *args, **kwargs):
        await self.fetch()
        return f(self, *args, **kwargs)
    return wrapper
