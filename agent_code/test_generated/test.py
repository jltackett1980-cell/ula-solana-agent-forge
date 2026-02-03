# Error parsing ULA: No service definition found

import re
from dataclasses import dataclass, field
from typing import Optional, List, Any
import uuid

class ValidationError(Exception):
    pass
