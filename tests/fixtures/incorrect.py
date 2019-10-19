# -*- coding: utf-8 -*-

def function(
    pos,  # noqa: FPO100
    /,
    arg1,
    arg2: int,
    default1=None,
    default2: int = None,
    *args,
    kw_only1,
    kw_only2: int,
    kw_only3: int = None,
    **kwargs,
):
    ...


async def coroutine(
    pos,  # noqa: FPO100
    /,
    arg1,
    arg2: int,
    default1=None,
    default2: int = None,
    *args,
    kw_only1,
    kw_only2: int,
    kw_only3: int = None,
    **kwargs,
):
    ...


class Test(object):
    def function(
        self,  # noqa: FPO100
        /,
        arg1,
        arg2: int,
        default1=None,
        default2: int = None,
        *args,
        kw_only1,
        kw_only2: int,
        kw_only3: int = None,
        **kwargs,
    ):
        ...


    async def coroutine(
        self,  # noqa: FPO100
        /,
        arg1,
        arg2: int,
        default1=None,
        default2: int = None,
        *args,
        kw_only1,
        kw_only2: int,
        kw_only3: int = None,
        **kwargs,
    ):
        ...

test_lambda = lambda x, /: x
