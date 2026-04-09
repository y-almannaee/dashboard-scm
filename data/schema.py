import dataclasses
from typing import Any, Dict
from datetime import datetime, timedelta

# universal data model
class UDM(dataclasses):
	SKU: str
	Grade: str
	Origin: str
	LeadTime: timedelta
	BOM: Dict[BOM, Any]

	def __init__(self):
		pass

class BOM:
	pass