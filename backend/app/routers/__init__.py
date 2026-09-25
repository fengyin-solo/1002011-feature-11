"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import greenland as router_greenland
from app.routers import streettree as router_streettree
from app.routers import flowerbed as router_flowerbed
from app.routers import nursery as router_nursery
from app.routers import irrigation as router_irrigation
from app.routers import pruning as router_pruning
from app.routers import pest as router_pest
from app.routers import fertilize as router_fertilize
from app.routers import replant as router_replant
from app.routers import ancient as router_ancient
from app.routers import patrol as router_patrol
from app.routers import rectify as router_rectify
from app.routers import facility as router_facility
from app.routers import accept as router_accept
from app.routers import plan as router_plan
from app.routers import season as router_season
from app.routers import waterbody as router_waterbody
from app.routers import record as router_record

ROUTERS = [router_greenland, router_streettree, router_flowerbed, router_nursery, router_irrigation, router_pruning, router_pest, router_fertilize, router_replant, router_ancient, router_patrol, router_rectify, router_facility, router_accept, router_plan, router_season, router_waterbody, router_record]
