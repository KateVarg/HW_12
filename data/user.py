import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_day: str
    date_month: str
    date_year: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str
