import os

from django.core.management.commands.runserver import Command as BaseRunserverCommand


class Command(BaseRunserverCommand):
    def execute(self, *args, **options):
        os.environ["DJANGO_RUNSERVER_HIDE_WARNING"] = "true"
        return super().execute(*args, **options)

    def on_bind(self, server_port):
        if self._raw_ipv6:
            addr = f"[{self.addr}]"
        elif self.addr == "0":
            addr = "0.0.0.0"
        else:
            addr = self.addr

        self.stdout.write(f"Starting development server at {self.protocol}://{addr}:{server_port}/")
