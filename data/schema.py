import dataclasses
from typing import Any, Dict
from datetime import datetime, timedelta

# universal data model
@dataclasses.dataclass
class UDM:
	SKU: str
	Grade: str
	Origin: str
	LeadTime: timedelta
	BOM: Dict[str, Any]

	def __init__(self, **kwargs):
		# Set attributes from kwargs
		for key, value in kwargs.items():
			setattr(self, key, value)
		pass

class BOM:
	pass
