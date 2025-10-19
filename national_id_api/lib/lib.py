from datetime import datetime, date
import re

from .consts import governorate_codes

def get_birth_governorate_name(code: str) -> str:
    
    """Get the name of the governorate given its code.
    
    Args:
        code (str): The governorate code as a two-digit string.
    
    Returns:
        str: The name of the governorate.
    """

    if not isinstance(code, str):
        raise TypeError("Governorate code must be a string")
    
    if (len(code) != 2) or (not code.isdigit()):
        raise ValueError("Governorate code must be a two-digit string")
    
    if code not in governorate_codes:
        raise ValueError(f"Invalid governorate code: {code}")
    
    return governorate_codes.get(code)

def validate_national_id(national_id: str) -> bool:
    
    """Validate Egyptian national ID number.
    
    Args:
        national_id (str): The national ID number as a string.

    Returns:
        bool: True if the national ID is valid, False otherwise.
    """

    if not isinstance(national_id, str):
        raise TypeError("National ID must be a string")
    
    if (len(national_id) != 14) or (not national_id.isdigit()):
        return False
    else:
        return True
    
def get_birth_date(code: str) -> str:
    
    """Extract the birth date from the national ID.
    
    Args:
        national_id (str): The national ID number as a string.

    Returns:
        str: The birth date in the format 'YYYY-MM-DD'.
    """

    if not isinstance(code, str):
        raise TypeError("code must be a string")
    
    if (len(code) != 7) or (not code.isdigit()):
        raise ValueError("code must be a 7-digit string")
    
    century_code = code[0]
    year = code[1:3]
    month = code[3:5]
    day = code[5:7]
    
    if century_code == '2':
        century = '19'
    elif century_code == '3':
        century = '20'
    else:
        raise ValueError("Invalid century code in national ID")
    
    full_year = century + year
    return f"{full_year}-{month}-{day}"

def get_gender(code: str) -> str:
    
    """Determine the gender from the national ID.
    Args:
        code (str): The code number for the gender section as a string.
    Returns:
        str: The gender ('Male' or 'Female').
    """

    if not isinstance(code, str):
        raise TypeError("code must be a string")

    if (len(code) != 1) or (not code.isdigit()):
        raise ValueError("code must be a single digit string")
    
    gender_digit = int(code)
    if gender_digit % 2 == 0:
        return "Female"
    else:
        return "Male"

def get_birth_order_number(code: str) -> int:
    
    """Extract the birth order number from the national ID.
    
    Args:
        code (str): The birth order number section as a string.

    Returns:
        int: The birth order number.
    """

    if not isinstance(code, str):
        raise TypeError("code must be a string")
    
    if (len(code) != 3) or (not code.isdigit()):
        raise ValueError("code must be a 3-digit string")
    
    return int(code)

def get_age_from_birth_date(birth_date: str) -> int:

    """Calculate age from birth date.
    
    Args:
        birth_date (str): The birth date in the format 'YYYY-MM-DD'.

    Returns:
        int: The age in years.
    """

    if not isinstance(birth_date, str):
        raise TypeError("birth_date must be a string")
    
    if (len(birth_date) != 10) or (not re.match(r"\d{4}-\d{2}-\d{2}", birth_date)):
        raise ValueError("birth_date must be in the format 'YYYY-MM-DD'")
    
    try:
        birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("birth_date must be in the format 'YYYY-MM-DD'")
    
    today = date.today()
    age = today.year - birth_datetime.year - ((today.month, today.day) < (birth_datetime.month, birth_datetime.day))
    return age

def get_national_id_info(national_id: str) -> dict:
    
    """Extract information from the national ID.
    
    Args:
        national_id (str): The national ID number as a string.

    Returns:
        dict: A dictionary containing birth_date, gender, and birth_governorate. 
    """

    if not validate_national_id(national_id):
        raise ValueError("Invalid national ID number")
    
    birth_date = get_birth_date(national_id[:7])
    gender = get_gender(national_id[12])
    birth_governorate = get_birth_governorate_name(national_id[7:9])
    birth_order_number = get_birth_order_number(national_id[9:12])
    age = get_age_from_birth_date(birth_date)
    return {
        "valid": True,
        "birth_date": birth_date,
        "gender": gender,
        "birth_governorate": birth_governorate,
        "birth_order_number": birth_order_number,
        "age": age
    }

