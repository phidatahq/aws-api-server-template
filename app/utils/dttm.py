import pendulum


def current_utc() -> pendulum.DateTime:
    return pendulum.now("UTC")


def current_utc_str() -> str:
    return current_utc().to_datetime_string()


def current_est() -> pendulum.DateTime:
    return pendulum.now("America/New_York")


def current_est_str() -> str:
    return current_est().to_datetime_string()


def current_pst() -> pendulum.DateTime:
    return pendulum.now("America/Los_Angeles")


def current_pst_str() -> str:
    return current_pst().to_datetime_string()
