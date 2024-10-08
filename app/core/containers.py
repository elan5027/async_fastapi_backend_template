from dependency_injector import providers, containers
from app.core.config import BaseAppSettings

# Service
from app.services.user_service import UserService
from app.services.image_service import ImageService

# Client
from app.clients.s3_client import S3Client

# Repository
from app.db.repositories.user_repository import UserRepository
from app.core.redis import RedisLock, RedisCache


class Container(containers.DeclarativeContainer):
    config: BaseAppSettings = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.api",
            "app.api.v1",
            "app.core",
            "app.services",
            "app.db.repositories",
        ]
    )

    redis_lock = providers.Singleton(RedisLock)
    redis_cache = providers.Singleton(RedisCache)

    # clients
    s3_client = providers.Factory(
        S3Client,
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        bucket=config.bucket,
        aws_region=config.aws_region,
    )

    # repositories
    user_repository = providers.Factory(
        UserRepository,
    )

    # services
    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
        # smtp_client=smtp_client,
        key=config.user_key,
        iv=config.seed_key,
    )

    image_service = providers.Factory(ImageService, s3_client=s3_client)
