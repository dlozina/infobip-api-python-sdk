from typing import Optional

from pydantic import AnyUrl, constr

from whatsapp.models.core import CamelCaseModel, MessageBody


class Content(CamelCaseModel):
    media_url: AnyUrl
    caption: Optional[constr(max_length=3000)] = None


class VideoMessageBody(MessageBody):
    content: Content
