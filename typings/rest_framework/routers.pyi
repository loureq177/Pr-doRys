"""
This type stub file was generated by pyright.
"""

from rest_framework import views
from rest_framework.schemas import SchemaGenerator
from rest_framework.schemas.views import SchemaView

"""
Routers provide a convenient and consistent way of automatically
determining the URL conf for your API.

They are used by simply instantiating a Router class, and then registering
all the required ViewSets with that router.

For example, you might have a `urls.py` that looks something like this:

    router = routers.DefaultRouter()
    router.register('users', UserViewSet, 'user')
    router.register('accounts', AccountViewSet, 'account')

    urlpatterns = router.urls
"""
Route = ...
DynamicRoute = ...
def escape_curly_brackets(url_path):
    """
    Double brackets in regex of url_path for escape string formatting
    """
    ...

def flatten(list_of_lists): # -> chain[Any]:
    """
    Takes an iterable of iterables, returns a single iterable containing all items
    """
    ...

class BaseRouter:
    def __init__(self) -> None:
        ...
    
    def register(self, prefix, viewset, basename=...): # -> None:
        ...
    
    def is_already_registered(self, new_basename): # -> bool:
        """
        Check if `basename` is already registered
        """
        ...
    
    def get_default_basename(self, viewset):
        """
        If `basename` is not specified, attempt to automatically determine
        it from the viewset.
        """
        ...
    
    def get_urls(self):
        """
        Return a list of URL patterns, given the registered viewsets.
        """
        ...
    
    @property
    def urls(self):
        ...
    


class SimpleRouter(BaseRouter):
    routes = ...
    def __init__(self, trailing_slash=..., use_regex_path=...) -> None:
        ...
    
    def get_default_basename(self, viewset): # -> Any:
        """
        If `basename` is not specified, attempt to automatically determine
        it from the viewset.
        """
        ...
    
    def get_routes(self, viewset): # -> list[Any]:
        """
        Augment `self.routes` with any dynamically generated routes.

        Returns a list of the Route namedtuple.
        """
        ...
    
    def get_method_map(self, viewset, method_map): # -> dict[Any, Any]:
        """
        Given a viewset, and a mapping of http methods to actions,
        return a new mapping which only includes any mappings that
        are actually implemented by the viewset.
        """
        ...
    
    def get_lookup_regex(self, viewset, lookup_prefix=...): # -> str:
        """
        Given a viewset, return the portion of URL regex that is used
        to match against a single instance.

        Note that lookup_prefix is not used directly inside REST rest_framework
        itself, but is required in order to nicely support nested router
        implementations, such as drf-nested-routers.

        https://github.com/alanjds/drf-nested-routers
        """
        ...
    
    def get_urls(self): # -> list[Any]:
        """
        Use the registered viewsets to generate a list of URL patterns.
        """
        ...
    


class APIRootView(views.APIView):
    """
    The default basic root view for DefaultRouter
    """
    _ignore_model_permissions = ...
    schema = ...
    api_root_dict = ...
    def get(self, request, *args, **kwargs): # -> Response:
        ...
    


class DefaultRouter(SimpleRouter):
    """
    The default router extends the SimpleRouter, but also adds in a default
    API root view, and adds format suffix patterns to the URLs.
    """
    include_root_view = ...
    include_format_suffixes = ...
    root_view_name = ...
    default_schema_renderers = ...
    APIRootView = APIRootView
    APISchemaView = SchemaView
    SchemaGenerator = SchemaGenerator
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def get_api_root_view(self, api_urls=...): # -> Callable[..., HttpResponse]:
        """
        Return a basic root view.
        """
        ...
    
    def get_urls(self): # -> list[Any]:
        """
        Generate the list of URL patterns, including a default root view
        for the API, and appending `.json` style format suffixes.
        """
        ...
    

