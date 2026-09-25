"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class GreenlandEntry(BaseModel):
    """公共绿地明细结构。"""

    field_0: str | None = None  # 绿地编码
    field_1: str | None = None  # 绿地名称
    field_2: str | None = None  # 绿地类型
    field_3: str | None = None  # 占地面积
    field_4: str | None = None  # 所属街道
    field_5: str | None = None  # 养护等级
    field_6: str | None = None  # 管护单位
    field_7: str | None = None  # 绿地状态

class StreettreeEntry(BaseModel):
    """行道树明细结构。"""

    field_0: str | None = None  # 树木编号
    field_1: str | None = None  # 树种名称
    field_2: str | None = None  # 胸径
    field_3: str | None = None  # 树高
    field_4: str | None = None  # 所在路段
    field_5: str | None = None  # 栽植年份
    field_6: str | None = None  # 上次修剪日
    field_7: str | None = None  # 树木状态

class FlowerbedEntry(BaseModel):
    """花坛花境明细结构。"""

    field_0: str | None = None  # 花坛编号
    field_1: str | None = None  # 所在绿地
    field_2: str | None = None  # 花卉品种
    field_3: str | None = None  # 栽植面积
    field_4: str | None = None  # 花期起止
    field_5: str | None = None  # 上次更换日
    field_6: str | None = None  # 换花频次
    field_7: str | None = None  # 花坛状态

class NurseryEntry(BaseModel):
    """苗圃苗木明细结构。"""

    field_0: str | None = None  # 苗圃编号
    field_1: str | None = None  # 苗木品种
    field_2: str | None = None  # 规格等级
    field_3: str | None = None  # 育苗株数
    field_4: str | None = None  # 育苗方式
    field_5: str | None = None  # 播种日期
    field_6: str | None = None  # 出圃日期
    field_7: str | None = None  # 苗木状态

class IrrigationEntry(BaseModel):
    """灌溉设施明细结构。"""

    field_0: str | None = None  # 设施编号
    field_1: str | None = None  # 设施类型
    field_2: str | None = None  # 所在绿地
    field_3: str | None = None  # 喷头数量
    field_4: str | None = None  # 水源类型
    field_5: str | None = None  # 上次检修日
    field_6: str | None = None  # 运行压力
    field_7: str | None = None  # 设施状态

class PruningEntry(BaseModel):
    """修剪单明细结构。"""

    field_0: str | None = None  # 修剪单号
    field_1: str | None = None  # 修剪对象
    field_2: str | None = None  # 修剪方式
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 作业班组
    field_5: str | None = None  # 修剪株数
    field_6: str | None = None  # 清运枝叶量
    field_7: str | None = None  # 修剪状态

class PestEntry(BaseModel):
    """防治单明细结构。"""

    field_0: str | None = None  # 防治单号
    field_1: str | None = None  # 有害生物
    field_2: str | None = None  # 危害对象
    field_3: str | None = None  # 危害等级
    field_4: str | None = None  # 防治措施
    field_5: str | None = None  # 用药名称
    field_6: str | None = None  # 防治日期
    field_7: str | None = None  # 防治状态

class FertilizeEntry(BaseModel):
    """施肥单明细结构。"""

    field_0: str | None = None  # 施肥单号
    field_1: str | None = None  # 施肥对象
    field_2: str | None = None  # 肥料品种
    field_3: str | None = None  # 施用方式
    field_4: str | None = None  # 施用数量
    field_5: str | None = None  # 施肥日期
    field_6: str | None = None  # 作业人员
    field_7: str | None = None  # 施肥状态

class ReplantEntry(BaseModel):
    """补植单明细结构。"""

    field_0: str | None = None  # 补植单号
    field_1: str | None = None  # 补植位置
    field_2: str | None = None  # 补植品种
    field_3: str | None = None  # 补植数量
    field_4: str | None = None  # 苗木来源
    field_5: str | None = None  # 计划日期
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 补植状态

class AncientEntry(BaseModel):
    """古树名木明细结构。"""

    field_0: str | None = None  # 古树编号
    field_1: str | None = None  # 树种名称
    field_2: str | None = None  # 树龄
    field_3: str | None = None  # 保护级别
    field_4: str | None = None  # 所在位置
    field_5: str | None = None  # 上次体检日
    field_6: str | None = None  # 复壮措施
    field_7: str | None = None  # 古树状态

class PatrolEntry(BaseModel):
    """巡查单明细结构。"""

    field_0: str | None = None  # 巡查单号
    field_1: str | None = None  # 巡查路线
    field_2: str | None = None  # 巡查人员
    field_3: str | None = None  # 巡查日期
    field_4: str | None = None  # 发现问题数
    field_5: str | None = None  # 整改项数
    field_6: str | None = None  # 巡查时长
    field_7: str | None = None  # 巡查状态

class RectifyEntry(BaseModel):
    """整改单明细结构。"""

    field_0: str | None = None  # 整改单号
    field_1: str | None = None  # 关联问题
    field_2: str | None = None  # 整改措施
    field_3: str | None = None  # 责任单位
    field_4: str | None = None  # 整改期限
    field_5: str | None = None  # 完成日期
    field_6: str | None = None  # 复核人员
    field_7: str | None = None  # 整改状态

class FacilityEntry(BaseModel):
    """园林设施明细结构。"""

    field_0: str | None = None  # 设施编号
    field_1: str | None = None  # 设施类型
    field_2: str | None = None  # 所在绿地
    field_3: str | None = None  # 设施数量
    field_4: str | None = None  # 安装日期
    field_5: str | None = None  # 上次维修日
    field_6: str | None = None  # 损坏数量
    field_7: str | None = None  # 设施状态

class AcceptEntry(BaseModel):
    """养护验收单明细结构。"""

    field_0: str | None = None  # 验收单号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 验收项目
    field_3: str | None = None  # 验收标准
    field_4: str | None = None  # 验收得分
    field_5: str | None = None  # 验收人员
    field_6: str | None = None  # 验收日期
    field_7: str | None = None  # 验收状态

class PlanEntry(BaseModel):
    """养护计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 养护类型
    field_2: str | None = None  # 养护对象
    field_3: str | None = None  # 计划周期
    field_4: str | None = None  # 计划工时
    field_5: str | None = None  # 作业班组
    field_6: str | None = None  # 负责人
    field_7: str | None = None  # 计划状态

class SeasonEntry(BaseModel):
    """时令布置单明细结构。"""

    field_0: str | None = None  # 布置单号
    field_1: str | None = None  # 布置节点
    field_2: str | None = None  # 布置位置
    field_3: str | None = None  # 花卉品种
    field_4: str | None = None  # 布置面积
    field_5: str | None = None  # 布置日期
    field_6: str | None = None  # 撤除日期
    field_7: str | None = None  # 布置状态

class WaterbodyEntry(BaseModel):
    """景观水体明细结构。"""

    field_0: str | None = None  # 水体编号
    field_1: str | None = None  # 水体类型
    field_2: str | None = None  # 所在绿地
    field_3: str | None = None  # 水面面积
    field_4: str | None = None  # 上次清捞日
    field_5: str | None = None  # 水质等级
    field_6: str | None = None  # 水生植物面积
    field_7: str | None = None  # 水体状态

class RecordEntry(BaseModel):
    """养护记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 养护对象
    field_2: str | None = None  # 作业类型
    field_3: str | None = None  # 作业日期
    field_4: str | None = None  # 投入人工
    field_5: str | None = None  # 使用机械
    field_6: str | None = None  # 记录人
    field_7: str | None = None  # 记录状态
