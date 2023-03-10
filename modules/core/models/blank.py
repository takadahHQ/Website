from django.db import models
from django.conf import settings
from modules.core.models.include import (
    idModel,
    statusModel,
    timeStampModel,
    CacheInvalidationMixin,
    CachedQueryManager,
)
