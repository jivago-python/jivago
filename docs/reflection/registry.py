from jivago.inject.annotation import Component
from jivago.lang.registry import Registry

registry = Registry.INSTANCE

registrations = registry.get_annotated_in_package(Component, "")

for registration in registrations:
    registered_class = registration.registered  # Registered class or function
    annotation_parameters = registration.arguments  # empty dictionary for standard annotations
