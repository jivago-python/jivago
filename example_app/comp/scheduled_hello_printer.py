from jivago.lang.annotations import Override
from jivago.lang.registry import Singleton
from jivago.lang.runnable import Runnable
from jivago.scheduling.annotations import Scheduled, Duration


@Singleton
@Scheduled(cron="* * * * *")
class ScheduledHelloPrinter(Runnable):

    def __init__(self):
        print("created a new scheduled hello printer")

    @Override
    def run(self):
        print("hello !")


@Scheduled(every=Duration.SECOND)
class RegularIntervalScheduledHelloPrinter(Runnable):

    @Override
    def run(self):
        print("Hello every second!")