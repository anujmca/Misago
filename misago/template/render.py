from typing import Optional

from starlette.requests import Request
from starlette.responses import Response

from ..types import TemplateContext
from .context import get_final_context
from .environment import env


async def render(
    request: Request,
    template_name: str,
    context: Optional[TemplateContext] = None,
    *,
    status_code: int = 200,
    media_type: str = "text/html",
) -> Response:
    final_context = await get_final_context(request, context)
    content = await render_to_string(template_name, final_context)
    return Response(content, status_code=status_code, media_type=media_type)


async def render_to_string(
    template_name: str, context: Optional[TemplateContext] = None
) -> str:
    template = env.get_template(template_name)
    return await template.render_async(context or {})