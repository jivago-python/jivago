# Resource tests
SIMPLE_GET = "Resource:GET"
SIMPLE_POST_DTO = "Resource:Got RequestDto"
DIFFERENT_POST_DTO = "Resource:Got AuthenticatedRequestDto(RequestDto)"
GET_WITH_PARAMETERS = "Resource:Got Query Parameters"
GET_WITH_PATH_PARAMETER = "Resource: Got Path Parameter"

# Runnable
PREINIT = "Hooks:PreInit"
INIT = "Hooks:Init"
POSTINIT = "Hooks:PostInit"

SCHEDULED = "Scheduled:EverySecond"

# Filters
FILTER = "Filtering:Entering Filter"

# Event
RUNNABLE_EVENT_HANDLER = "Event:Got Event in runnable"
INSTANTIATED_EVENT_HANDLER = "Event: Got Event in instantiated handler"
FUNCTION_EVENT_HANDLER = "Event: Got Event in simple function"

# Dependency injection
INSTANTIATED_LAZY_BEAN = "Injection: Instantiated lazy component"
