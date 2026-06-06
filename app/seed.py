from app.models import Record


def default_records() -> list[Record]:
    return [
        Record("r1", "Marina Booking Desk 首轮安排", "oliver", "进行中", "高", "先确认核心节点和资源。"),
        Record("r2", "Marina Booking Desk 周会", "mira", "待处理", "中", "整理当前风险和后续动作。"),
    ]
