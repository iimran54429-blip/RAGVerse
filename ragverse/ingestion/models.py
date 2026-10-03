from dataclasses import dataclass
from datetime import datetime


@dataclass
class DocumentMetadata:
    document_id: str
    document_name: str
    source: str
    upload_date: datetime
    file_type: str