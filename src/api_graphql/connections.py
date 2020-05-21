from graphene import Int
from graphene import Connection

# Create your connections here


class TotalCountConnection(Connection):
    total_count = Int()

    class Meta:
        abstract = True

    def resolve_total_count(self, info):
        return self.length
