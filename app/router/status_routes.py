from fastapi import APIRouter

from app.router.endpoints import endpoints
from app.utils.dttm import (
    current_utc_str,
    current_est_str,
    current_pst_str,
)

######################################################
## Router for Health Checks
######################################################

status_router = APIRouter(tags=["status"])


@status_router.get(endpoints.PING)
def status_ping():
    return {
        "status": "success",
        "router": "status",
        "path": endpoints.PING,
        "utc": current_utc_str(),
        "pst": current_pst_str(),
        "est": current_est_str(),
    }


@status_router.get(endpoints.HEALTH)
def status_health():
    return {
        "status": "success",
        "router": "status",
        "path": endpoints.HEALTH,
        "utc": current_utc_str(),
        "pst": current_pst_str(),
        "est": current_est_str(),
    }
