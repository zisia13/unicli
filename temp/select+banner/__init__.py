try:
    from banner.banner import (
        Banner_Colors as _Banner_Colors,
        Banner_String as _Banner_String
    )
    from banner.recolor import recolor_horizontal_4c, reset
    from select.select import Select
except:
    from .banner.banner import (
        Banner_Colors as _Banner_Colors,
        Banner_String as _Banner_String
    )
    from .banner.recolor import recolor_horizontal_4c, reset
    from .select.select import Select
finally:
    Banner = recolor_horizontal_4c(
        text = _Banner_String,
        color_1 = _Banner_Colors[0],
        color_2 = _Banner_Colors[1],
        color_3 = _Banner_Colors[2],
        color_4 = _Banner_Colors[3]
    ) + reset
