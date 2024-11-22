import logging.config

from dependency_injector import containers, providers
from requests import Session

from app.adaptors.chat_open_ai import ChatOpenAIAdapter
from app.services.llm_service import LLMService
from app.services.movie_service import MovieService
from app.services.request_service import RequestService
from app.utils.template_manager import TemplateManager


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    session = providers.Factory(Session)

    # Providers
    custom_request_service = providers.Factory(
        RequestService,
        token=config.themoviedb.access_token,  # token
        session=session
    )
    adapter = providers.Factory(
        ChatOpenAIAdapter,
        model="gpt-3.5-turbo",
        temperature=0
    )
    template = providers.Factory(
        TemplateManager
    )
    llm_service = providers.Factory(
        LLMService,
        chat_model=adapter,
        template_manager=template
    )
    # Services
    movie_service = providers.Factory(
        MovieService,
        service=custom_request_service
    )
